
#Ultimos_digitos_iguales
#Determinar si los dos ultimos digitos de un numero entero son iguales

#input
n=int(input("Digite el numero: "))

#Procesing
if n<0:
    n=n*-1
else:
    n=n
a=n%10
b=n//10
c=b%10
if 0<n<9:
     print("El numero no cuenta como minimo 2 digitos")
else:
    if  a==c:
        print("--------------------------")
        print("Los 2 ultimos digitos del numero son iguales")
        print("----------------------------------------")
    else:
        print("------------------------------------")
        print("Los 2 utimos digitos del numero no son iguales")
        print("-----------------------------------------")
    
