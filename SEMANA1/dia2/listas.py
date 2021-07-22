#Trabajo con listas
primos=[2,3,5,7,]  #números primos
dias=["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]

fecha=["martes",20,"julio",2021] #valores de tipos diferentes

print(dias[1:5])
#print(fecha)
print(len(primos))
primos.append(17)
print(primos)

dias.pop() #elimina el último registro
print(dias)

del primos[3]
print(primos)

primos.insert(3,7)
print(primos)

for x in dias:
    print(x)