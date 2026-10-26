from ED.fila import Fila
from ED.lista import Lista
from ED.node import Node
from ED.pilha import Pilha

print('---- Exercicio 1 ----')
fila = Fila()
fila.enqueue(10)
fila.enqueue(5)
fila.enqueue(20)
fila.enqueue(15)

print(f'Tamanho: {fila.len()}')
print(f'Mínimo: {fila.min()}')
print(f'Máximo: {fila.max()}')
print(f'Soma: {fila.sum()}')
print(f'Média: {fila.avg()}')

print('---- Exercicio 2 ----')
fila1 = Fila()
fila1.enqueue(1)
fila1.enqueue(2)
fila1.enqueue(3)

fila2 = Fila()
fila2.enqueue(4)
fila2.enqueue(5)

print("Fila 1 original:")
fila1.imprimir()

fila1.append(fila2)
print("Fila 1 apos append:")
fila1.imprimir()

fila1.reverse()
print("Fila 1 apos reverse:")
fila1.imprimir()

print('---- Exercicio 3 ----')
pilha = Pilha()
pilha.push(10)
pilha.push(20)
pilha.push(10)
pilha.push(30)
pilha.push(20)

print("Pilha original:")
pilha.imprimir()

print("Buscar 30:", pilha.buscar(30))
print("Buscar 50:", pilha.buscar(50))

pilha.editar(30, 99)
print("Apos editar 30 para 99:")
pilha.imprimir()

pilha.remover(10)
print("Apos remover o primeiro 10:")
pilha.imprimir()

pilha.remover_repetidos()
print("Apos remover repetidos:")
pilha.imprimir()

print('---- Exercicio 4 ----')
fila = Fila()
fila.enqueue(10)
fila.enqueue(20)
fila.enqueue(10)
fila.enqueue(30)
fila.enqueue(20)

print("Fila original:")
fila.imprimir_fila()

print("Buscar 30:", fila.buscar(30))
print("Buscar 50:", fila.buscar(50))

fila.editar((30, 99))
print("Apos editar 30 para 99:")
fila.imprimir_fila()

fila.remover(10)
print("Apos remover o primeiro 10:")
fila.imprimir_fila()

fila.remover_repetidos()
print("Apos remover repetidos:")
fila.imprimir_fila()