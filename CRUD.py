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
        self.ventana.title("BASE DE DATOS DPA")
        self.ventana.config(bg="white")
        self.ventana.geometry("1040x500")
        #self.ventana.resizable(width="False", height="False")

        self.tablaDatos()

    def tablaDatos (self):
        '''
        Función donde se encuentran widgets, entre los principales
        destaca el TreeView para la recopilación de información en una tabla
        '''
        scrollbarX = Scrollbar (self.ventana, orient = HORIZONTAL)
        scrollbarY = Scrollbar (self.ventana, orient = VERTICAL)
        
        #Asignación de columbas de la tabla
        self.tablaDatos = ttk.Treeview(self.ventana, columns =  ('#1', '#2', '#3', '#4', '#5', '#6', '#7'))
        
        #Propiedades de la tabla (posición y tamaño)
        self.tablaDatos.place(relx=0.00, rely=0.200, width=1310, height=535)

        #Creación de scrollbars, tanto en eje vertica como en eje horizontal 
        scrollbarX.place(relx= 0, rely =0.965, width=1320)
        scrollbarY.place(relx= 0.98, rely =0.0, height=700)
        
        #Configuración de las scrollbars para sincronizarlas con la tabla
        self.tablaDatos.configure(xscrollcommand=scrollbarX.set, yscrollcommand=scrollbarY.set)
        scrollbarY.configure(command=self.tablaDatos.yview)
        scrollbarX.configure(command=self.tablaDatos.xview)

        #Asignación de propiedades a cada una de las columnas de la tabla
        self.tablaDatos.heading("#0", text = "PROV_COD",anchor=W)
        self.tablaDatos.heading("#1", text = "PROV_DESC",anchor=W)
        self.tablaDatos.heading("#2", text = "PROV_TAMA",anchor=W)
        self.tablaDatos.heading("#3", text = "PROV_HAB",anchor=W)
        self.tablaDatos.heading("#4", text = "PROV_HOMBRES",anchor=W)
        self.tablaDatos.heading("#5", text = "PROV_MUJERES",anchor=W)
        self.tablaDatos.heading("#6", text = "PROV_PREFECTO",anchor=W)
        self.tablaDatos.heading("#7", text = "PROV_FECHA",anchor=W)

        #Llamado de funciones para la tabla
        self.insertDatesTable()
        self.widgetsCRUD()

    def widgetsCRUD(self):
        '''
        Creación de cada uno los widgets para ingresar datos a la base de datos.
        '''

        '''Label texto primer nombre'''
        mostrarLabel=tk.Label(self.ventana, text = "Código: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=0, y=1)
        '''Label texto segundo nombre'''
        mostrarLabel=tk.Label(self.ventana, text = "Nombre: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=0, y=25)
        '''Label texto apellido'''
        mostrarLabel=tk.Label(self.ventana, text = "Tamaño: ")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=0, y=50)
        '''Label texto segundo apellido'''
        mostrarLabel=tk.Label(self.ventana, text = "Num. Habitantes:")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=0, y=75)
        '''Label texto género'''
        mostrarLabel=tk.Label(self.ventana, text = "Num. Hombres")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=200, y=1)
        '''Label texto cédula'''
        mostrarLabel=tk.Label(self.ventana, text = "Num. Mujeres")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=200, y=25)
        '''Label texto provincia'''
        mostrarLabel=tk.Label(self.ventana, text = "Prefecto")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=200, y=50)
        '''Label texto Cantón'''
        mostrarLabel=tk.Label(self.ventana, text = "Fecha")
        mostrarLabel.config(bg= "white", fg="#4779b2",font=("Arial", 8, "bold"))
        mostrarLabel.place(x=200, y=75)

        '''Entradas de texto (Entrys)'''
        '''Entrada de texto del primer nombre'''
        x_1 = 100
        x_2= 300
        
        self.PROV_COD=tk.Entry(self.ventana, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.PROV_COD.place(x=x_1, y=0)

        self.PROV_DESC = tk.Entry(self.ventana, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.PROV_DESC.place(x=x_1, y=25)
 
        self.PROV_TAMA = tk.Entry(self.ventana, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.PROV_TAMA.place(x=x_1, y=50)

        self.PROV_HAB = tk.Entry(self.ventana, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.PROV_HAB.place(x=x_1, y=75)
        
       
        self.PROV_HOMBRES = tk.Entry(self.ventana, font=font.Font(family="Arial", size = "8"),textvar="", width=13, relief="solid")
        self.PROV_HOMBRES.place(x=x_2, y=0)
        
        self.PROV_MUJERES= tk.Entry(self.ventana, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.PROV_MUJERES.place(x=x_2, y=25)
       
        self.PROV_PREFECTO= tk.Entry(self.ventana, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.PROV_PREFECTO.place(x=x_2, y=50)
        
        self.PROV_FECHA= tk.Entry(self.ventana, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.PROV_FECHA.place(x=x_2, y=75)

        self.elementoEnTabla = tk.Entry(self.ventana, font=font.Font(family="Arial", size = "8"),textvar="", width=15, relief="solid")
        self.PROV_FECHA.place(x=870, y=5)
        
        #COMBOBOXS
        '''Menu despegable para elegir la provincia y el cantón del usuario'''
        # self.provinciaEntry = ttk.Combobox(
        #     self.ventana, 
        #     width=10, 
        #     state="readonly",
        #     values=tuple(conectarMongo.diccionarioPyC().keys()))
        # self.provinciaEntry.place(x=250, y=50)
        # self.provinciaEntry.bind("<<ComboboxSelected>>", on_combobox_select1)

        # '''Menu despegable cantón que dependerá de las opciones de la ventana provincia'''
        # self.cantonEntry = ttk.Combobox(self.ventana, width=10, state="readonly")
        # self.cantonEntry.place(x=250, y=75)

        # '''Menú despegable donde mostrará la lista de generos a las que se puede elegir'''
        # self.generoEntry = ttk.Combobox(self.ventana, value= conectarMongo.listaGeneros(), width=8, state="readonly")
        # self.generoEntry.place(x=250, y=1)

        # '''Menú despegable donde mostrará la lista de estados a las que se puede elegir'''
        # self.estadoEntry = ttk.Combobox(self.ventana, value= conectarMongo.estadosUsuarios(), width=15, state="readonly")
        # self.estadoEntry.place(x=400, y=50)

        # '''Menú despegable donde mostrará la lista de roles a las que se puede elegir'''
        # self.rolEntry = ttk.Combobox(self.ventana, value= conectarMongo.mostrarRoles(), width=10, state="readonly")
        # self.rolEntry.place(x=560, y=75)

        # '''Menú despegable donde mostrará la lista de beneficiarios a las que se puede elegir'''
        # self.beneficarioEntry = ttk.Combobox(self.ventana, value= conectarMongo.beneficariosUsuarios(), width=10, state="readonly")
        # self.beneficarioEntry.place(x=720, y=75)
        
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
        listaEntidadProvincia = conectarMongo.entidadProvincia.find()
        
        for listaEntidadProvincia in conectarMongo.entidadProvincia.find():
            '''
            Bucle donde se van a insertar todos los datos que existen en la base de datos
            dentro de la tabla.
            '''
            #Insertamos datos
            self.tablaDatos.insert("", END, text = (listaEntidadProvincia["PROV_COD"]), values=( 
            listaEntidadProvincia["PROV_DESC"],
            listaEntidadProvincia["PROV_TAMA"],
            listaEntidadProvincia["PROV_HAB"],
            listaEntidadProvincia["PROV_HOMBRES"],
            listaEntidadProvincia["PROV_MUJERES"],
            listaEntidadProvincia["PROV_PREFECTO"],
            listaEntidadProvincia["PROV_FECHA"],
            ))
            
    def actualizarTabla (self):
        '''
        Actualización de datos dentro de la tabla
        '''
        getDatos(
                self.PROV_COD.get(),
                self.PROV_DESC.get(),
                self.PROV_TAMA.get(),
                self.PROV_HAB.get(),
                self.provinciaEntry.get(),
                self.cantonEntry.get(),
                self.PROV_HOMBRES.get(),
                self.PROV_MUJERES.get(),
                self.generoEntry.get(),
                self.estadoEntry.get(),
                self.PROV_PREFECTO.get(),
                self.PROV_FECHA.get(),
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
        listaEntidadProvincia = conectarMongo.coleccionPersonas.find()
        specificFind = conectarMongo.coleccionPersonas.find(query)

        for listaEntidadProvincia in specificFind:
            '''
            Bucle donde se van a insertar todos los datos que existen en la base de datos
            dentro de la tabla.
            '''
            #Insertamos datos
            self.tablaDatos.insert("", END, text = (listaEntidadProvincia["cedula"]), values=(listaEntidadProvincia["nombre"], 
            listaEntidadProvincia["nombre2"],
            listaEntidadProvincia["apellido"],
            listaEntidadProvincia["apellido2"],
            listaEntidadProvincia["provincia"],
            listaEntidadProvincia["canton"],
            listaEntidadProvincia["genero"],
            listaEntidadProvincia["estado"],
            listaEntidadProvincia["rol"],
            listaEntidadProvincia["PROV_PREFECTO"],
            listaEntidadProvincia["hijos"],
            listaEntidadProvincia["beneficiario"]
            ))
        
    def editarDatos(self):
        self.ventaneEditar = tk.Toplevel()
        self.ventaneEditar.title("Datos")
        self.ventaneEditar.geometry("300x300")
        self.ventaneEditar.resizable(width="False", height="False")


def getDatos (nombre, nombre2, apellido, apellido2, provincia, canton, cedula, edad, genero, estado, PROV_PREFECTO, hijos, rol, beneficario):
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
                                        if validarCorreoRE(PROV_PREFECTO): #Validar correo electrónico
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
                                                                'PROV_PREFECTO': PROV_PREFECTO,
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