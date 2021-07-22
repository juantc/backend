from statistics import mean

#Ingresar n notas
notas=[]
x=int(input("Ingrese cantidad de notas: "))
for x in range (x):
    nota=int(input("Ingrese nota"+str(x+1)+" : "))
    notas.append(nota)
print(notas)

print("Promedio de notas ",mean(notas))
print("Nota máxima ",max(notas))
print("Nota mínima ",min(notas))

    