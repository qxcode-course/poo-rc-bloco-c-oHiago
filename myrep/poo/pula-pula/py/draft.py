#Inserir crianças na fila de espera do pula pula
#Mover a primeira criança da fila de espera do pula pula para dentro do pula pula.
#Mover a primeira criança que entrou no pula pula para o final da fila de espera.


class Criança:
    def __init__(self,nome:str,idade:int):
        self.__nome = nome
        self.__idade = idade
    def getNome(self):
        return self.__nome
    def getIdade(self):
        return self.__idade
    def __str__(self):
        return f"{self.__nome}:{self.__idade}"

class Pulapula:
    def __init__(self):
        self.espera: list[Criança] = []
        self.pulapula: list[Criança | None] = []

    def fila(self,criança: Criança):
        self.espera.insert(0,criança)

    def entrar(self):
        if not self.espera:
            print("fail: ninguem na fila")
            return
        else:
            criança = self.espera.pop()
            self.pulapula.insert(0,criança) 

    def sair(self):
        if not self.pulapula:
            return 
        criança = self.pulapula.pop()
        self.espera.insert(0,criança)

    def remover(self, nome: str):
        for i, criança in enumerate (self.espera):
            if criança.getNome() == nome:
                del self.espera[i]
                return
           
        for i, criança in enumerate (self.pulapula):
            if criança.getNome() == nome:
                del self.pulapula[i]
                return
            
        print (f"fail: {nome} nao esta no pula-pula")

    def __str__(self):
        espera = ", ".join(str(x) for x in self.espera)
        pulapula = ", ".join(str(x) for x in self.pulapula)
        return f"[{espera}] => [{pulapula}]"

def main():
    pula_pula = Pulapula ()

    while True:
        line = input()
        print("$"+line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(pula_pula)
        elif args[0] == "arrive":
            nome = args[1]
            idade = int(args[2])
            pula_pula.fila(Criança(nome,idade))
        elif args[0] == "enter":
            pula_pula.entrar()
        elif args[0] == "leave":
            pula_pula.sair()
        elif args[0] == "remove":
            nome = args[1]
            pula_pula.remover(nome)
        else:
            print("fail: comando não encontrado")

if __name__ == "__main__":
    main()