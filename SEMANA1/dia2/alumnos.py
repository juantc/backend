#Programa para gestión de alumnos
#CRUD: CREATE, READ, UPDATE, DELETE
#Definir variables de entrada y salida
alumnos=[]
alumno={}
salir='no'

#Lógica

    
def menuopciones():
    print("*" * 20)
    print("[1] REGISTRAR ALUMNO")    
    print("[2] MOSTRAR ALUMNO")    
    print("[3] ACTUALIZAR ALUMNO")    
    print("[4] ELIMINAR ALUMNO")    
    print("*" * 20)
    
while(salir=='no'):
    cargarArchivo()
    #print("OPCIONES : 1-Registrar alumno   2-Mostrar alumnos")
    menuopciones()
    opcion=input()
    if(opcion=="1"):
        print("REGISTRO DE NUEVO ALUMNO: ")
        nombre=input("Nombre : ")
        email=input("Email : ")
        celular=input("Celular : ")
    elif(opcion == "2"):
        print("LISTADO DE ALUMNOS")
        readAlumno()
    elif(opcion=="3"):
        print("ACTUALIZAR ALUMNO")
        updateAlumno()
    elif(opcion=="4"):
        print("ELIMINAR ALUMNO")
        deleteAlumno()
    else:
        print("MARCÓ UNA OPCIÓN INCORRECTA")
        continue
    print("Desea salir del programa? si/no")
    salir=input()
#Mostrar resultados