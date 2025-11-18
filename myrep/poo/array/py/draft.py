import random

class Foo:
    def __init__(self, x:int):
        self.x = x
    def __str__(self):
        return f"Foo:({self.x})"
class Listas:
    def __init__(self):
        self.lista_vazia: list[int] = [] #Criar um array vazio
        self.lista_nums: list[int] = [1,2,3,4,5] #Criar um array preenchido (tipo primitivo)
        self.lista_foo: list[Foo] = [Foo(1), Foo(2)]#Criar um array preenchido (classe Foo)
        for f in self.lista_foo:
            print(f)
       

def main():
    lista = Listas()
    
    print(lista.lista_vazia)
    #Adicionar e remover elementos ao final
    lista.lista_nums.append(10) 
    print(lista.lista_nums) 
    lista.lista_nums.pop() #remove elemento
    print(lista.lista_nums) 
    #Adicionar e remover elementos no inicio
    lista.lista_nums.insert(0,5) 
    print(lista.lista_nums)
    lista.lista_nums.pop(0)
    print(lista.lista_nums)
    #Adicionar e remover elementos em uma posição específica
    lista.lista_nums.insert(4,10) 
    print(lista.lista_nums)
    lista.lista_nums.pop(4)
    print(lista.lista_nums)
   # Fazer impressão formatada utilizando o método join
    separador = '-'
    frase = separador.join(map(str, lista.lista_nums))
    print(frase)
#Obter tamanho do array
    print(lista.lista_nums)
    tamanho = len(lista.lista_nums) #Obter o tamanho do array
    print(tamanho)
    # Criar um array com elementos em sequência de zero a n
    sequencia = list(range(0,5))
    print(sequencia)
    #Criar um array com valores aleatórios
    aleatorio = [random.randint(1,500) for _ in range(5)]
    print(aleatorio)
    #Acessar elementos por índice
    numero_1 = lista.lista_nums[0]
    print(numero_1)
    numero_2 = lista.lista_nums[1]
    print(numero_2)
    ultimo_numero = lista.lista_nums[-1]
    print(ultimo_numero)
    #Percorrer os elementos utilizando for-range
    for i in range(5):
        print(i)
    #Percorrer os elementos utilizando for indexado
    lista_cor = ['azul', 'amarelo', 'verde']
    tamanho_lista = len(lista_cor)

    for y in range(tamanho_lista):
        cor = lista_cor[y]
        print({y},{cor})

    #Procurar um elemento X usando laço


main()
