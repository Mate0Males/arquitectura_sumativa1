# ============================
# SISTEMA DE PEDIDOS DE COMIDA
# VERSION CODIGO ESPAGUETI
# ============================

productos = []
pedidos = []

id_producto = 1
id_pedido = 1

while True:

    print("\n==============================")
    print(" SISTEMA DE PEDIDOS DE COMIDA ")
    print("==============================")
    print("1. Registrar producto")
    print("2. Ver productos")
    print("3. Crear pedido")
    print("4. Ver pedidos")
    print("5. Entregar pedido")
    print("6. Salir")

    opcion = input("\nSeleccione una opción: ")

    # REGISTRAR PRODUCTO
    if opcion == "1":

        nombre = input("Ingrese el nombre del producto: ")

        try:
            precio = float(input("Ingrese el precio: "))
        except:
            print("Precio inválido")
            continue

        producto = {
            "id": id_producto,
            "nombre": nombre,
            "precio": precio
        }

        productos.append(producto)

        print("Producto registrado correctamente.")

        id_producto += 1

    # VER PRODUCTOS
    elif opcion == "2":

        if len(productos) == 0:
            print("No existen productos registrados.")
        else:
            print("\n--- LISTA DE PRODUCTOS ---")

            for producto in productos:
                print(
                    f"ID: {producto['id']} | "
                    f"Nombre: {producto['nombre']} | "
                    f"Precio: ${producto['precio']:.2f}"
                )

    # CREAR PEDIDO
    elif opcion == "3":

        if len(productos) == 0:
            print("Debe registrar productos primero.")
            continue

        print("\n--- PRODUCTOS DISPONIBLES ---")

        for producto in productos:
            print(
                f"{producto['id']} - "
                f"{producto['nombre']} "
                f"(${producto['precio']:.2f})"
            )

        try:
            id_seleccionado = int(
                input("Ingrese el ID del producto: ")
            )
        except:
            print("ID inválido")
            continue

        producto_encontrado = None

        for producto in productos:
            if producto["id"] == id_seleccionado:
                producto_encontrado = producto

        if producto_encontrado is None:
            print("Producto no encontrado.")
        else:

            pedido = {
                "id": id_pedido,
                "producto": producto_encontrado["nombre"],
                "precio": producto_encontrado["precio"],
                "estado": "Pendiente"
            }

            pedidos.append(pedido)

            print("Pedido creado correctamente.")
            print(f"Número de pedido: {id_pedido}")

            id_pedido += 1

    # VER PEDIDOS
    elif opcion == "4":

        if len(pedidos) == 0:
            print("No existen pedidos registrados.")
        else:

            print("\n--- LISTA DE PEDIDOS ---")

            for pedido in pedidos:

                print(
                    f"Pedido #{pedido['id']} | "
                    f"Producto: {pedido['producto']} | "
                    f"Precio: ${pedido['precio']:.2f} | "
                    f"Estado: {pedido['estado']}"
                )

    # ENTREGAR PEDIDO
    elif opcion == "5":

        if len(pedidos) == 0:
            print("No existen pedidos.")
            continue

        try:
            id_buscar = int(
                input("Ingrese el ID del pedido: ")
            )
        except:
            print("ID inválido")
            continue

        encontrado = False

        for pedido in pedidos:

            if pedido["id"] == id_buscar:

                encontrado = True

                if pedido["estado"] == "Entregado":
                    print("El pedido ya fue entregado.")
                else:
                    pedido["estado"] = "Entregado"
                    print("Pedido entregado correctamente.")

        if not encontrado:
            print("Pedido no encontrado.")

    # SALIR
    elif opcion == "6":

        print("Saliendo del sistema...")
        break

    else:

        print("Opción inválida.")