class Forno:
    def __init__(self):
        self.pizzas = []
        self.lenha = None

    def assar(self, pizza):
        if not self.lenha:
            print('não ha lenha')


class Pizzaolo:
    def __init__(self):
        self._forno = Forno()

    def preparar_pizza(self, pizza):
        self._forno.pizzas(pizza)


class Pizza:
    def __init__(self):
        self._pizzaolo = Pizzaolo()

    def pedido(self, pizza):
        self._pizzaolo.preparar_pizza(pizza)
