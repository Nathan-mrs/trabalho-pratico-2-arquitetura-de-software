"""Trabalho Prático 02 — composição entre contrato e condutor."""
from datetime import date
from decimal import Decimal


class Condutor:
    def __init__(self, identificador, nome, numero_cnh):
        self.identificador = identificador
        self.nome = nome
        self.numero_cnh = numero_cnh

    def atualizar_cnh(self, numero_cnh):
        self.numero_cnh = numero_cnh

    def exibir_dados(self):
        return f"{self.nome} | CNH: {self.numero_cnh}"


class ContratoLocacao:
    def __init__(self, cliente, veiculo, inicio, termino,
                 valor_total, nome_condutor, numero_cnh):
        if termino <= inicio:
            raise ValueError("O término deve ser posterior ao início.")
        self.cliente = cliente
        self.veiculo = veiculo
        self.data_inicio = inicio
        self.data_termino_prevista = termino
        self.valor_total = Decimal(str(valor_total))
        if self.valor_total < 0:
            raise ValueError("O valor não pode ser negativo.")
        self.status = "ativo"
        # Composição: o contrato cria seu próprio registro de condutor.
        self.condutor = Condutor(1, nome_condutor, numero_cnh)

    def finalizar_contrato(self):
        self.status = "finalizado"

    def cancelar_contrato(self):
        self.status = "cancelado"

    def exibir_dados(self):
        valor = f"{self.valor_total:.2f}".replace(".", ",")
        return (f"Cliente: {self.cliente} | Veículo: {self.veiculo}\n"
                f"Valor: R$ {valor} | Status: {self.status}\n"
                f"Condutor: {self.condutor.exibir_dados()}")


if __name__ == "__main__":
    contrato = ContratoLocacao(
        "CLI001", "ABC1D23", date(2026, 10, 1), date(2026, 10, 5),
        "600.00", "João da Silva", "12345678900"
    )
    print(contrato.exibir_dados())
    contrato.finalizar_contrato()
    print(f"Após finalizar: {contrato.status}")
