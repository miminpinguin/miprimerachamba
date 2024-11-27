print("bienvenido querido usuario, se presenta el menú:")
opcion=1
while opcion!=0:
    
    print("bienvenido querido usuario, se presenta el menú:")
    print("ingresa 1. área del triangulo")
    print("ingresa 2. area del rectangulo")
    print("ingresa 3. area del circulo")
    print("ingresa 4. convertir temperatura de F a C")
    print("ingresa 5. convertir temperatura C a F")
    
input("¿que actividad deseas realizar?")

variables=(input("¿tu actividad requiere de una un radio?"))
if(variables==1):
    baseT=input("ingresa la base del triangulo")
alturaT=input("ingresa la altura del triangulo")
res=(baseT*alturaT)/2
print("el resultado es: ", res)
elif (variables=2):
baseR=input("ingresa la base de tu rectangulo")
alturaR=input("ingresa la altura de tu rectangulo")

res=baseR*alturaB
print("el resultado es: ", res)
elif(variables==3):
res=pi*radio*radio
print("el resultado es: ", res)

elif(variables==4):
res=((fahrenheit-32)*5)/9
print("el resultado es: ", res)

elif( variables==5):
res=(celsius*9/5)+32
print("el resultado es: ", res)
else:
print("syntax error")

opcion=int(input("deseas continuar, sino presiona 0, para salir"))
    


    

    