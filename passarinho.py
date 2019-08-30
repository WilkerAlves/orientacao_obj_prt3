class Passaro:
    def __init__(self, nome):
        self.nome = nome


class CanarinhoPistola(Passaro):
    def __init__(self, nome, camisa):
        super().__init__(nome)
        self.camisa = camisa

    def __str__(self):
        return f'CanarinhoPistola(nome="{self.nome}", camisa="{self.camisa}")'
