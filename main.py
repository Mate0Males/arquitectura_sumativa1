from src.infraestructure.memory_db import InMemoryPedidoRepository
from src.application.use_cases.consultar_menu_use_case import ConsultarMenuUseCase
from src.application.use_cases.registrar_cliente_use_case import RegistrarClienteUseCase
from src.application.use_cases.crear_pedido_use_case import CrearPedidoUseCase
from src.application.use_cases.ver_pedidos_use_case import VerPedidosUseCase
from src.infraestructure.adapters.console_ui import PedidoController

def main():
    repository = InMemoryPedidoRepository()

    consultar_menu_uc = ConsultarMenuUseCase(repository)
    registrar_cliente_uc = RegistrarClienteUseCase(repository)
    crear_pedido_uc = CrearPedidoUseCase(repository)
    ver_pedidos_uc = VerPedidosUseCase(repository)

    controller = PedidoController(
        consultar_menu_uc=consultar_menu_uc,
        registrar_cliente_uc=registrar_cliente_uc,
        crear_pedido_uc=crear_pedido_uc,
        ver_pedidos_uc=ver_pedidos_uc
    )

    controller.iniciar()

if __name__ == "__main__":
    main()