from src.application.ports.pedido_repository import PedidoRepositoryPort
from src.domain.pedidos.pedido import Pedido

class CrearPedidoUseCase:

    def __init__(self, repository: PedidoRepositoryPort):
        self.repository = repository

    def ejecutar(self, cedula_cliente: str, productos_solicitados: list) -> Pedido:
        cliente = self.repository.buscar_cliente_por_cedula(cedula_cliente)
        if cliente is None:
            return None

        pedido = Pedido(
            cliente_cedula=cliente.cedula,
            cliente_nombre=cliente.nombre,
            categoria_cliente=cliente.categoria
        )

        for item in productos_solicitados:
            producto = self.repository.buscar_producto_por_id(item["producto_id"])
            if producto is None:
                raise ValueError(f"Producto con ID {item['producto_id']} no encontrado.")

            pedido.agregar_producto(producto, item["cantidad"])
            self.repository.actualizar_producto(producto)

        if len(pedido.lineas) == 0:
            return None

        return self.repository.guardar_pedido(pedido)