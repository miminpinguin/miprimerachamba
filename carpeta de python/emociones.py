

opcion=1

while opcion!=0:
    num1=int(input("ingresa el primer numero"))
    num2=int(input("ingresa el segundo numero"))
    print("ingresa 1. sumar")
    print("ingresa 2. restar")
    print("ingresa 3. multiplicar")
    print("ingresa 4. dividir")
    op=int(input("¿Que operación quieres hacer con esos numeros?"))
    if (op==1):
        res=num1+num2
        print("la suma de los numeros es: ", res)
    elif(op==2):
        res=num1-num2
    

        print("la resta de los numeros es: ", res)
    elif (op == 3):
        res = num1 * num2
        print("La multiplicación de los números es:", res)
    elif (op == 4):
            res = num1 / num2
            print("La división de los números es:", res)
    else:
        print("no valido")
    opcion=int(input("deseas continuar, sino presiona 0, para salir"))
    