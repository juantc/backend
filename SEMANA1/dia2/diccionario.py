#Manejo de diccionarios
capitales={'Perú' : 'Lima','Ecuador' : 'Quito','Chile':'Santiago','Uruguay':'Montevideo','Brasil':'Brasilia'}

print(capitales['Perú'])
print(capitales)
capital={'USA':'Washington DC'}
capitales.update(capital) #para agregar valoral Diccionario
print(capitales)

alumnos={
    'nombre':'Cesar Mayta',
    'email': 'cesarmayta@gmail.com',
    'celular': '956290589'
}
print('-------------')
print(alumnos['nombre'])
print('-------------')
print(alumnos['email'])
alumnoModelo=alumnos.copy()
alumnos['email']='cmayta@gmail.com'
print(alumnos['email'])
print(alumnoModelo)

#eliminar alumno
a=alumnos.pop('dni','no existe dni')
print(a)
print(alumnos)


#eliminar todos los valores
#alumnos={}
#alumnos.clear()

print(alumnos)

#imprimir las llaves
print(alumnos.keys())

print(alumnos.values())
print('****************')
for clave in alumnos:
    print(clave, alumnos[clave])

for clave in alumnos.keys():
    print(clave, alumnos[clave])
    
for clave,valor in alumnos.items():
    print(clave,valor)
    
