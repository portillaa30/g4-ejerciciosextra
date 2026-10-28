temperatura=int(input("Ingrese la temperatura registrada"))


def evaluar_temperatura(temp):
    if temp< 26:
        print("Temperatura demasiado baja para el desarrollo del embrion.")
    elif temp>34:
        print("Demasiado caliente para el desarrollo del embrion")
    else: 
        print("Temperatura adecuada")

print(evaluar_temperatura(temperatura))