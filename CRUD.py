import tkinter as tk
import tkinter
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from logicaNegocios import *
from regular_expressions_validations import *

class ventanaTkinter():
    '''
    Subclase ventana, se encarga de configurar la ventana
    y agregar widgets para que estos sean mostrados en la interfaz gráfica.
    ---
    Atributos
    -------
    ventana = tk
        Ventana a configurar (Heredado de la clase ventanaTkinter)
    Métodos:
    ----------
    __init__(self, ventana):
        Cosntructor de los atributos de la clase
    '''
    def __init__(self, ventana):
    
        '''
        Constructor de los parámetros a usar
        ---
        Parámetros:
            ventana: str
                Variable donde se asignará la ventana la cual se va a mostrar
        '''
        self.ventana = ventana


class ventanaMiesAdmin(ventanaTkinter):
    '''
    Subclase ventanaMiesAdmin, se encarga de configurar la ventana
    y agregar widgets para que estos sean mostrados en la interfaz gráfica.
    ---
    Atributos
    -------
    ventana = tk
        Ventana a configurar (Heredado de la ventana ventanaTkinter)
    Métodos:
    ----------
    ventanaControl (self):
        Permite la configuración directa de la ventana administrador.
    '''

    def ventanaControl (self):
        '''
        Configuración de la ventana principal del CRUD
        '''
        #Se cierra la ventana anterior
        """self.ventana.withdraw()"""
        #Asignamos una subventana
        """self.ventana = tk.Toplevel()"""

        '''Propiedades de la ventana'''
        self.ventana.title("BONO - MIES")
        self.ventana.config(bg="white")
        self.ventana.geometry("1040x500")
        self.ventana.resizable(width="False", height="False")

        self.tablaDatos()

    def tablaDatos (self):
        '''
        Función donde se encuentran widgets, entre los principales
        destaca el TreeView para la recopilación de información en una tabla
        '''
        scrollbarX = Scrollbar (self.ventana, orient = HORIZONTAL)
        scrollbarY = Scrollbar (self.ventana, orient = VERTICAL)
        
        #Asignación de columbas de la tabla
        self.tablaDatos = ttk.Treeview(self.ventana, columns =  ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11', '#12'))
        
        #Propiedades de la tabla (posición y tamaño)
        self.tablaDatos.place(relx=0.00, rely=0.200, width=1020, height=380)

        #Creación de scrollbars, tanto en eje vertica como en eje horizontal 
        scrollbarX.place(relx= 0, rely =0.965, width=1020)
        scrollbarY.place(relx= 0.98, rely =0.0, height=500)
        
        #Configuración de las scrollbars para sincronizarlas con la tabla
        self.tablaDatos.configure(xscrollcommand=scrollbarX.set, yscrollcommand=scrollbarY.set)
        scrollbarY.configure(command=self.tablaDatos.yview)
        scrollbarX.configure(command=self.tablaDatos.xview)

        #Asignación de propiedades a cada una de las columnas de la tabla
        self.tablaDatos.heading("#0", text = "Cédula",anchor=W)
        self.tablaDatos.heading("#1", text = "Nombre",anchor=W)
        self.tablaDatos.heading("#2", text = "Nombre2",anchor=W)
        self.tablaDatos.heading("#3", text = "Apellido",anchor=W)
        self.tablaDatos.heading("#4", text = "Apellido2",anchor=W)
        self.tablaDatos.heading("#5", text = "Provincia",anchor=W)
        self.tablaDatos.heading("#6", text = "Cantón",anchor=W)
        self.tablaDatos.heading("#7", text = "Genero",anchor=W)
        self.tablaDatos.heading("#8", text = "Estado",anchor=W)
        self.tablaDatos.heading("#9", text = "Rol",anchor=W)
        self.tablaDatos.heading("#10", text = "CorreoElectronico",anchor=W)
        self.tablaDatos.heading("#11", text = "Hijos",anchor=W)
        self.tablaDatos.heading("#12", text = "Beneficiario",anchor=W)

        #Llamado de funciones para la tabla
        self.insertDatesTable()
        self.widgetsCRUD()

    def widgetsCRUD(self):
        '''
        Creación de cada uno los widgets para ingresar datos a la base de datos.
        '''

        '''Label texto primer nombre'''
        mostrarLabel=tk.Label(self.ventana, text = "Nombre: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=0, y=1)
        '''Label texto segundo nombre'''
        mostrarLabel=tk.Label(self.ventana, text = "Nombre 2: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=0, y=25)
        '''Label texto apellido'''
        mostrarLabel=tk.Label(self.ventana, text = "Apellido: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=0, y=50)
        '''Label texto segundo apellido'''
        mostrarLabel=tk.Label(self.ventana, text = "Apellido 2: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=0, y=75)
        '''Label texto género'''
        mostrarLabel=tk.Label(self.ventana, text = "Género: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=200, y=1)
        '''Label texto cédula'''
        mostrarLabel=tk.Label(self.ventana, text = "Cédula: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=200, y=25)
        '''Label texto provincia'''
        mostrarLabel=tk.Label(self.ventana, text = "Provincia: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=189, y=50)
        '''Label texto Cantón'''
        mostrarLabel=tk.Label(self.ventana, text = "Cantón: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=200, y=75)
        '''Label texto edad'''
        mostrarLabel=tk.Label(self.ventana, text = "Edad: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=350, y=1)
        '''Label correo electrónico'''
        mostrarLabel=tk.Label(self.ventana, text = "Correo: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=350, y=25)
        '''Label texto Hijos del usuario'''
        mostrarLabel=tk.Label(self.ventana, text = "Hijos: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=350, y=75)
        '''Label texto estados en los que puede estar un usuario'''
        mostrarLabel=tk.Label(self.ventana, text = "Estado: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=350, y=50)
        '''Label texto roles de los usuarios existentes'''
        mostrarLabel=tk.Label(self.ventana, text = "Rol: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=530, y=75)
        '''Label texto roles de los usuarios existentes'''
        mostrarLabel=tk.Label(self.ventana, text = "Benefiario: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=650, y=75)
        '''Label texto, buscar por cédula'''
        mostrarLabel=tk.Label(self.ventana, text = "Buscar por cédula: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=750, y=1)

        '''Entradas de texto (Entrys)'''
        '''Entrada de texto del primer nombre'''
        self.nombreEntry=tk.Entry(self.ventana, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.nombreEntry.place(x=65, y=0)
        '''Entrada de texto del segundo nombre'''
        self.nombre2Entry = tk.Entry(self.ventana, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.nombre2Entry.place(x=65, y=25)
        '''Entrada de texto del primer apellido'''
        self.apellidoEntry = tk.Entry(self.ventana, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.apellidoEntry.place(x=65, y=50)
        '''Entrada de texto del segundo apellido'''
        self.apellido2Entry = tk.Entry(self.ventana, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.apellido2Entry.place(x=65, y=75)
        '''Entrada de texto de la ciudad del usuario'''
        self.cedulaEntry = tk.Entry(self.ventana, font=font.Font(family="Arial", size = "8"),textvar="", width=13, relief="solid")
        self.cedulaEntry.place(x=250, y=25)
        '''Entrada de texto de la edad del usuario'''
        self.edadEntry= tk.Entry(self.ventana, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.edadEntry.place(x=400, y=1)
        '''Entrada de texto del correo electrónico del usuario'''
        self.correoElectronico= tk.Entry(self.ventana, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.correoElectronico.place(x=400, y=25)
        '''Entrada de texto de la cantidad de hijos del usuario'''
        self.hijosEntry= tk.Entry(self.ventana, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.hijosEntry.place(x=400, y=75)
        '''Entrada de texto para buscar un usuario por su cédula'''
        self.buscarCedula = tk.Entry(self.ventana, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.buscarCedula.place(x=870, y=1)

        #COMBOBOXS
        '''Menu despegable para elegir la provincia y el cantón del usuario'''
        self.provinciaEntry = ttk.Combobox(
            self.ventana, 
            width=10, 
            state="readonly",
            values=tuple(conectarMongo.diccionarioPyC().keys()))
        self.provinciaEntry.place(x=250, y=50)
        self.provinciaEntry.bind("<<ComboboxSelected>>", on_combobox_select1)

        '''Menu despegable cantón que dependerá de las opciones de la ventana provincia'''
        self.cantonEntry = ttk.Combobox(self.ventana, width=10, state="readonly")
        self.cantonEntry.place(x=250, y=75)

        '''Menú despegable donde mostrará la lista de generos a las que se puede elegir'''
        self.generoEntry = ttk.Combobox(self.ventana, value= conectarMongo.listaGeneros(), width=8, state="readonly")
        self.generoEntry.place(x=250, y=1)

        '''Menú despegable donde mostrará la lista de estados a las que se puede elegir'''
        self.estadoEntry = ttk.Combobox(self.ventana, value= conectarMongo.estadosUsuarios(), width=15, state="readonly")
        self.estadoEntry.place(x=400, y=50)

        '''Menú despegable donde mostrará la lista de roles a las que se puede elegir'''
        self.rolEntry = ttk.Combobox(self.ventana, value= conectarMongo.mostrarRoles(), width=10, state="readonly")
        self.rolEntry.place(x=560, y=75)

        '''Menú despegable donde mostrará la lista de beneficiarios a las que se puede elegir'''
        self.beneficarioEntry = ttk.Combobox(self.ventana, value= conectarMongo.beneficariosUsuarios(), width=10, state="readonly")
        self.beneficarioEntry.place(x=720, y=75)
        
        #BOTONES

        '''Botón que permite actualizar la tabla'''
        getDatosBoton= tk.Button(self.ventana, text= "Agregar", 
            cursor="hand2", bg= "#5172f3",fg= "white",  
            width=10, height=1, relief="flat", font=("Arial", 8, "bold"),
            command = self.actualizarTabla)
        getDatosBoton.place(x=530, y=1)

        '''Botón inserta datos en la tabla como a su vez en la base de datos'''
        actualizarTabla= tk.Button(self.ventana, text= "Actualizar", 
            cursor="hand2", bg= "#1b9e1d",fg= "white",  
            width=10, height=1, relief="flat", font=("Arial", 8, "bold"),
            command = self.insertDatesTable)
        actualizarTabla.place(x=530, y=30)

        '''Botón editar datos en la tabla como a su vez en la base de datos'''
        editarTabla= tk.Button(self.ventana, text= "Editar", 
            cursor="hand2", bg= "#edc30f",fg= "white",  
            width=10, height=1, relief="flat", font=("Arial", 8, "bold"),
            command = self.editarDatos)
        editarTabla.place(x=620, y=1)

        '''Botón elimina datos en la tabla como a su vez en la base de datos'''
        eliminarTabla= tk.Button(self.ventana, text= "Eliminar", 
            cursor="hand2", bg= "#ff0206",fg= "white",  
            width=10, height=1, relief="flat", font=("Arial", 8, "bold"),
            command = self.elimarDato)
        eliminarTabla.place(x=620, y=30)

        '''Botón elimina datos en la tabla como a su vez en la base de datos'''
        eliminarTabla= tk.Button(self.ventana, text= "🔎", 
            cursor="hand2", bg= "#0a509f",fg= "white",  
            width=2, height=1, relief="flat", font=("Arial", 8, "bold"),
            command = self.buscarDatoEnTabla)
        eliminarTabla.place(x=970, y=1)
    
    def insertDatesTable(self):
        '''
        Función que permite ingresar datos a la tabla y mostrarla en la misma
        (Esta se actualizará cada que se llame a la misma)
        '''
        #Elimnar datos dentro de la base de datos, permitiendo a actualización de la misma
        datos = self.tablaDatos.get_children()
        for dato in datos:
            self.tablaDatos.delete(dato)

        #Llenar las casillas de la tabla con los datos de la base de datos
        listaDatos = conectarMongo.coleccionPersonas.find()
        
        for listaDatos in conectarMongo.coleccionPersonas.find():
            '''
            Bucle donde se van a insertar todos los datos que existen en la base de datos
            dentro de la tabla.
            '''
            #Insertamos datos
            self.tablaDatos.insert("", END, text = (listaDatos["cedula"]), values=(listaDatos["nombre"], 
            listaDatos["nombre2"],
            listaDatos["apellido"],
            listaDatos["apellido2"],
            listaDatos["provincia"],
            listaDatos["canton"],
            listaDatos["genero"],
            listaDatos["estado"],
            listaDatos["rol"],
            listaDatos["correoElectronico"],
            listaDatos["hijos"],
            listaDatos["beneficiario"]
            ))
            

    
    def actualizarTabla (self):
        '''
        Actualización de datos dentro de la tabla
        '''
        getDatos(
                self.nombreEntry.get(),
                self.nombre2Entry.get(),
                self.apellidoEntry.get(),
                self.apellido2Entry.get(),
                self.provinciaEntry.get(),
                self.cantonEntry.get(),
                self.cedulaEntry.get(),
                self.edadEntry.get(),
                self.generoEntry.get(),
                self.estadoEntry.get(),
                self.correoElectronico.get(),
                self.hijosEntry.get(),
                self.rolEntry.get(),
                self.beneficarioEntry.get()
            )
        #Llamamos a la función para actualizar la tabla de datos.
        self.insertDatesTable()
        
    def obtenerDato (self):
        '''
        Método el cual nos permite obtener el dato de la tabla
        seleccionando los items de la misma.
        ---
        Return
        -------
        return item_details.get("text")
            Retorna la cédula de la casilla selecionada
        '''
        selected_item = self.tablaDatos.focus()
        item_details = self.tablaDatos.item(selected_item)
        return item_details.get("text")

    def elimarDato (self):
        '''
        Método el cual nos permite elimar un dato de la base de datos
        y a su vez, actualizar la tabla para que este ya no se encuentre 
        en la misma.
        '''
        query = {"cedula": self.obtenerDato()}
        conectarMongo.coleccionPersonas.delete_one(query)
        self.insertDatesTable()

    def buscarDatoEnTabla(self):
        '''Busca datos correspondientes a la cédula de identidad de un usuario'''
        #Elimnar datos dentro de la base de datos, permitiendo a actualización de la misma
        datos = self.tablaDatos.get_children()
        for dato in datos:
            self.tablaDatos.delete(dato)

        #Llenar las casillas de la tabla con los datos de la base de datos
        query = {'cedula': self.buscarCedula.get()}
        listaDatos = conectarMongo.coleccionPersonas.find()
        specificFind = conectarMongo.coleccionPersonas.find(query)

        for listaDatos in specificFind:
            '''
            Bucle donde se van a insertar todos los datos que existen en la base de datos
            dentro de la tabla.
            '''
            #Insertamos datos
            self.tablaDatos.insert("", END, text = (listaDatos["cedula"]), values=(listaDatos["nombre"], 
            listaDatos["nombre2"],
            listaDatos["apellido"],
            listaDatos["apellido2"],
            listaDatos["provincia"],
            listaDatos["canton"],
            listaDatos["genero"],
            listaDatos["estado"],
            listaDatos["rol"],
            listaDatos["correoElectronico"],
            listaDatos["hijos"],
            listaDatos["beneficiario"]
            ))
        
    def editarDatos(self):
        self.ventaneEditar = tk.Toplevel()
        self.ventaneEditar.title("Datos")
        self.ventaneEditar.geometry("300x300")
        self.ventaneEditar.resizable(width="False", height="False")


def getDatos (nombre, nombre2, apellido, apellido2, provincia, canton, cedula, edad, genero, estado, correoElectronico, hijos, rol, beneficario):
    '''
    Método el cual se encarga validar cada uno de los datos que ingresa un usuario:
    El ingreso de datos personales como nombres o apellidos serán validados que no tengan números
    '''
    if validarNombresRE(nombre, 'nombre'): #Validar nombre
        if validarNombresRE(nombre2, 'nombre'): #Validar nombre2
            if validarNombresRE(apellido, 'apellido'): #Validar apellido
                if validarNombresRE(apellido2, 'apellido'): #Validar apellido2
                    if validarCedulaRE(cedula): #Validar cédula
                        if validarPyCRE(provincia, canton): #Validar provincia y cantón
                                if validarEdadRE(edad): #Validar edad
                                        if validarCorreoRE(correoElectronico): #Validar correo electrónico
                                            if hijos.isnumeric(): #Validar edad
                                                if validarRol(rol):
                                                    '''
                                                    Siendo todos los datos validados se crea un diccionario
                                                    mismo el cual será ingresado en la base de datos.
                                                    '''
                                                    diccionario={'nombre': nombre.upper(), 
                                                                'nombre2':nombre2.upper(), 
                                                                'apellido': apellido.upper(), 
                                                                'apellido2': apellido2.upper(),
                                                                'provincia': provincia, 
                                                                'canton': canton, 
                                                                'cedula': cedula, 
                                                                'edad': edad,
                                                                'genero': genero,
                                                                'estado': estado,
                                                                'rol': rol,
                                                                'correoElectronico': correoElectronico,
                                                                'hijos': hijos,
                                                                'beneficiario' : beneficario
                                                                }
                                                    #Ingresamos el diccionario a nuestra base de datos.
                                                    updateDataBase=conectarMongo.coleccionPersonas.insert_one(diccionario)
                                                    return True
                                                    
                                            else:
                                                messagebox.showwarning("Error", hijos + " no es un valor válido")

def on_combobox_select1(event):
    '''
    Función encargada de validar la información de un 
    combobox dependiente de otro por medio de un diccionario
    '''
    ventanaAdmin.cantonEntry.set("")
    ventanaAdmin.cantonEntry.config(values=conectarMongo.diccionarioPyC()[ventanaAdmin.provinciaEntry.get()])
    pass

if __name__ == '__main__':
    '''Instancia de la clase a PageLoader para poder conectar a MongoDB'''
    conectarMongo = PageLoader(myClient)

    '''Instancia de Tkinter tanto como de la clase ventanasMies para abrir la ventana principal'''    
    ventana = Tk()
    
    '''Instancia de la clase personaMies'''
    ventanaAdmin=ventanaMiesAdmin(ventana)
    
    '''Invocación a la clase principal'''
    ventanaAdmin.ventanaControl()

    '''Función mainloop'''
    ventana.mainloop()