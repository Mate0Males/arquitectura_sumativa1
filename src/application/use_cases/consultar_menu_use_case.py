from typing import List
from src.application.ports.pedido_repository import PedidoRepositoryPort
from src.domain.catalogo.producto import Producto

class ConsultarMenuUseCase:

    def __init__(self, repository: PedidoRepositoryPort):
        self.repository = repository

    def ejecutar(self) -> List[Producto]:
        return self.repository.obtener_productos()