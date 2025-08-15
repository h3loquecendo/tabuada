numero = int(input("digite um numero: "))
i = int(input("digite onde a tabuada deve comecar: "))
f = int(input("digite ate onde a tabuada deve ir: "))

while i <= f: 
    print(f"{numero} x {i} = {numero * i}")
    i += 1 