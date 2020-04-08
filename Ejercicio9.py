import random
vidas=0
print("Hola! Cual es tu nombre?")
name=input()
numero=random.randint(1,50)
print("Bueno, "+name+", estoy pensando en un numero entre 1 y 50")
print("Adivina")
while vidas<6:
    if vidas==3:
        if ((numero%2)==0):
            print("Una ayuda, el numero es par")
        else:
            print("Una ayuda, el numero es impar")    
    intento=input()
    intento=int(intento)
    if intento<numero:
        print("El numero es demasiado bajo")
        vidas=vidas+1
    elif intento>numero:
        print("El numero es demasiado alto")
        vidas=vidas+1
    elif intento==numero:
        print("Buen trabajo, ADIVINASTE!")
if vidas==6:
    print("No Adivinaste, PERDISTE")
