from libEscuela import clsAlumno
import os
#PROGRAMA PARA GESTÓN DE ALUMNOS
#CRUD : CREATE , READ, UPDATE, DELETE
#DEFINIR VARIABLES DE ENTRADA Y SALIDA
alumnos = []
alumno = {}
salir = 'no'

def menuopciones():
    print("*" * 20)
    print("[1] REGISTRAR ALUMNO")
    print("[2] MOSTRAR ALUMNOS")
    print("[3] ACTUALIZAR ALUMNO")
    print("[4] ELIMINAR ALUMNO")
    print("*" * 20)
    
    
def cargarAlumnos(strAlumnos):
    lstAlumnosData=[]
    lstAlumnos=strAlumnos.splitlines()
    del lstAlumnos[0]
    for objAlumno in lstAlumnos:
        lstObjAlumno=objAlumno.split(',')
        nombre=lstObjAlumno[0]
        email=lstObjAlumno[1]
        celular=lstObjAlumno[2]
        nuevoAlumno=clsAlumno(nombre,email,celular)
        lstAlumnosData.append(nuevoAlumno)
    return lstAlumnosData

def mostrarAlumnos():
    
    
fr = open('alumnos.txt','r')
fAlumnos = fr.read()
print(fAlumnos)
alumnos = cargarAlumnos(fAlumnos)
fr.close()

while(salir == 'no'):
    menuopciones()
    opcion = input("INGRESE OPCIÓN: ")
    if(opcion == "1"):
        print("REGISTRO DE NUEVO ALUMNO:")
        nombre = input("NOMBRE : ")
        email = input("EMAIL : ")
        celular = input("CELULAR : ")
        alumnos = createAlumno(nombre,email,celular,alumnos)
    elif(opcion == "2"):
        readAlumno(alumnos)
    elif(opcion == "3"):
        updateAlumno(alumnos)
    elif(opcion=="4"):
        deleteAlumno(alumnos)
    else:
        print("MARCO UNA OPCIÓN INCORRECTA")
        continue
    
    print("Desea salir del programa? ")
    salir = input()
    
    if(salir == "si"):
        strAlumnosGrabar = grabarAlumnos(alumnos)
        fw = open('alumnos.txt','w')
        fw.write(strAlumnosGrabar)
        fw.close()