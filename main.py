PRODUCTOS = [
    {"id": 1, "nombre": "Hamburguesa Clásica", "precio": 4.50, "stock": 15},
    {"id": 2, "nombre": "Pizza Personal", "precio": 6.75, "stock": 10},
    {"id": 3, "nombre": "Hot Dog Especial", "precio": 3.25, "stock": 20}
]

CLIENTES = [
    {"cedula": "1101234567", "nombre": "Carlos Mendoza", "categoria": "Regular"},
    {"cedula": "1107654321", "nombre": "Ana Torres", "categoria": "Frecuente"}
]

PEDIDOS = []

def ejecutar_sistema():
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
            print("\n--- MENÚ DISPONIBLE ---")
            for producto in PRODUCTOS:
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

            CLIENTES.append({
                "cedula": cedula,
                "nombre": nombre,
                "categoria": categoria
            })
            print("Cliente registrado correctamente.")

        elif opcion == "3":
            print("\n--- NUEVO PEDIDO ---")
            cedula_cliente = input("Ingrese la cédula del cliente: ")
            cliente = None

            for c in CLIENTES:
                if c["cedula"] == cedula_cliente:
                    cliente = c
                    break

            if cliente is None:
                print("Cliente no registrado.")
                continue

            detalle_pedido = []
            subtotal = 0

            while True:
                id_producto = input("ID del producto (f para finalizar): ")

                if id_producto.lower() == "f":
                    break

                producto = None
                for p in PRODUCTOS:
                    if str(p["id"]) == id_producto:
                        producto = p
                        break

                if producto is None:
                    print("Producto no encontrado.")
                    continue

                cantidad = int(input(f"Cantidad de {producto['nombre']}: "))

                if cantidad > producto["stock"]:
                    print(f"Stock insuficiente. Disponible: {producto['stock']}")
                    continue

                producto["stock"] -= cantidad
                total_item = producto["precio"] * cantidad
                subtotal += total_item

                detalle_pedido.append({
                    "producto": producto["nombre"],
                    "cantidad": cantidad,
                    "precio": producto["precio"],
                    "total": total_item
                })
                print("Producto agregado al pedido.")

            if len(detalle_pedido) == 0:
                print("Pedido cancelado.")
                continue

            descuento = 0
            if cliente["categoria"].upper() == "FRECUENTE":
                descuento = subtotal * 0.05

            total_pagar = subtotal - descuento

            pedido = {
                "id": len(PEDIDOS) + 1,
                "cliente": cliente["nombre"],
                "detalle": detalle_pedido,
                "subtotal": subtotal,
                "descuento": descuento,
                "total": total_pagar
            }
            PEDIDOS.append(pedido)

            print("\n====================================")
            print(" FACTURA DEL PEDIDO ")
            print("====================================")
            print(f"Pedido N°: {pedido['id']}")
            print(f"Cliente: {pedido['cliente']}")
            print("------------------------------------")
            for item in pedido["detalle"]:
                print(f"{item['cantidad']}x {item['producto']} - ${item['total']:.2f}")
            print("------------------------------------")
            print(f"Subtotal: ${pedido['subtotal']:.2f}")
            print(f"Descuento: ${pedido['descuento']:.2f}")
            print(f"Total: ${pedido['total']:.2f}")
            print("====================================")

        elif opcion == "4":
            print("\n--- HISTORIAL DE PEDIDOS ---")
            if len(PEDIDOS) == 0:
                print("No existen pedidos registrados.")
            for pedido in PEDIDOS:
                print(
                    f"Pedido #{pedido['id']} | "
                    f"Cliente: {pedido['cliente']} | "
                    f"Total: ${pedido['total']:.2f}"
                )

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    ejecutar_sistema()