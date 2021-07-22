#Programa para bucles
n=int(input("Ingrese tabla de multiplicar:"))
for x in range(1,13,2):
    tabla= n*x
    print(str(n)+" x "+str(x)+" = "+str(tabla))