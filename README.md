# Sistema de Gestión de Pedidos de Comida (Código Espagueti)

Este repositorio contiene una versión de demostración de un Sistema de Gestión de Pedidos de Comida desarrollado en Python mediante una aplicación de consola.

Esta rama representa la implementación utilizando la arquitectura conocida como **Código Espagueti**.

## Descripción

En esta versión, toda la funcionalidad del sistema se encuentra concentrada en un único archivo (`main.py`). La lógica de negocio, la gestión de datos y la interacción con el usuario están mezcladas dentro del mismo flujo de ejecución.

El propósito de esta implementación es evidenciar los problemas que surgen cuando una aplicación crece sin una adecuada organización de responsabilidades.

## Funcionalidades

El sistema permite:

* Registrar productos de comida.
* Visualizar los productos registrados.
* Crear pedidos a partir de los productos disponibles.
* Consultar los pedidos realizados.
* Marcar pedidos como entregados.

## Características de la versión "Código Espagueti"

* Toda la aplicación se encuentra en un único archivo (`main.py`).
* Uso de listas y variables globales para almacenar información.
* Ausencia de clases y objetos de dominio.
* No existe separación entre la interfaz de usuario y la lógica de negocio.
* Manipulación directa de datos desde diferentes secciones del programa.
* Alta dependencia entre componentes.
* Escasa reutilización de código.
* Difícil mantenimiento y escalabilidad.


## Requisitos

* Python 3.x

## Ejecución

Desde la terminal, ubicarse en la carpeta del proyecto y ejecutar:

```bash
python main.py
```

## Limitaciones

Esta implementación presenta varios problemas comunes en sistemas poco estructurados:

* Dificultad para agregar nuevas funcionalidades.
* Mayor probabilidad de introducir errores al realizar cambios.
* Baja mantenibilidad.
* Escalabilidad limitada.
* Complicaciones para realizar pruebas unitarias.

