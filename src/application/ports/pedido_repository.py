from abc import ABC, abstractmethod
from typing import List
from src.domain.catalogo.producto import Producto
from src.domain.clientes.cliente import Cliente
from src.domain.pedidos.pedido import Pedido

class PedidoRepositoryPort(ABC):

    @abstractmethod
    def obtener_productos(self) -> List[Producto]:
        pass

    @abstractmethod
    def buscar_producto_por_id(self, producto_id: int) -> Producto:
        pass

    @abstractmethod
    def actualizar_producto(self, producto: Producto):
        pass

    @abstractmethod
    def obtener_clientes(self) -> List[Cliente]:
        pass

    @abstractmethod
    def buscar_cliente_por_cedula(self, cedula: str) -> Cliente:
        pass

    @abstractmethod
    def guardar_cliente(self, cliente: Cliente):
        pass

    @abstractmethod
    def obtener_pedidos(self) -> List[Pedido]:
        pass

    @abstractmethod
    def guardar_pedido(self, pedido: Pedido) -> Pedido:
        pass