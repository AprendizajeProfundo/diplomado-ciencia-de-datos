import re
import datetime
import requests
import pandas as pd
from bs4 import BeautifulSoup
from html2text import html2text

def get_news(url):
    # Respuesta del servidor
    response = requests.get(url)
    # Obtener el código html en estructuras significantes
    soup = BeautifulSoup(response.text, "html.parser")
    # Para unir root con otros subdominios
    url = '/'.join(url.split('/')[:-1])
    # Segmentar tipo de info según fuente
    ### El tiempo
    if 'eltiempo' in url:
        source = 'eltiempo'
        ### Lo más avanzado, sacar info específica
        titulos_html = soup.find_all('a',{'class':'title page-link'})
    else:
        source = 'semana'
        ### Lo más avanzado, sacar info específica
        titulos_html = soup.find_all('a',{'target':'_self'})
        
    # Obtener titulos
    titulos = [html2text(str(titulo)).split('(')[0] for titulo in titulos_html]
    # Obtener links
    subdomains = [html2text(str(titulo)).split('(')[1] for titulo in titulos_html]
    subdomains = ['/'+sub if sub[0]!='/' else sub for sub in subdomains]
    links = ['('+url+sub for sub in subdomains]
    
    # Cruzar Datos para DataFrame
    data_raw = zip(titulos,links)
    # Construir DataFrame
    datos = pd.DataFrame(data_raw,columns=['Titular','Link'])
    
    # Limpieza General (Expresiones Regulares -> Investigar)
    datos['Titular'] = datos['Titular'].replace('\[|\]','',regex=True)
    datos['Link'] = datos['Link'].replace('\(|\)','',regex=True)
    datos['Titular'] = datos['Titular'].replace('\n',' ',regex=True)
    datos['Link'] = datos['Link'].replace('\n','',regex=True)
    
    ############ Extraer texto de cada noticia #########
    
    noticias = []
    fecha = []
    
    for i, url in enumerate(datos['Link']):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        texto_raw = soup.find_all('p',{'class':'contenido'})
        
        texto_limpio = html2text(str(texto_raw))
        #Quitar links
        texto_limpio = re.sub(r'\([^)]*\)',' ',texto_limpio)
        # Quitar paréntesis redondos y cuadrados después de quitar links
        texto_limpio = re.sub(r'[\[\]\(\)]','',texto_limpio)
        # Quitar saltos de línea
        texto_limpio = re.sub(r'\n',' ',texto_limpio)
        # Quitar asteriscos
        texto_limpio = re.sub(r'\*',' ',texto_limpio)
        # Quitar comillas sencillas y reemplazar por dobles
        texto_limpio = re.sub(r"[\\']",'\'',texto_limpio)
        # Quitar todo lo que no tenga punto al final, después del punto final.
        texto_limpio = re.sub(r'([^.]*$)','',texto_limpio)
        # Quitar Espacios extra (dos o más)
        texto_limpio = re.sub('\s\s+', ' ',texto_limpio)
        # Quitar el patrón . , [texto]
        texto_limpio = re.sub('\.\s,\s', '. ',texto_limpio)
        # Algunos países tienen prob
        texto_limpio = re.sub(u'\\\'xa0','',texto_limpio)
        texto_limpio = re.sub(u', ✕(\s?\!?) , ','',texto_limpio)
        #texto_limpio = re.sub(u"\d\.\s(.*)",'',texto_limpio)
        # Quitar espacios iniciales y finales
        texto_limpio = texto_limpio.strip()
        noticias.append(texto_limpio)
        #print(texto_limpio)
        
        # Extraer Fechas
        fecha_raw = soup.find_all('span',{'class':'publishedAt'})
        fecha_limpia = html2text(str(fecha_raw[-1] if len(fecha_raw)>0 else fecha_raw))
        #print(fecha_limpia, type(fecha_limpia))
        
        print(f'{i+1}. {url}')
        
    datos['Noticia'] = noticias
    datos['Fecha'] = fecha_limpia
    
    
    # Como guardar en archivo .csv???
    datos.to_csv(f'{source}_{str(datetime.date.today())}.csv',index=False)
    
    return datos