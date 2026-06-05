class PedidoController:

    def __init__(self, service):
        self.service = service

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
                productos = self.service.ver_menu()
                print("\n--- MENÚ DISPONIBLE ---")
                for producto in productos:
                    print(
                        f"ID: {producto['id']} | "
                        f"{producto['nombre']} | "
                        f"Precio: ${producto['precio']:.2f} | "
                        f"Stock: {producto['stock']}"
                    )

            elif opcion == "2":
                print("\n--- REGISTRAR CLIENTE ---")
                cedula = input("Cédula: ")
                nombre = input("Nombre: ")
                categoria = input("Categoría (Regular/Frecuente): ")

                mensaje = self.service.registrar_cliente(
                    cedula,
                    nombre,
                    categoria
                )
                print(mensaje)

            elif opcion == "3":
                print("\n--- NUEVO PEDIDO ---")
                cedula = input("Ingrese la cédula del cliente: ")
                pedido = self.service.crear_pedido(cedula)

                if pedido is None:
                    print("No fue posible crear el pedido.")
                    continue

                print("\n====================================")
                print(" FACTURA DEL PEDIDO ")
                print("====================================")
                print(f"Pedido N°: {pedido.get('id', 'N/A')}")
                print(f"Cliente: {pedido['cliente']}")
                print("------------------------------------")

                for item in pedido["detalle"]:
                    print(
                        f"{item['cantidad']}x "
                        f"{item['producto']} "
                        f"- ${item['total']:.2f}"
                    )

                print("------------------------------------")
                print(f"Subtotal: ${pedido['subtotal']:.2f}")
                print(f"Descuento: ${pedido['descuento']:.2f}")
                print(f"Total: ${pedido['total']:.2f}")
                print("====================================")

            elif opcion == "4":
                pedidos = self.service.ver_pedidos()
                print("\n--- HISTORIAL DE PEDIDOS ---")

                if len(pedidos) == 0:
                    print("No existen pedidos registrados.")

                for pedido_historial in pedidos:
                    print(
                        f"Pedido #{pedido_historial['id']} | "
                        f"Cliente: {pedido_historial['cliente']} | "
                        f"Total: ${pedido_historial['total']:.2f}"
                    )

            elif opcion == "5":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")