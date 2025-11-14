#Inserir crianças na fila de espera do pula pula
#Mover a primeira criança da fila de espera do pula pula para dentro do pula pula.
#Mover a primeira criança que entrou no pula pula para o final da fila de espera.


class Pessoa:
    def __init__(self,nome:str):
        self.__nome = nome
    def getNome(self):
        return self.__nome
    def __str__(self):
        return f"{self.__nome}"

class Pulapula:
    def __init__(self):
        self.espera: list[Pessoa] = []
        self.pulapula: list[Pessoa | None] = []

    def fila(self,pessoa: Pessoa):
        self.espera.append(pessoa)

    def entrar(self):
        if self.espera is None:
            print("fail: ninguem na fila")
            return
        else:
            self.espera.pop(0)

    def sair(self):
        if self.espera is None:
            print("fail: ninguem na fila")
            return
        else:
            self.pulapula.pop(0)

def main():
    pula_pula: Pulapula | None = None

    while True:
        line = input()
        print("$"+line)
        args = line.split()

        if args[0] == "end":
            break
        if args[0] == "show":
            print("pula_pula")
        if args[0] == "arrive":
            nome = args[1]
            pula_pula.fila(Pessoa(nome))

if __name__ == "__main__":
    main()