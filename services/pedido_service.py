class PedidoService:

    def __init__(self, repository):
        self.repository = repository

    def ver_menu(self):
        return self.repository.obtener_productos()

    def registrar_cliente(self, cedula, nombre, categoria):
        cliente = self.repository.buscar_cliente_por_cedula(cedula)

        if cliente:
            return "El cliente ya existe."

        nuevo_cliente = {
            "cedula": cedula,
            "nombre": nombre,
            "categoria": categoria
        }

        self.repository.guardar_cliente(nuevo_cliente)
        return "Cliente registrado correctamente."

    def crear_pedido(self, cedula_cliente):
        cliente = self.repository.buscar_cliente_por_cedula(cedula_cliente)

        if cliente is None:
            print("Cliente no registrado.")
            return None

        detalle_pedido = []
        subtotal = 0

        while True:
            print("\n--- PRODUCTOS DISPONIBLES ---")
            productos = self.repository.obtener_productos()

            for producto in productos:
                print(
                    f"{producto['id']} - "
                    f"{producto['nombre']} "
                    f"(${producto['precio']:.2f}) "
                    f"Stock: {producto['stock']}"
                )

            opcion = input("ID del producto (f para finalizar): ")

            if opcion.lower() == "f":
                break

            try:
                producto_id = int(opcion)
            except ValueError:
                print("Debe ingresar un número válido.")
                continue

            producto = self.repository.buscar_producto_por_id(producto_id)

            if producto is None:
                print("Producto no encontrado.")
                continue

            try:
                cantidad = int(input("Cantidad: "))
            except ValueError:
                print("Debe ingresar una cantidad numérica.")
                continue

            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
                continue

            if cantidad > producto["stock"]:
                print(f"Stock insuficiente. Disponible: {producto['stock']}")
                continue

            self.repository.actualizar_stock(producto["id"], cantidad)
            total_item = producto["precio"] * cantidad
            subtotal += total_item

            detalle_pedido.append({
                "producto": producto["nombre"],
                "cantidad": cantidad,
                "precio": producto["precio"],
                "total": total_item
            })

        if len(detalle_pedido) == 0:
            return None

        descuento = 0
        if cliente["categoria"].upper() == "FRECUENTE":
            descuento = subtotal * 0.05

        total = subtotal - descuento

        pedido = {
            "cliente": cliente["nombre"],
            "detalle": detalle_pedido,
            "subtotal": subtotal,
            "descuento": descuento,
            "total": total
        }

        self.repository.guardar_pedido(pedido)
        return pedido

    def ver_pedidos(self):
        return self.repository.obtener_pedidos()