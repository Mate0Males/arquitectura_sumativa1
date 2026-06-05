from typing import List
from src.domain.catalogo.producto import Producto

class LineaPedido:

    def __init__(self, producto: Producto, cantidad: int):
        if cantidad <= 0:
            raise ValueError(
                "La cantidad debe ser mayor que cero."
            )

        self.producto = producto
        self.cantidad = cantidad
        self.subtotal = producto.precio * cantidad

class Pedido:

    def __init__(
        self,
        cliente_cedula: str,
        cliente_nombre: str,
        categoria_cliente: str
    ):
        self.id = None
        self.cliente_cedula = cliente_cedula
        self.cliente_nombre = cliente_nombre
        self.categoria_cliente = categoria_cliente.upper()
        self.lineas: List[LineaPedido] = []

    def agregar_producto(
        self,
        producto: Producto,
        cantidad: int
    ):
        if not producto.tiene_stock_suficiente(cantidad):
            raise ValueError(
                f"Stock insuficiente para {producto.nombre}. "
                f"Disponibles: {producto.stock}"
            )

        producto.disminuir_stock(cantidad)
        linea = LineaPedido(producto, cantidad)
        self.lineas.append(linea)

    def calcular_subtotal(self) -> float:
        return sum(
            linea.subtotal
            for linea in self.lineas
        )

    def calcular_descuento(self) -> float:
        subtotal = self.calcular_subtotal()
        if self.categoria_cliente == "FRECUENTE":
            return subtotal * 0.10
        return 0

    def calcular_total(self) -> float:
        subtotal = self.calcular_subtotal()
        descuento = self.calcular_descuento()
        return subtotal - descuento