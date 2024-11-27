#crear unciones

#funciones llamada saludar, a recibir nel nombre
def saludar(nombre):
    print("holaaaa", nombre)

nom=input("ingresa tu nombre")
saludar(nom)

def sumita(n1, n2, n3, n4, n5):
    res_suma=n1+n2+n3+n4+n5
    return res_suma
n1=int(input("ingresa el primer numero"))
n2=int(input("ingresa el segundo numero"))
n3=int(input("ingresa el tercero numero"))
n4=int(input("ingresa el cuarto numero"))
n5=int(input("ingresa el quinto numero"))
print(sumita(n1, n2, n3, n4, n5))
#crear una función llamada area_triangulo
#que reciba base y altura
#regrese el resultado del área
def area_triangulo(b,h):
    area=(b*h)/2
    return area
#usar la función
print(area_triangulo(4,5))


########ejercicio
'''crear una función llamada multiplicar que reciba 3 numeros, regresar el resultado
'''

def multiplicar(num1, num2, num3):
    multi=(num1*num2*num3)
    return multi
print(multiplicar(4,5,3))


'''crear una funcion llamada largo_cadena
que reciba un texto y devuelva 
la cantidad de caracteres de la misma'''
#usar la funcion print(largo cadena("el mundo es bonito"))
def largo_cadena(txt):
    text=len(txt)
    return text
print(largo_cadena("the world is beatiful"))

''' crear una funcion llamda promedio 
que reciba 2 calificaciones y devuelva el promedio'''
#pedir calif. primer y segundo parcial
#print("el promedio es: " promedio(cal1, cal2))
def promedio(cal1, cal2):
    prom=(cal1+cal2)/2
    return prom
cal1=int(input("ingresa la primera calificacion "))
cal2=int(input("ingresa la segunda calificacion "))
print(promedio(cal1,cal2))

#crear una función que reciba el nombre 
#de la persona, su edad y el mes de nacimiento
#devuelva:
#las dos primeras letras del nombre-edad-primer
#letra del mes
#ejemplo:MA170
def disk_curp(name, age, mounth):
    letras=name[0:2]
    print(letras)
disk_curp("MIKE", 17, "OCTOBER")
