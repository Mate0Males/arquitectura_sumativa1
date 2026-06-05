# Sistema de Gestión de Pedidos de Comida - Arquitectura Hexagonal y DDD

## Descripción

Este proyecto implementa un Sistema de Gestión de Pedidos de Comida utilizando los principios del **Diseño Guiado por el Dominio (DDD)** y **Arquitectura Hexagonal (Puertos y Adaptadores)**. El objetivo principal es aislar las reglas de negocio del dominio de cualquier infraestructura técnica o interfaz de usuario, garantizando un software altamente mantenible, escalable y acoplado de forma limpia.

## Arquitectura Implementada

La aplicación está organizada siguiendo la separación de capas orientada a DDD y el flujo de dependencias concéntrico hacia el núcleo de negocio:

### 1. Capa de Dominio (`src/domain/`)
Es el corazón del sistema, completamente agnóstica de frameworks o librerías externas. Contiene:
* **Entidades y Objetos de Valor:** Modelos enriquecidos con su propia lógica y validaciones (`Producto`, `Cliente`, `Pedido`, `LineaPedido`, `Factura`).
* **Lógica del Dominio:** Reglas esenciales como la verificación y reducción de stock, o el cálculo automático de subtotales, descuentos y totales.

### 2. Capa de Aplicación (`src/application/`)
Orquesta el comportamiento del sistema y sirve de puente entre el mundo exterior y el dominio:
* **Puertos (`ports/`):** Interfaces abstractas (`PedidoRepositoryPort`) que definen los contratos que la infraestructura debe cumplir.
* **Casos de Uso (`use_cases/`):** Flujos específicos e independientes de la aplicación (`ConsultarMenuUseCase`, `RegistrarClienteUseCase`, `CrearPedidoUseCase`, `VerPedidosUseCase`).

### 3. Capa de Infraestructura (`src/infraestructure/`)
Contiene los detalles técnicos y adaptadores que se conectan a los puertos definidos por la aplicación:
* **Adaptadores de Entrada (UI):** `PedidoController` en `console_ui.py`, encargado de interactuar con el usuario por consola y ejecutar los casos de uso.
* **Adaptadores de Salida (Persistencia):** `InMemoryPedidoRepository` en `memory_db.py`, encargado de simular el almacenamiento y persistencia de datos implementando el puerto del repositorio.

## Funcionalidades Ubicuas

* **Consultar Menú:** Recupera los productos disponibles con sus precios y existencias actuales.
* **Registrar Cliente:** Registra nuevos compradores bajo categorías de negocio (`Regular` / `Frecuente`).
* **Crear Pedido con Lógica de Dominio:** * Valida y disminuye el stock en tiempo real en la entidad del dominio.
  * Calcula descuentos dinámicos (10%) si el cliente cumple el criterio de ser "Frecuente".
  * Genera una factura estructurada basada en el estado del pedido.
* **Historial de Pedidos:** Almacena y expone las transacciones realizadas en memoria.


## Ejecución

Desde la terminal, ubicarse en la carpeta del proyecto y ejecutar:

```bash
python main.py
```

## Limitaciones del Sistema

* **Persistencia volátil:** Los datos se almacenan en memoria, por lo que todo se borra al cerrar el programa.
* **Sin control de concurrencia:** No soporta accesos simultáneos de múltiples usuarios en tiempo real.
* **Interfaz síncrona:** La consola bloquea el flujo del programa mientras espera que el usuario escriba.
* **Acoplamiento de modelos:** Las entidades de dominio se guardan directamente sin un mapeador (*Data Mapper*) hacia la persistencia.