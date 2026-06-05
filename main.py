from repositories.pedido_repository import PedidoRepository
from services.pedido_service import PedidoService
from controllers.pedido_controller import PedidoController

def main():
    repository = PedidoRepository()
    service = PedidoService(repository)
    controller = PedidoController(service)

    controller.iniciar()

if __name__ == "__main__":
    main()