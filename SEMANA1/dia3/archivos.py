"""
f=open('alumnos.txt','a')
print("registro de alumno")

nombre=input("nombre:")
email=input("Email: ")
celular=input("Celular: ")

f.write('\n'+nombre+","+email+","+celular)
f.close()
"""

fr=open('alumnos.txt','r')
alumnos=fr.read()
print(alumnos)

lstAlumnosData=[]
#alumno={}

lstAlumnos=alumnos.splitlines()
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