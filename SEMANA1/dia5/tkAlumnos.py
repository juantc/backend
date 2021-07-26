from tkinter import *
from tkinter.ttk import Treeview
import sqlite3


class Alumno:
    
    db_name='database.s3db'
    
    def ejecutarSql(self,sql,parametros=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor=conn.cursor()
            resultado=cursor.execute(sql,parametros)
            conn.commit()
        return resultado
            
    def readAlumnos(self):
        rsAlumnos = self.trvAlumnos.get_children()
        #limpiando la tabla
        for a in rsAlumnos:
            self.trvAlumnos.delete(a)
            
        sqlAlumnos='select * from alumnos'
        resultado=self.ejecutarSql(sqlAlumnos)
        for fila in resultado:
            self.trvAlumnos.insert('',0,text=fila[0],values=fila[1])
            
    def createAlumno(self):
        sqlInsertAlumno="insert into alumnos values(?,?)"
        parametros=(self.nombre.get(), self.email.get())
        self.ejecutarSql(sqlInsertAlumno,parametros)
        self.readAlumnos()
        
    def __init__(self,window):
        self.wind=window
        self.wind.title('Alumnos')   
         
        #creamos un frame
        frame=LabelFrame(self.wind,text='Registro de Nuevo Alumno')
        frame.grid(row=0,column=0,columnspan=3,pady=10)
            
        #campos del formularo
        #Agregar campo nombre
        #Creamos label para nombre del alumno
        lblNombre=Label(frame,text='Nombre :')
        lblNombre.grid(row=1,column=0)
      
        #Creamos textField para caja de texto del alumno y lo asignamos al atributo 
        self.nombre=Entry(frame)
        self.nombre.grid(row=1,column=1)


        #Creamos label para nombre del email
        lblEmail=Label(frame,text='Email :')
        lblEmail.grid(row=2,column=0)
        #Creamos texfield para caja de texto del alumno y lo asignamos al atributo nombre del alumno
        self.email=Entry(frame)
        self.email.grid(row=2,column=1)
        
        #Creamos label para nombre del celular
        #lblCelular=Label(frame,text='Celular : ')
        #lblCelular.grid(row=3,column=0)
        #Creamos texfield para caja de texto del alumno y lo asignamos al atributo nombre del alumno
        #self.celular=Entry(frame)
        #self.celular.grid(row=3,column=1)        
        

        #Boton para crear nuevo alumno
        btnNuevoAlumno=Button(frame,text='Registrar Alumno',command=self.createAlumno)
        btnNuevoAlumno.grid(row=4,columnspan=2,sticky=W+E)
        #btnNuevoAlumno.grid(row=4,columnspan=2)
        
        
        self.trvAlumnos=Treeview(height=10,columns=2)
        self.trvAlumnos.grid(row=5,column=0,columnspan=2)
        self.trvAlumnos.heading('#0',text='Nombre',anchor=CENTER)
        self.trvAlumnos.heading('#1',text='Email',anchor=CENTER)
        
        self.readAlumnos()
        
window=Tk()
app=Alumno(window)
window.mainloop()