from src.application.use_cases.consultar_menu_use_case import ConsultarMenuUseCase
from src.application.use_cases.registrar_cliente_use_case import RegistrarClienteUseCase
from src.application.use_cases.crear_pedido_use_case import CrearPedidoUseCase
from src.application.use_cases.ver_pedidos_use_case import VerPedidosUseCase
from src.domain.facturacion.factura import Factura

class PedidoController:

    def __init__(
        self,
        consultar_menu_uc: ConsultarMenuUseCase,
        registrar_cliente_uc: RegistrarClienteUseCase,
        crear_pedido_uc: CrearPedidoUseCase,
        ver_pedidos_uc: VerPedidosUseCase
    ):
        self.consultar_menu_uc = consultar_menu_uc
        self.registrar_cliente_uc = registrar_cliente_uc
        self.crear_pedido_uc = crear_pedido_uc
        self.ver_pedidos_uc = ver_pedidos_uc

    def iniciar(self):
        while True:
            print("\n====================================")
            print(" SISTEMA DE PEDIDOS DE COMIDA ")
            print("====================================")
            print("1. Ver Menú")
            print("2. Registrar Cliente")
            print("3. Crear Pedido")
            print("4. Ver Pedidos")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                productos = self.consultar_menu_uc.ejecutar()
                print("\n--- MENÚ DISPONIBLE ---")
                for producto in productos:
                    print(
                        f"ID: {producto.id} | "
                        f"{producto.nombre} | "
                        f"Precio: ${producto.precio:.2f} | "
                        f"Stock: {producto.stock}"
                    )

            elif opcion == "2":
                print("\n--- REGISTRAR CLIENTE ---")
                cedula = input("Cédula: ")
                nombre = input("Nombre: ")
                categoria = input("Categoría (Regular/Frecuente): ")

                mensaje = self.registrar_cliente_uc.ejecutar(cedula, nombre, categoria)
                print(mensaje)

            elif opcion == "3":
                print("\n--- NUEVO PEDIDO ---")
                cedula = input("Ingrese la cédula del cliente: ")
                productos_solicitados = []

                while True:
                    print("\n--- PRODUCTOS DISPONIBLES ---")
                    productos = self.consultar_menu_uc.ejecutar()
                    for producto in productos:
                        print(f"{producto.id} - {producto.nombre} (${producto.precio:.2f}) Stock: {producto.stock}")

                    opcion_p = input("ID del producto (f para finalizar): ")
                    if opcion_p.lower() == "f":
                        break

                    try:
                        producto_id = int(opcion_p)
                        cantidad = int(input("Cantidad: "))
                    except ValueError:
                        print("Debe ingresar valores numéricos válidos.")
                        continue

                    productos_solicitados.append({"producto_id": producto_id, "cantidad": cantidad})

                try:
                    pedido = self.crear_pedido_uc.ejecutar(cedula, productos_solicitados)
                    if pedido is None:
                        print("No fue posible crear el pedido. Verifique los datos.")
                        continue

                    factura = Factura(pedido)
                    print("\n====================================")
                    print(" FACTURA DEL PEDIDO ")
                    print("====================================")
                    print(factura.generar_resumen())
                    print("------------------------------------")
                    for linea in pedido.lineas:
                        print(f"{linea.cantidad}x {linea.producto.nombre} - ${linea.subtotal:.2f}")
                    print("====================================")
                except ValueError as e:
                    print(f"Error al crear pedido: {e}")

            elif opcion == "4":
                pedidos = self.ver_pedidos_uc.ejecutar()
                print("\n--- HISTORIAL DE PEDIDOS ---")
                if len(pedidos) == 0:
                    print("No existen pedidos registrados.")

                for p in pedidos:
                    print(f"Pedido #{p.id} | Cliente: {p.cliente_nombre} | Total: ${p.calcular_total():.2f}")

            elif opcion == "5":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida.")