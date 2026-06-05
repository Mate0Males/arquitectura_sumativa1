from typing import List
from src.application.ports.pedido_repository import PedidoRepositoryPort
from src.domain.catalogo.producto import Producto
from src.domain.clientes.cliente import Cliente
from src.domain.pedidos.pedido import Pedido

PRODUCTOS_DB = [
    Producto(id=1, nombre="Hamburguesa Clásica", precio=4.50, stock=15),
    Producto(id=2, nombre="Pizza Personal", precio=6.75, stock=10),
    Producto(id=3, nombre="Hot Dog Especial", precio=3.25, stock=20)
]

CLIENTES_DB = [
    Cliente(cedula="1101234567", nombre="Carlos Mendoza", categoria="Regular"),
    Cliente(cedula="1107654321", nombre="Ana Torres", categoria="Frecuente")
]

PEDIDOS_DB = []

class InMemoryPedidoRepository(PedidoRepositoryPort):

    def obtener_productos(self) -> List[Producto]:
        return PRODUCTOS_DB

    def buscar_producto_por_id(self, producto_id: int) -> Producto:
        for producto in PRODUCTOS_DB:
            if producto.id == producto_id:
                return producto
        return None

    def actualizar_producto(self, producto: Producto):
        for idx, p in enumerate(PRODUCTOS_DB):
            if p.id == producto.id:
                PRODUCTOS_DB[idx] = producto
                break

    def obtener_clientes(self) -> List[Cliente]:
        return CLIENTES_DB

    def buscar_cliente_por_cedula(self, cedula: str) -> Cliente:
        for cliente in CLIENTES_DB:
            if cliente.cedula == cedula:
                return cliente
        return None

    def guardar_cliente(self, cliente: Cliente):
        CLIENTES_DB.append(cliente)

    def obtener_pedidos(self) -> List[Pedido]:
        return PEDIDOS_DB

    def guardar_pedido(self, pedido: Pedido) -> Pedido:
        pedido.id = len(PEDIDOS_DB) + 1
        PEDIDOS_DB.append(pedido)
        return pedido