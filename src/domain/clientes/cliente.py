from dataclasses import dataclass

@dataclass
class Cliente:
    cedula: str
    nombre: str
    categoria: str

    def es_frecuente(self) -> bool:
        return self.categoria.upper() == "FRECUENTE"