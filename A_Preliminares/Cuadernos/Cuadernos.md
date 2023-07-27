Este es el directorio de cuadernos preliminares.

Aquí podemos comenzar a trabajar con el lenguaje markdown. Estoy escribiendo en markdown

Podemos escribir *En itálico* o en **negrita**

Podemos incluso definir títulos de distintos tamaños

# Título 1
## Título 2
### Título 3
#### Título 4

> Es posible hacer bloques de citas

* Hacer listas
* Hacer listas
* Hacer listas

Hacer una tabla

|columna 1|columna 2|
|---------|---------|
|valor1   |valor2   |

Hacemos una cita al pie de pagína. [^1]

[^1]: Aquí va el pie de página.


O una lista de tareas 
- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media


Para escribir terminos en "Math Mode", agregamos `$ $` entre la frase. Por ejemplo $X + 1 = 7$.

LaTeX tiene múltiples convenciones para llamar símbolos, y funciones para hacer ecuaciones. Hagamos por ejemplo la ecuación de la media poblacional.

\begin{align}
    \mu = \frac{\sum_{i=1}^{N}X_{i}}{N}
\end{align}

Podemos también hacer cosas como matrices

\begin{pmatrix}
1 & 2 & 3\\
a & b & c
\end{pmatrix}

E insertarlas dentro del texto cambiando su tamaño usando $\big(\begin{smallmatrix}a & b\\c & d\end{smallmatrix}\big)$ 

Para aprender las múltiples convenciones es buena idea visitar [overleaf](https://www.overleaf.com/learn)


Usando HTML podemos hacer cosas como cambiar colores, tamaños de forma más detallada, cambiar la fuente, y la alineación

<h1 style="color:blue;">Este es un título de color</h1>

<h1>Un <span style="color:red">Importante</span> mensaje</h1>


<h1 style="font-family:verdana;">este es un título en Verdana</h1>

<h1 style="font-size:400%;">Este es un título con un cambio de tamaño porcentual</h1>

<h1 style="font-size:30px;">Título con un cambio de tamaño en pixeles</h1>

<h1 style="text-align:center;color:green;">Título centrado con cambio de color</h1>