class Client:
    def __init__(self, id: str, phone: int):
        self.id = id
        self.phone = phone

    def __str__(self):
        return f"{self.id},{self.phone}"
    
class Theater:
    def __init__(self,qtd:int):
        self.cadeiras: list[Client | None] = [] * qtd

    def __str__(self):
        cadeiras = ", ".join([str(x)] if x else "-" for x in self.cadeiras)
        return f"[{cadeiras}]"
    
def main():
    
    cinema = Theater (0)

    while True:
        line = input()
        print("$" + line)
        args:list[str] = line.split(" ")

        if args[0] == "end":
            break
        if args[0] == "show":
            print(cinema)
        if args[0] == "init":
            cinema = Theater (int(args[1]))

if __name__ == "__main__":
    main()