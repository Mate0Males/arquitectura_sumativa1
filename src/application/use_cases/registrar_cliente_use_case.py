from src.application.ports.pedido_repository import PedidoRepositoryPort
from src.domain.clientes.cliente import Cliente

class RegistrarClienteUseCase:

    def __init__(self, repository: PedidoRepositoryPort):
        self.repository = repository

    def ejecutar(self, cedula: str, nombre: str, categoria: str) -> str:
        cliente_existente = self.repository.buscar_cliente_por_cedula(cedula)
        if cliente_existente:
            return "El cliente ya existe."

        nuevo_cliente = Cliente(cedula=cedula, nombre=nombre, categoria=categoria)
        self.repository.guardar_cliente(nuevo_cliente)
        return "Cliente registrado correctamente."