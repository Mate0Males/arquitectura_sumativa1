from typing import List
from src.application.ports.pedido_repository import PedidoRepositoryPort
from src.domain.pedidos.pedido import Pedido

class VerPedidosUseCase:

    def __init__(self, repository: PedidoRepositoryPort):
        self.repository = repository

    def ejecutar(self) -> List[Pedido]:
        return self.repository.obtener_pedidos()