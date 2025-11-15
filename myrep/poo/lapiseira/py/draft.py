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
        self.tip: Grafite | None = None
        self.thickness = thickness
     def inserir(self, tip: Grafite) -> bool:
        if self.tip !=  None:
            print ("fail: ja existe grafite")
            return False
        if self.thickness != tip.get_thickness():
            print ("fail: calibre incompativel")
            return False 
        self.tip = tip
        return True

     def remover(self) -> Grafite | None: 
        if self.tip == None:
            print ("fail: nao existe grafite")
            return None
        aux: Grafite = self.tip
        self.tip = None
        return aux
     def escrever(self):
        if self.tip == None:
            print("fail: nao existe grafite")
            return
        if self.tip.get_size() <= 10:
            print("fail: tamanho insuficiente")
            return

        gasto = self.tip.usagePerSheet()
        novo_tamanho = self.tip.get_size() - gasto

        if self.tip.get_size() - self.tip.usagePerSheet() < 10:
            print ("fail: folha incompleta")
            self.tip.set_size(10)
            return

        self.tip.set_size(novo_tamanho)

     def __str__(self):
        return f"calibre: {self.thickness}, grafite: {self.tip if self.tip != None else "null"}"

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
        elif args[0] == "remove":
            grafite = lapiseira.remover()
        elif args[0] == "write":
            lapiseira.escrever()
            
if __name__ == "__main__":    
    main()