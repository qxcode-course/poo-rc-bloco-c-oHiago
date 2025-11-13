class Foo:
    def __init__(self, x:int):
        self.x = x
    def __str__(self):
        return f"Foo:({self.x})"
class Listas:
    def __init__(self):
        self.lista_vazia: list[int] = [] 
        self.lista_nums: list[int] = [1,2,3,4,5] 
        self.lista_nums.append(7)
        self.lista_foo: list[Foo] = [] 
    
    y = list(range(4,10))
    print(y)

def main():
    lista = Listas()
    
    print(lista.lista_vazia)
    print(lista.lista_foo)
    lista.lista_nums.append(10)  
    lista.lista_nums.insert(0,0)  
    lista.lista_nums.remove(4) 
    lista.lista_nums.pop(1) 
    lista.lista_nums.pop(5)
    separador = '-'
    frase = separador.join(map(str, lista.lista_nums))
    print(frase)
    print(lista.lista_nums)
    tamanho = len(lista.lista_nums) 

    print(tamanho)

main()
