# TDD Juego de la Vida de Jhon Conway en Python

_Autor: Jose G Solano Romero_

_El proyecto es el desarrollo de la logica del Juego de la vida del matematico Jhon Conway aplicando TDD en Python_

## Reglas de juego 🚀

_El desarrollo del proyecto se basa en crear la logica del juego de la vida utilizando TDD (Test Driven Development) desde el inicio._
_No requiere una UI, ese no es objetivo, sino de aprender el como se debe aplicar TDD a un proyecto._
_El proyecto se basara en las siguientes 4 reglas del juego:_

* Cualquier célula viva con menos de dos vecinos vivos muere.
* Cualquier célula viva con dos o tres vecinos vivos sigue viviendo para la siguiente generación.
* Cualquier célula viva con más de tres vecinos vivos muere (cantidad maxima 8 vecinos en una grilla).
* Cualquier célula muerta con exactamente tres vecinos vivos se convierte en una célula viva.


### Pre-requisitos 📋

_Para poder hacer correr el proyecto es necesario las siguientes herramientas_

* Python 3.7.
* Editor de texto o IDE (Visual Studio, Visual Studio Code, PyCharm, etc..).
* Un Entorno de Python (Puede ser el por defecto, o uno creado por el IDE)
* Tener instalado en el Entorno UnitTest para realizar las pruebas

### Instalación 🔧

_Clonar o descargar el proyecto desde el GitHub, de prefencia con un IDE que soporte o tenga integracion con Python_

_El IDE utilizado fue Visual Studio 2019 Enterprise, con modificaciones para trabajar con Python_

_En caso de usar editor de texto, abrir la carpeta del proyecto._


## Ejecutando las pruebas ⚙️

Si se utiliza un IDE, deberia reconocer las pruebas como tal, en caso de no realizarlo solo se debe referenciar el archivo "TestGameOfLife.py"

Si se utiliza un Editor de texto, es recomendable instalar una extension de prueba de python.

Si no se cuenta con una extension del editor de texto, o desea realizarlo mediante consola debe seguir los siguientes pasos:

Abrir la consola de sistema(cmd, bash, windows PowerShell, etc) y crear un entorno de python

```
$ python -m venv mi-entorno-virtual
```

Teniendo el Entorno Activado, dentro de la carpeta del proyecto, ejecutar el archivo de pruebas

```
$ py TestGameOfLife.py
```

Y podremos visualizar los resultados de las pruebas!!
