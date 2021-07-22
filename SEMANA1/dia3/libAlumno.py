#libreria alumno

def cargarAlumnos(strAlumnos):
    lstAlumnosData=[]
    #alumno={}
    lstAlumnos=strAlumnos.splitlines()
    print(lstAlumnos)
    del lstAlumnos[0]
    for objAlumno in lstAlumnos:
        lstObjAlumno=objAlumno.split(',')
        print(lstObjAlumno)
        nombre=lstObjAlumno[0]
        email=lstObjAlumno[1]
        celular=lstObjAlumno[2]
        dicAlumno={
            'nombre':nombre,
            'email':email,
            'celular':celular
        }
        lstAlumnosData.append(dicAlumno)
    print(lstAlumnosData)
    fr.close()





def createAlumno(nombre,email,celular):
    nuevoAlumno={
            'nombre': nombre,
            'email': email,
            'celular': celular
        }
    alumnos.append(nuevoAlumno)
    #return 1

def readAlumno():
    #print(alumnos)
    for a in alumnos: #a es un diccionario
        print("================")
        for clave,valor in a.items():
            print(clave+" : "+valor)

def updateAlumno():
    print("ACTUALIZAR ALUMNO")
    posAlumno=-1
    alumnoBusqueda=input("INGRESE EL NOMBRE DEL ALUMNO")
    for i in range(len(alumnos)):    
        a=alumnos[i]
        for clave,valor in a.items():
            if valor==alumnoBusqueda:
                print(a)
                posAlumno=i
                print("posición del alumno:"+str(posAlumno))
                break
    print("ACTUALIZANDO DATOS DEL ALUMNO: ")
    nombre=input("Nombre : ")
    email=input("Email : ")
    celular=input("Celular : ")  
    actAlumno={
            'nombre': nombre,
            'email': email,
            'celular': celular        
        }
    del alumnos[posAlumno]
    alumnos.insert(posAlumno,actAlumno)
          
def deleteAlumno():

    print("ELIMINAR ALUMNO") 