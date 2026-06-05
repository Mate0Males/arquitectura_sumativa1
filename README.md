# arquitectura_sumativa1

Proyecto académico para la materia de Arquitectura de Software que evalúa la evolución de un Sistema de Gestión de Pedidos de Comida.

## Descripción

Este repositorio presenta tres enfoques distintos para implementar el mismo dominio de negocio:

* **feature/espagueti:** una versión con anti-patrones y diseño poco modular.
* **feature/capas:** un enfoque monolítico organizado en capas.
* **feature/ddd:** una implementación basada en Domain-Driven Design (DDD).

Cada enfoque reside en su propia rama `feature/` y permite comparar cómo evoluciona la arquitectura desde una implementación básica y poco estructurada hasta un diseño más mantenible, escalable y alineado con buenas prácticas de desarrollo.

## Dominio del Proyecto

El sistema permite gestionar pedidos de comida mediante funcionalidades como:

* Registro de productos.
* Consulta de productos disponibles.
* Creación de pedidos.
* Consulta de pedidos registrados.
* Actualización del estado de los pedidos.
* Gestión básica del flujo de entrega.

## Propósito

* Mostrar las limitaciones y riesgos del código espagueti.
* Comparar la organización de una arquitectura monolítica por capas.
* Explorar los beneficios de Domain-Driven Design (DDD) en un sistema de gestión de pedidos.
* Analizar cómo una misma problemática puede resolverse utilizando distintos enfoques arquitectónicos.

## Estructura de Ramas

| Rama              | Arquitectura               |
| ----------------- | -------------------------- |
| feature/espagueti | Código Espagueti           |
| feature/capas     | Monolítico por Capas       |
| feature/ddd       | Domain-Driven Design (DDD) |

## Tecnologías Utilizadas

* Python 3
* Git
* Visual Studio Code
