# ***Proyecto, Interfaz Grafica TK*** 

*Jefferson Ramiro Lopez Ramirez*

*7690-21-1522*

## ***librerias utilizadas***

**from tkinter import (*)**

*Importamos la libreria de interfaz Grafica*

**from tkinter import messagebox**

*utilizamos esta libreria como un cuadro de dialogo que esta conformada con una ventanta de titulo, un mensaje en especifico , empleanda para informarle al usuario sobre una cuestion o bien tomar una decision.*

**Algunas de las funciones para generar cuadros de dialogo**

* showinfo ( )
* showwarning ( )
* showerror ( )
* askquestion ( )
* askyesno ( )
* askokcancel ( )
* askyesnocancel ( )
* askretrycancel ( )

**utilizadas en mi proyecto** 

* showinfo ( )
* askquestion ( )

**from tkinter.filedialog import askopenfile, asksaveasfile**

*askopenfile crea un dialogo open (abierto) y retorna el nombre del archivo seleccionado que corresponde a un archvio existente,*
*asksaveasfile crea un dialogo saveas (guardar como) y retorna el nombre del archivo seleccionado.*

**creamos la raiz de nuestra interfaz (ventana de la interfaz)**

*Interfaz=Tk ( )*

**Agregamos el titulo a nuestra interfaz utilizando title(" ")**

*Interfaz.title("Proyecto Interfaz Grafica")*

## ***Estructura de la interfaz***

**creamos nuestro menu y configuramos el ancho y la altura de nuestra interfaz**

~~~
barraMenu=Menu(Interfaz)

Interfaz.config(menu=barraMenu, width=500, height=300)

añadimos el menú creado a la barra de menús con la función add_cascade

Para comprobar que las acciones del menú efectivamente funcionan vamos a crear una etiqueta de texto con la clase Label

Ejemplo:

barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Edicion",menu=edicionMenu)
barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)

~~~

**sub menu con las opciones a realizar**

~~~
(tearroff=0 utilizamos para quitar los guiones que trae por defecto)

barraMenu=Menu(Interfaz)
archivoMenu=Menu(barraMenu,tearoff=0)
archivoMenu.add_command(label="Abrir archivo", command = Abrir_archivo)
archivoMenu.add_command(label="Nuevo", command= nuevo)
archivoMenu.add_command(label="Guardar como", command = Guardar_Como)
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

~~~


## ***funcionalidad de nuestro Menu***

*utilizamos funciones para hacer que las opciones de nuestro menu respondan correctamente*

*utilizamos command=el nombre de nuestra funcion que ira conectado al sub menu para poder ejecutarse de forma correcta*

~~~
def nuevo():

    texto.delete(1.0,END)

Ejemplo:

archivoMenu.add_command(label="Nuevo", command= nuevo)

seria el mismo proceso para las demas funciones
~~~

~~~
def Abrir_archivo():

    abrir = askopenfile(filetypes=((" Todos los Archivos","*.*"),(" Archivos python","*.py"), (" Archivos c++","*.cpp"),(" Archivos pseint","*.psc"),(" Archivos de texto","*.txt"))) 
       

    if abrir != None:

        texto.insert(1.0, abrir.read())

~~~

~~~
def Guardar_Como():

    guardar = asksaveasfile(filetypes=((" Todos los Archivos","*.*"),(" Archivos python","*.py"), (" Archivos c++","*.cpp"),(" Archivos pseint","*.psc"),(" Archivos de texto","*.txt"))) 
       

    print(guardar.write(texto.get(1.0, END)))
    
~~~

~~~
def salir():
    salir1=messagebox.askquestion("salir","¿Desea salir de la interfaz? ")
    if salir1 == 'yes':
        Interfaz.quit() 
        Interfaz.destroy()
~~~

  ~~~      
def copiar():

    texto.clipboard_clear()

    texto.clipboard_append(texto.selection_get())

~~~

~~~
def pegar():

    texto.insert(INSERT, texto.clipboard_get())
~~~

~~~
def cortar():

    texto.clipboard_clear()

    texto.clipboard_append(editor.selection_get())

    texto.delete("sel.first", "sel.last")
~~~

~~~

def deshacer():

    texto.edit_undo()
~~~

~~~
def rehacer():

    texto.edit_redo()
~~~
def Manual_usuario():
    messagebox.showinfo("Direccion repositorio Github", "https://github.com/JLopezR21/proyecto-3")
~~~
def Integrantes():
    messagebox.showinfo("Ayuda"," Jefferson Ramiro Lopez Ramirez 7690-21-1522 ")   
~~~
~~~
def Informacion():
    messagebox.showinfo("Acerca de..", " Esta interfaz esta diseñada para archivos de texto,trantado con un entorno de edicion,usando  tkinter, manipulando  archivos .py .txt  .cpp  .psc etc ","Licencia x.org)
~~~

*Luego de tener nuestra barra de Menu generamos un campo de texto*

*utilizamos la palabra text (texto largo)*

*utilizamos el metodo pack para ajustar todos los elementos dentro de nuestra interfaz*

~~~

texto = Text(Interfaz, undo="true")

texto.pack(side=TOP, fill=BOTH, expand=1)

~~~

**metodo main loop( )**

*usando el método mainloop(), que lanza el bucle principal, encargado de gestionar todos los eventos que reciba la aplicación.*