PRODUCTOS = [
    {
        "id": 1,
        "nombre": "Hamburguesa Clásica",
        "precio": 4.50,
        "stock": 15
    },
    {
        "id": 2,
        "nombre": "Pizza Personal",
        "precio": 6.75,
        "stock": 10
    },
    {
        "id": 3,
        "nombre": "Hot Dog Especial",
        "precio": 3.25,
        "stock": 20
    }
]

CLIENTES = [
    {
        "cedula": "1101234567",
        "nombre": "Carlos Mendoza",
        "categoria": "Regular"
    },
    {
        "cedula": "1107654321",
        "nombre": "Ana Torres",
        "categoria": "Frecuente"
    }
]

PEDIDOS = []

class PedidoRepository:

    def obtener_productos(self):
        return PRODUCTOS

    def buscar_producto_por_id(self, id_producto):
        for producto in PRODUCTOS:
            if producto["id"] == id_producto:
                return producto
        return None

    def actualizar_stock(self, id_producto, cantidad):
        producto = self.buscar_producto_por_id(id_producto)
        if producto:
            producto["stock"] -= cantidad
            return True
        return False

    def obtener_clientes(self):
        return CLIENTES

    def buscar_cliente_por_cedula(self, cedula):
        for cliente in CLIENTES:
            if cliente["cedula"] == cedula:
                return cliente
        return None

    def guardar_cliente(self, cliente):
        CLIENTES.append(cliente)
        return cliente

    def obtener_pedidos(self):
        return PEDIDOS

    def guardar_pedido(self, pedido):
        pedido["id"] = len(PEDIDOS) + 1
        PEDIDOS.append(pedido)
        return pedido