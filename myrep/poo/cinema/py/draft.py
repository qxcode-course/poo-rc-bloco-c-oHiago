class Client:
    def __init__(self, id: str, phone: int):
        self.id = id
        self.phone = phone

    def __str__(self):
        return f"{self.id}:{self.phone}"
    
class Theater:
    def __init__(self,n_cadeiras:int):
        self.cadeiras: list[Client | None] = []

        for _ in range (n_cadeiras):
            self.cadeiras.append(None)
    
    def reserve (self, id: str, phone: int, index: int):
        if index < 0 or index >= len(self.cadeiras):
            print("fail: cadeira nao existe")
            return
        if self.cadeiras[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return
        for cliente in self.cadeiras:
            if cliente is not None and cliente.id == id:
                print("fail: cliente ja esta no cinema")
                return
        
        self.cadeiras[index] = Client(id,phone)

    def __str__(self):
        cadeiras = " ".join(str(x) if x else "-" for x in self.cadeiras)
        return f"[{cadeiras}]"
    
def main():
    
    cinema = Theater (0)

    while True:
        line = input()
        print("$" + line)
        args:list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(cinema)
        elif args[0] == "init":
            n_cadeiras = int(args[1])
            cinema = Theater (n_cadeiras)
        elif args[0] == "reserve":
            id = args[1]
            phone = int(args[2])
            index = int(args[3])
            cinema.reserve(id, phone, index)

if __name__ == "__main__":
    main()