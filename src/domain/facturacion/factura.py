from src.domain.pedidos.pedido import Pedido

class Factura:

    def __init__(self, pedido: Pedido):
        self.pedido_id = pedido.id
        self.cliente_cedula = pedido.cliente_cedula
        self.cliente_nombre = pedido.cliente_nombre

        self.subtotal = pedido.calcular_subtotal()
        self.descuento = pedido.calcular_descuento()
        self.total = pedido.calcular_total()

    def generar_resumen(self) -> str:
        return (
            f"Factura del Pedido #{self.pedido_id}\n"
            f"Cliente: {self.cliente_nombre}\n"
            f"Cédula: {self.cliente_cedula}\n"
            f"Subtotal: ${self.subtotal:.2f}\n"
            f"Descuento: ${self.descuento:.2f}\n"
            f"Total: ${self.total:.2f}"
        )
    