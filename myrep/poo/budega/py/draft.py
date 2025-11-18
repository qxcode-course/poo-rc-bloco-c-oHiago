class Pessoa:
    def __init__ (self, nome: str):
        self.__nome = nome 
    def getNome (self):
        return self.__nome 
    def __str__(self):
        return f"{self.__nome}"
    
class Mercantil:
    def __init__(self, n_caixas: int):
        self.espera: list[Pessoa] = []
        self.caixas: list[Pessoa | None ] = []
        for _ in range (n_caixas):
            self.caixas.append(None)

    def chegar(self, pessoa: Pessoa):
        self.espera.append(pessoa)

    def chamar(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("fail: index invalido")
            return
        if self.caixas[index] is not None:
            print("fail: caixa ocupado")
            return
        if len(self.espera) == 0:
            print("fail: sem clientes")
            return
        
        self.caixas[index] = self.espera.pop(0)
        

    def finalizar(self, index: int) -> Pessoa | None:
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return None
        if self.caixas[index] is None:
            print("fail: caixa vazio")
            return None
        
        pessoa = self.caixas[index]
        self.caixas[index] = None
        return pessoa
    
    def __str__(self):
        caixas = ", ".join([str(x)  if x else "-----" for x in self.caixas])
        espera = ", ".join([str(x) for x in self.espera])
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"

def main():
    mercantil: Mercantil | None = None

    while True: 
        line = input() 
        print("$" + line) 
        args = line.split() 
        
        if args[0] == "end": 
            break 
        elif args[0] =="show": 
            print(mercantil) 
        elif args[0] =="init": 
            n_caixas = int(args[1]) 
            mercantil = Mercantil(n_caixas)
        elif args[0] == "arrive":
            nome = args[1]
            mercantil.chegar(Pessoa(nome))
        elif args[0] == "call":
            index = int(args[1])
            mercantil.chamar(index)
        elif args[0] == "finish":
            index = int(args[1])
            mercantil.finalizar(index)
        else:
            print("fail: comando não encontrado")
if __name__ == "__main__":
    main()       
