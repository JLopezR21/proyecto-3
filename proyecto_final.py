from tkinter import *

from tkinter import messagebox

from tkinter.filedialog import askopenfile, asksaveasfile




interfaz=Tk()
interfaz.title("Proyecto Interfaz Grafica")


barraMenu=Menu(interfaz)
interfaz.config(menu=barraMenu, width=500, height=300)



def nuevo():

    texto.delete(1.0,END)


def Abrir_archivo():

    abrir = askopenfile(filetypes=(("Todos los Archivos","*.*"),(" Archivos python","*.py"),(" Archivos de texto","*.txt"),(" Archivos c++","*.cpp"),(" Archivos pseint","*.psc"))) 
       
       

    if abrir != None:

        texto.insert(1.0, abrir.read())

       

def Guardar_como():

    guardar = asksaveasfile(filetypes=(("Todos los Archivos","*.*"),(" Archivos python","*.py"),(" Archivos de texto","*.txt"),(" Archivos c++","*.cpp"),(" Archivos pseint","*.psc"))) 

    print(guardar.write(texto.get(1.0, END)))
    
    
def salir():
    salir1=messagebox.askquestion("salir","¿Desea salir de la interfaz? ")
    if salir1 == 'yes':
        interfaz.quit() 
        interfaz.destroy()
        
        
def copiar():

    texto.clipboard_clear()

    texto.clipboard_append(texto.selection_get())

def pegar():

    texto.insert(INSERT, texto.clipboard_get())

def cortar():

    texto.clipboard_clear()

    texto.clipboard_append(texto.selection_get())

    texto.delete("sel.first", "sel.last")

def deshacer():

    texto.edit_undo()

def rehacer():

    texto.edit_redo()

def Informacion():
    messagebox.showinfo("Acerca de..", " Esta interfaz esta diseñada para archivos de texto,trantado con un entorno de edicion,usando  tkinter, manipulando  archivos .py .txt  .cpp  .psc etc ,Licencia x.org")

def Manual_usuario():
    messagebox.showinfo("Direccion repositorio Github", "https://github.com/JLopezR21/proyecto-3" )
    
def Integrantes():
    messagebox.showinfo("Ayuda"," Jefferson Ramiro Lopez Ramirez 7690-21-1522 ")   

archivoMenu=Menu(barraMenu,tearoff=0)
archivoMenu.add_command(label="Abrir archivo", command = Abrir_archivo)
archivoMenu.add_command(label="Nuevo", command= nuevo)
archivoMenu.add_command(label="Guardar", command = Guardar_como)

archivoMenu.add_separator()
archivoMenu.add_command(label="salir", command = salir)


edicionMenu=Menu(barraMenu,tearoff=0)
edicionMenu.add_command(label="copiar", command= copiar)
edicionMenu.add_command(label="cortar", command= cortar)
edicionMenu.add_command(label="pegar", command= pegar)
edicionMenu.add_separator()
edicionMenu.add_command(label="Rehacer", command= rehacer)
edicionMenu.add_command(label="Deshacer", command= deshacer)

ayudaMenu=Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="Informacion", command= Informacion )
ayudaMenu.add_command(label="Manual de usuario", command= Manual_usuario)
ayudaMenu.add_command(label="Integrantes", command= Integrantes)

barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Edicion",menu=edicionMenu)
barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)

texto = Text(interfaz, undo="true")

texto.pack(side=TOP, fill=BOTH, expand=1)

interfaz.mainloop()