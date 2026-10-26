from ED.node import Node

class Fila():

    def __init__(self):
        self.inicio = None
        self.final = None

    def esta_vazia(self):
        return not self.inicio

    def enqueue(self, dado):
        novo = Node(dado)
        if not self.esta_vazia():
            self.final.prox = novo
            self.final = novo
        else:
            self.inicio = novo
            self.final = novo

    def dequeue(self):
        aux = self.inicio
        if not self.esta_vazia():
            if self.inicio != self.final:
                self.inicio = self.inicio.prox
            else:
                self.inicio = None
                self.final = None
            dado = aux.item
            del aux
            return dado

    def first(self):
        if not self.esta_vazia():
            return self.inicio.item

    def destruir(self):
        while not self.esta_vazia():
            self.dequeue()

    def imprimir(self):
        aux = Fila()
        while not self.esta_vazia():
            print(self.first())
            aux.enqueue(self.dequeue())

        while not aux.esta_vazia():
            self.enqueue(aux.dequeue())

    def imprimir_fila(self):
        self.imprimir()

    def len(self):
        contador = 0
        atual = self.inicio
        while atual is not None:
            contador += 1
            atual = atual.prox
        return contador

    def min(self):
        if self.esta_vazia():
            return None
        menor = self.inicio.item
        atual = self.inicio.prox
        while atual is not None:
            if atual.item < menor:
                menor = atual.item
            atual = atual.prox
        return menor

    def max(self):
        if self.esta_vazia():
            return None
        maior = self.inicio.item
        atual = self.inicio.prox
        while atual is not None:
            if atual.item > maior:
                maior = atual.item
            atual = atual.prox
        return maior

    def sum(self):
        soma = 0
        atual = self.inicio
        while atual is not None:
            soma += atual.item
            atual = atual.prox
        return soma

    def avg(self):
        quantidade = self.len()
        if quantidade == 0:
            return 0
        return self.sum() / quantidade

    def append(self, outra_lista):
        atual = outra_lista.inicio
        while atual is not None:
            self.enqueue(atual.item)
            atual = atual.prox

    def reverse(self):
        elementos = []
        while not self.esta_vazia():
            elementos.append(self.dequeue())
        for elemento in reversed(elementos):
            self.enqueue(elemento)

    def buscar(self, info):
        elementos = []
        encontrado = False
        while not self.esta_vazia():
            elementos.append(self.dequeue())
        if info in elementos:
            encontrado = True
        for x in elementos:
            self.enqueue(x)
        return encontrado

    def editar(self, info):
        antigo, novo = info
        elementos = []
        encontrado = False
        while not self.esta_vazia():
            elementos.append(self.dequeue())
        for i in range(len(elementos)):
            if elementos[i] == antigo and not encontrado:
                elementos[i] = novo
                encontrado = True
        for x in elementos:
            self.enqueue(x)
        return encontrado

    def remover(self, info):
        elementos = []
        encontrado = False
        while not self.esta_vazia():
            elementos.append(self.dequeue())
        novos_elementos = []
        for x in elementos:
            if x == info and not encontrado:
                encontrado = True
            else:
                novos_elementos.append(x)
        for x in novos_elementos:
            self.enqueue(x)
        return encontrado

    def remover_repetidos(self):
        elementos = []
        while not self.esta_vazia():
            elementos.append(self.dequeue())
        vistos = set()
        unicos = []
        for x in elementos:
            if x not in vistos:
                vistos.add(x)
                unicos.append(x)
        for x in unicos:
            self.enqueue(x)