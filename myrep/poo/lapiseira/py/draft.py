class Grafite:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.__thickness = thickness
        self.__hardness = hardness
        self.__size = size
    def get_thickness(self):
        return self.__thickness
    def get_hardness(self):
        return self.__hardness
    def get_size(self):
        return self.__size
    def set_thickness(self, calibre: float):
        self.__thickness = calibre
    def set_hardness(self, dureza: str):
        self.__hardness = dureza 
    def set_size(self, tamanho: int):
        self.__size = tamanho
    def usagePerSheet(self):
        if self.__hardness == "HB":
            return 1
        if self.__hardness == "2B":
            return 2
        if self.__hardness == "4B":
            return 4
        if self.__hardness == "6B":
            return 6
    def __str__(self):
        return f"[{self.get_thickness()}:{self.get_hardness()}:{self.get_size()}]"

class Lapiseira:
     def __init__(self, thickness: float = 0.0):
        self.thickness = thickness
        self.tambor: list[Grafite] = []
        self.bico: Grafite | None = None

     def inserir(self, bico: Grafite) -> bool:
        
        if self.thickness != bico.get_thickness():
            print ("fail: calibre incompatível")
            return False 
        self.tambor.append(bico)
        return True
     
     def puxar(self):
         
        if self.bico is not None:
            print("fail: ja existe grafite no bico")
            return
        if not self.tambor:
            print("fail: tambor vazio")
            return
        self.bico = self.tambor.pop(0)
        
             

     def remover(self) -> Grafite | None: 
        if self.tambor is not None:
            return None
        aux = self.bico
        self.bico = None
        return aux
         
     def escrever(self):
        if self.bico == None:
            print("fail: nao existe grafite")
            return
        if self.bico.get_size() <= 10:
            print("fail: tamanho insuficiente")
            return

        gasto = self.bico.usagePerSheet()
        novo_tamanho = self.bico.get_size() - gasto

        if self.bico.get_size() - self.bico.usagePerSheet() < 10:
            print ("fail: folha incompleta")
            self.bico.set_size(10)
            return

        self.bico.set_size(novo_tamanho)

     def __str__(self):
        tambor = "".join(str(x) for x in self.tambor)
        bico = str(self.bico) if self.bico else "[]"
        return f"calibre: {self.thickness}, bico: {bico}, tambor: <{tambor}>"

def main ():
     lapiseira = Lapiseira()

     while True:
        line = input()
        print("$"+line)
        args:list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(lapiseira)
        elif args[0] == "init":
            lapiseira = Lapiseira(float(args[1]))
        elif args[0] == "insert":
            thickness = float(args[1])
            hardness = str(args[2])
            size = int(args[3])
            grafite = Grafite(thickness,hardness,size)
            lapiseira.inserir(grafite) 
        elif args[0] == "pull":
            lapiseira.puxar()   
        elif args[0] == "remove":
            grafite = lapiseira.remover()
        elif args[0] == "write":
            lapiseira.escrever()

if __name__ == "__main__":    
    main()