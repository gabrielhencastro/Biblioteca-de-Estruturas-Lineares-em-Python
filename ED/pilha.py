from ED.node import Node

class Pilha():
    
    def __init__(self):
        self.topo = None

    def esta_vazia(self):
        return not self.topo

    def push(self, dado):
        novo = Node(dado)
        novo.prox = self.topo
        self.topo = novo

    def pop(self):
        if not self.esta_vazia():
            aux = self.topo
            self.topo = self.topo.prox
            dado = aux.item
            del aux
            return dado

    def top(self):
        if not self.esta_vazia():
            return self.topo.item

    def destruir(self):
        while not self.esta_vazia():
            self.pop()

    def imprimir(self):
        aux = Pilha()
        while not self.esta_vazia():
            print(self.top())
            aux.push(self.pop())

        while not aux.esta_vazia():
            self.push(aux.pop())

    def buscar(self, info):
        elementos = []
        encontrado = False
        while not self.esta_vazia():
            elementos.append(self.pop())
        if info in elementos:
            encontrado = True
        for x in reversed(elementos):
            self.push(x)
        return encontrado

    def editar(self, antigo, novo):
        elementos = []
        encontrado = False
        while not self.esta_vazia():
            elementos.append(self.pop())
        for i in range(len(elementos)):
            if elementos[i] == antigo and not encontrado:
                elementos[i] = novo
                encontrado = True
        for x in reversed(elementos):
            self.push(x)
        return encontrado

    def remover(self, info):
        elementos = []
        encontrado = False
        while not self.esta_vazia():
            elementos.append(self.pop())
        novos_elementos = []
        for x in elementos:
            if x == info and not encontrado:
                encontrado = True
            else:
                novos_elementos.append(x)
        for x in reversed(novos_elementos):
            self.push(x)
        return encontrado

    def remover_repetidos(self):
        elementos = []
        while not self.esta_vazia():
            elementos.append(self.pop())
        vistos = set()
        unicos = []
        for x in elementos:
            if x not in vistos:
                vistos.add(x)
                unicos.append(x)
        for x in reversed(unicos):
            self.push(x)