# importamos csv para utilizar archivos csv (excel)
import csv
# importamos tkinter para utilizar interfaz grafica
from tkinter import messagebox,Tk,Button,Label,Entry
# importamos os.path para utilizar una ruta de archivos a trabajar en el codigo
import os.path
# importamos functools para que los botones de la interfaz tengan capacidad de enviar parametros
from functools import partial
# importamos tempfile para utilizar archivos temporales (sobreescritura)
from tempfile import NamedTemporaryFile
import shutil
file_exists = os.path.isfile("GestionUsuarios.csv")
headers = ['usuario', 'password']


# Función para mostrar ventana principal
def VentanaP():
    # Variable global para utilizarla en otras funciones del programa
    global ventanaPrincipal
    ventanaPrincipal = Tk()
    # Se establece estos parametros para establecer una posicion de despliegue a la ventana
    width = 600
    height = 220
    eje_x = ventanaPrincipal.winfo_screenwidth() // 2 - width // 2
    eje_y = ventanaPrincipal.winfo_screenheight() // 2 - height // 2
    posicion = str(width) + "x" + str(height) + "+" + str(eje_x) + "+" + str(eje_y)
    ventanaPrincipal.geometry(posicion)
    
    ventanaPrincipal.configure(bg="#B7B5C6")
    ventanaPrincipal.title("¡Aplicacion de registro en excel!")
    
    # BOTONES DE FUNCIONES DEL PROGRAMA
    button1 = Button(ventanaPrincipal,text="Registrar Usuario",command=Ventana1)
    button1.pack()
    button1.configure(width=22,fg="black",bg="#9DEEEC")
    button1.place(x=60, y=30)

    button2 = Button(ventanaPrincipal,text="Modificar usuario/contraseña",command=Ventana2)
    button2.pack()
    button2.configure(width=22,fg="black",bg="#9DEEEC")
    button2.place(x=310, y=70)

    button3 = Button(ventanaPrincipal,text="Limpiar Excel",command=Ventana5)
    button3.pack()
    button3.configure(width=20,fg="black",bg="#9DEEEC")
    button3.place(x=140, y=70)

    button4 = Button(ventanaPrincipal,text="Borrar usuario",command=Ventana3)
    button4.pack()
    button4.configure(width=22,fg="black",bg="#9DEEEC")
    button4.place(x=390, y=30)

    button5 = Button(ventanaPrincipal,text="Salir del programa",command=ventanaPrincipal.destroy)
    button5.pack()
    button5.configure(width=20,fg="black",bg="#9DEEEC")
    button5.place(x=225, y=110)

    button6 = Button(ventanaPrincipal,text="Iniciar sesión",command=Ventana4)
    button6.pack()
    button6.configure(width=22,fg="black",bg="#9DEEEC")
    button6.place(x=225, y=30)

    lblbienvenida = Label(ventanaPrincipal)
    lblbienvenida.pack()
    lblbienvenida.configure(font=("Courier", 16, "italic"),bg="#B7B5C6",text="BIENVENIDO!!! \n AL SISTEMA DE REGISTRO EN ARCHIVOS DE EXCEL")
    lblbienvenida.place(x=0, y=160)

    ventanaPrincipal.mainloop()



# formato al archivo excel(csv) usuario y password, ademas darle un formato de escritura en el archivo csv
with open ("GestionUsuarios.csv", 'a') as csvfile:
    writer = csv.DictWriter(csvfile, delimiter=';', lineterminator='\n',fieldnames=headers)

    # si no existe el archivo se vuelve a darle un formato y se limpia dejando solo la cabezera o headers( usuario , password)
    if not file_exists:
        writer.writeheader()

def Registro(CajaTextoUsuario,CajaTextoPassword):
    # Rescata las cajas de texto de la ventana1 "CajaTextoUsuario y CajaTextoPassword"
    # Se rescatan las cajas de texto en las variables locales (usuario, contrasenia)
    usuario = CajaTextoUsuario.get()
    contrasenia = CajaTextoPassword.get()
    validado = ExisteUsuario(usuario)
    if validado == 1:
        # Si el usuario no existe existe en excel retorna 1
        # user y passw son variables locales por lo cual los parametros de las cajas de texto se rescatan en ellas (user = usuario, passw = contrasenia)
        user = usuario
        passw = contrasenia
        # la funcion witcontraseniah open es para abrir el archivo CSV que se esta registrando.
        if len(user) >= 4 and len(passw) >=4:
            with open ("GestionUsuarios.csv","a") as file:
                # esta funcion es para establecer el formato de registro que sea separado por (;) y (\n) para que tome un espacio a la linea de abajo
                escribe=csv.DictWriter(file,delimiter=";",lineterminator='\n',fieldnames=headers)
                # aqui se escriben los parametros enviados user y pssw en el archivo CSV.
                escribe.writerow({'usuario': user,'password':passw})
            # y se envia un mensaje de registro exitoso del usuario.
            messagebox.showinfo("Registro exitoso","Bienvenido usuario: "+usuario)
            CerrarVentanaRegistro()
            VentanaP()
        # restriccion de usuario mayor a 4 caracteres
        elif len(user) <4:
            messagebox.showwarning("Error","debe ingresar un usuario con minimo 4 caracteres.")
        # restriccion de password mayor a 4 caracteres
        elif len(passw) <4:
            messagebox.showwarning("Error","debe ingresar una contraseña con minimo 4 caracteres.")
        # user vacio
        elif user == '':
            messagebox.showwarning("Error","debe ingresar un usuario.")
        # contraseña vacia
        elif passw == '':
            messagebox.showwarning("Error","debe ingresar una contraseña.")
         

    # ya existe el usuario en el excel
    elif validado == -1:
        messagebox.showwarning("Error","Ingrese un usuario diferente a: "+usuario)
    else:
        messagebox.showwarning("Error","debe ingresar un usuario y contraseña.")
    
# Ventana registro
def Ventana1():
    # cerrar ventana principal
    ventanaPrincipal.withdraw()
    # se establece la RegistroVentana como variable global para utilizarla en otras funciones.
    global RegistroVentana
    
    # ventana tkinter
    RegistroVentana = Tk()
    RegistroVentana.title("Registro de usuario")
    RegistroVentana.configure(bg="#B7B5C6")
    width = 500
    height = 300

    EtiquetaRegistro = Label(RegistroVentana)
    EtiquetaRegistro.pack()
    EtiquetaRegistro.configure(font=("Courier", 14, "italic"),bg="#B7B5C6",text="Registro de usuario")
    EtiquetaRegistro.place(x=150, y=0)

    eje_x = RegistroVentana.winfo_screenwidth() // 2 - width // 2
    eje_y = RegistroVentana.winfo_screenheight() // 2 - height // 2

    posicion = str(width) + "x" + str(height) + "+" + str(eje_x) + "+" + str(eje_y)
    RegistroVentana.geometry(posicion)

    Etiqueta1 = Label(RegistroVentana, text="Ingresa nuevo Usuario",bg="#B7B5C6")
    Etiqueta1.pack()
    Etiqueta1.place(x=145, y=70)

    CajaTextoUsuario = Entry(RegistroVentana,width=23)
    CajaTextoUsuario.pack()
    CajaTextoUsuario.place(x=150, y=100)

    Etiqueta2 = Label(RegistroVentana, text="Ingresa nueva Contraseña",bg="#B7B5C6")
    Etiqueta2.pack()
    Etiqueta2.place(x=145, y=130)

    CajaTextoPassword = Entry(RegistroVentana,width=23)
    CajaTextoPassword.pack()
    CajaTextoPassword.place(x=150, y=160)

    button = Button(RegistroVentana,text="Registrar Usuario",fg="black",bg="#49E3B7",width=15,command=partial(Registro,CajaTextoUsuario,CajaTextoPassword))
    button.pack()
    button.place(x=300, y=100)

    button1 = Button(RegistroVentana,text="Volver",fg="black",bg="#49E3B7",width=15,command=CerrarVentanaRegistro)
    button1.pack()
    button1.place(x=300, y=160)
    RegistroVentana.mainloop()
            
def CerrarVentanaRegistro():
    RegistroVentana.destroy()
    VentanaP()

            
# funcion para validar si existe el usuario que se utiliza en Registro.
def ExisteUsuario(user):
    # este metodo sirve leer el archivo csv excel y se define que se lee con separador ; y \n que es un salto de espacio hacia abajo
    csv_file = csv.DictReader(open('GestionUsuarios.csv', "r"), delimiter=";",lineterminator='\n',fieldnames=headers)
    for row in csv_file:
        if user == row["usuario"]:
            return -1
    return 1

# funcion para validar si los parametros enviados de user y password desde la ventana de inicio de sesion.
def VerificarUsuario(user, password):
    # este metodo sirve para abrir y leer el archivo excel, con formato de lectura, y busca el parametro user y password para el inicio de sesion
    csv_file = csv.DictReader(open('GestionUsuarios.csv', "r"), delimiter=";",lineterminator='\n',fieldnames=headers)
    for row in csv_file:
        if user == row["usuario"] and password == row["password"]:
             # si retorna -1 es por que ya existe el usuario.
            return 1
    # si retorna 1 es por el usuario no existe en el archivo excel.
    return -1
# Ventana modificar usuario
def Ventana2():
    # cerrar ventana principal
    ventanaPrincipal.withdraw()
    # se establece la ventanaModificar como global para utilizarla en otras funciones.
    global VentanaModificar

    # ventana tkinter
    VentanaModificar = Tk()
    VentanaModificar.title("Modificar Usuario")
    VentanaModificar.configure(bg="#B7B5C6")

    #Se establece estos parametros para establecer una posicion de despliegue a la ventana
    width = 500
    height = 300
    eje_x = VentanaModificar.winfo_screenwidth() // 2 - width // 2
    eje_y = VentanaModificar.winfo_screenheight() // 2 - height // 2
    posicion = str(width) + "x" + str(height) + "+" + str(eje_x) + "+" + str(eje_y)
    VentanaModificar.geometry(posicion)
    
    # Etiquetas,Cajas de texto y botones
    EtiquetaVentanaModificar = Label(VentanaModificar)
    EtiquetaVentanaModificar.pack()
    EtiquetaVentanaModificar.configure(font=("Courier", 14, "italic"),bg="#B7B5C6",text="Modificar Usuario")
    EtiquetaVentanaModificar.place(x=150, y=0)

    
    EtiquetaUsuario = Label(VentanaModificar)
    EtiquetaUsuario.pack()
    EtiquetaUsuario.configure(text="Usuario a modificar",bg="#B7B5C6")
    EtiquetaUsuario.place(x=150, y=50)

    CajaTextoUsuario = Entry(VentanaModificar)
    CajaTextoUsuario.pack()
    CajaTextoUsuario.configure(width=23)
    CajaTextoUsuario.place(x=150, y=80)

    EtiquetaNuevoUsuario = Label(VentanaModificar)
    EtiquetaNuevoUsuario.pack()
    EtiquetaNuevoUsuario.configure(text="Nuevo Usuario",bg="#B7B5C6")
    EtiquetaNuevoUsuario.place(x=150, y=110)

    CajaTextoNuevoUsuario = Entry(VentanaModificar)
    CajaTextoNuevoUsuario.pack()
    CajaTextoNuevoUsuario.configure(width=23)
    CajaTextoNuevoUsuario.place(x=150, y=140)

    EtiquetaNuevaContrasenia = Label(VentanaModificar, text="Nueva Contraseña",bg="#B7B5C6")
    EtiquetaNuevaContrasenia.pack()
    EtiquetaNuevaContrasenia.place(x=150,y=170)

    CajaTextoNuevaContrasenia = Entry(VentanaModificar,width=23)
    CajaTextoNuevaContrasenia.pack()
    CajaTextoNuevaContrasenia.place(x=150,y=200)

    # boton de inicio de sesion, este boton envia los parametros de CajaTextoUsuario, CajaTextoNuevoUsuario y CajaTextoNuevaContraseña.
    button = Button(VentanaModificar,text="Actualizar Usuario",fg="black",bg="#49E3B7",command=partial(ModificarUsuario,CajaTextoUsuario,CajaTextoNuevoUsuario,CajaTextoNuevaContrasenia))
    button.pack()
    button.place(x=300, y=140)

    # boton volver que llama la funcion CerrarVentanaModificar.
    button1 = Button(VentanaModificar,text="Volver",fg="black",bg="#49E3B7",command=CerrarVentanaModificar)
    button1.pack()
    button1.place(x=300, y=200)

    VentanaModificar.mainloop()

def CerrarVentanaModificar():
    VentanaModificar.destroy()
    VentanaP()    

# se reciben parametros desde la ventana2 la cual es modificar usuario, se reciben (CajaTextoUsuario,CajaTextoNuevoUsuario,CajaTextoNuevaContrasenia)
def ModificarUsuario(CajaTextoUsuario,CajaTextoNuevoUsuario,CajaTextoNuevaContrasenia):
    # Rescata el parametro CajaTextoUsuario de la caja de texto de la ventana2 modificar en la variable Usuario
    Usuario = CajaTextoUsuario.get()
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    # se abre el archivo excel se lee y se escribe con los formatos (;) como separador y (\n) como espacio para abajo
    with open("GestionUsuarios.csv", 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile,delimiter=";",lineterminator='\n', fieldnames=headers)
        writer = csv.DictWriter(tempfile,delimiter=";",lineterminator='\n', fieldnames=headers)
        for row in reader:
            # si el user ingresado esta en al fila de usuario del archivo csv.
            if row['usuario'] == str(Usuario):
                print('updating row ', row['usuario'])
                # se captura de las cajas de texto ingresadas las variables CajaTextoNuevoUsuario,CajaTextoNuevaContrasenia como newuser y newpass
                nuevoUsuario = CajaTextoNuevoUsuario.get()
                nuevaContrasenia = CajaTextoNuevaContrasenia.get()
                # si el nuevoUsuario es diferente a campo en blanco se busca el campo usuario y se agrega el newuser a la fila(row)
                if nuevoUsuario.strip() != "":
                    row["usuario"] = nuevoUsuario
                # si el nuevaContrasenia es diferente a campo en blanco se busca el campo usuario y se agrega el newpass a la fila(row)
                if nuevaContrasenia.strip() != "":
                    row["password"] = nuevaContrasenia
            row = {'usuario': row['usuario'], 'password': row['password']}
            # funcion para escribir en el excel
            writer.writerow(row)     
    # editar el archivo temporal de GestionUsuarios.csv  
    shutil.move(tempfile.name, "GestionUsuarios.csv")
    # mensaje de metodo exitoso
    messagebox.showinfo("Editar","Usuario Modificado: "+Usuario)

# ventana borrar usuario
def Ventana3():
    # cerrar ventana principal
    ventanaPrincipal.withdraw()
    # se establece la VentanaBorrarUsuario como global para utilizarla en otras funciones.
    global VentanaBorrarUsuario
    # ventana tkinter
    VentanaBorrarUsuario = Tk()
    VentanaBorrarUsuario.title("Borrar Usuario")
    VentanaBorrarUsuario.configure(bg="#B7B5C6")

    #Se establece estos parametros para establecer una posicion de despliegue a la ventana
    ancho = 500
    alto = 200
    eje_x = VentanaBorrarUsuario.winfo_screenwidth() // 2 - ancho // 2
    eje_y = VentanaBorrarUsuario.winfo_screenheight() // 2 - alto // 2
    posicion = str(ancho) + "x" + str(alto) + "+" + str(eje_x) + "+" + str(eje_y)
    VentanaBorrarUsuario.geometry(posicion)

    #Etiquetas
    EtiquetaBorrarUsuario = Label(VentanaBorrarUsuario)
    EtiquetaBorrarUsuario.pack()
    EtiquetaBorrarUsuario.configure(font=("Courier", 14, "italic"),bg="#B7B5C6",text="Borrar Usuario existente")
    EtiquetaBorrarUsuario.place(x=130, y=0)

    Etiqueta1 = Label(VentanaBorrarUsuario, text="Ingrese usuario a eliminar",bg="#B7B5C6")
    Etiqueta1.pack()
    Etiqueta1.place(x=145, y=50)

    #Cajas de texto
    CajaTextoUsuarioEliminar = Entry(VentanaBorrarUsuario)
    CajaTextoUsuarioEliminar.pack()
    CajaTextoUsuarioEliminar.place(x=150, y=80)
    CajaTextoUsuarioEliminar.configure(width=23)

    # Boton de BorrarUsuario, este boton envia los parametros CajaTextoUsuarioEliminar para utilizarlos en la funcion
    button = Button(VentanaBorrarUsuario,text="Borrar Usuario",fg="black",bg="#49E3B7",command=partial(BorrarUsuario,CajaTextoUsuarioEliminar))
    button.pack()
    button.place(x=300, y=80)

    # Boton volver llama a la funcion cerrarVentanaBorrarUsuario
    button1 = Button(VentanaBorrarUsuario,text="Volver",fg="black",bg="#49E3B7",command=cerrarVentanaBorrarUsuario)
    button1.pack()
    button1.place(x=300, y=120)

    VentanaBorrarUsuario.mainloop()

# funcion eliminarUsuario que recibe como parametro tboxuserEliminar desde la ventana (funcion)eliminarventana
def BorrarUsuario(CajaTextoUsuarioEliminar):
    # se almacena la variable ingresada por la caja de texto tboxuserEliminar en la variable user
    user = CajaTextoUsuarioEliminar.get()
    lines = list()
    # se abre el archivo csv se lee y se escribe con los formatos (;) como separador y (\n) como espacio para abajo
    with open('GestionUsuarios.csv', 'r') as read_file:
        reader = csv.DictReader(open('GestionUsuarios.csv', "r"), delimiter=";",lineterminator='\n',fieldnames=headers)
        for row in reader:
            # si el usuario es diferente de user se limpia la lista lines en la fila
            if row["usuario"] != user:
                lines.append(row)
        messagebox.showinfo("se elimino el","Usuario: "+user)
    # se abre el archivo csv y se le vuelve a dar el formato en luego de haber limpiado la linea.
    with open('GestionUsuarios.csv', 'w') as write_file:
        writer = csv.DictWriter(write_file,delimiter=";",lineterminator='\n',fieldnames=headers)
        writer.writerows(lines)

# Funcion para mantener una sola ventana abierta
def cerrarVentanaBorrarUsuario():
    VentanaBorrarUsuario.destroy()
    VentanaP()

# Funcion inicio de sesion
def Ventana4():
    # cerrar ventana principal
    ventanaPrincipal.withdraw()
    # se establece la ventanaLog (ventana de inicio de sesion) como global para utilizarla en otras variables o funciones.
    global ventanaInicioSesion
    
    # ventana tkinter
    ventanaInicioSesion = Tk()
    ventanaInicioSesion.title("Bienvenido al inicio de sesion")
    ventanaInicioSesion.configure(bg="#B7B5C6")
    ventanaInicioSesion.geometry("500x300")
    width = 500
    height = 300

    eje_x = ventanaInicioSesion.winfo_screenwidth() // 2 - width // 2
    eje_y = ventanaInicioSesion.winfo_screenheight() // 2 - height // 2

    posicion = str(width) + "x" + str(height) + "+" + str(eje_x) + "+" + str(eje_y)
    ventanaInicioSesion.geometry(posicion)

    EtiquetaInicioSesion = Label(ventanaInicioSesion)
    EtiquetaInicioSesion.pack()
    EtiquetaInicioSesion.configure(font=("Courier", 14, "italic"),bg="#B7B5C6",text="Inicio de Sesión")
    EtiquetaInicioSesion.place(x=150, y=0)

    # Etiquetas y cajas de texto de tkinter
    EtiquetaUsuario = Label(ventanaInicioSesion, text="Usuario",bg="#B7B5C6")
    EtiquetaUsuario.pack()
    EtiquetaUsuario.place(x=145, y=70)

    CajaTextoUsuario = Entry(ventanaInicioSesion,width=23)
    CajaTextoUsuario.pack()
    CajaTextoUsuario.place(x=150, y=100)

    EtiquetaContrasenia = Label(ventanaInicioSesion, text="Contraseña",bg="#B7B5C6")
    EtiquetaContrasenia.pack()
    EtiquetaContrasenia.place(x=145, y=130)

    CajaTextoContrasenia = Entry(ventanaInicioSesion,width=23)
    CajaTextoContrasenia.pack()
    CajaTextoContrasenia.place(x=150, y=150)

    # boton de Iniciar Sesion que envia parametros "CajaTextoUsuario y CajaTextoContrasenia" a funcion InicioSesion
    button = Button(ventanaInicioSesion,text="Iniciar sesion",fg="black",bg="#49E3B7", command=partial(InicioSesion,CajaTextoUsuario,CajaTextoContrasenia))
    button.pack()
    button.place(x=300, y=100)

    # Boton volver llama a la funcion cerrarVentanaInicioSesion para cerrar la ventana inicio de sesion
    button1 = Button(ventanaInicioSesion,text="Volver",fg="black",bg="#49E3B7",command=CerrarVentanaInicioSesion)
    button1.pack()
    button1.place(x=300, y=150)
    ventanaInicioSesion.mainloop()

# funcion InicioSesion que rescata como parametro CajaTextoUsuario,CajaTextoContrasenia, vienen de la ventana inicio de sesion.
def InicioSesion(CajaTextoUsuario,CajaTextoContrasenia):
    # las variables recibidas por parametro las convertimos en variables locales para usarlas en estta funcion (user,pswd)
    user = CajaTextoUsuario.get()
    passw = CajaTextoContrasenia.get()
    # se utiliza la funcion buscar usuario para validar que el user y pswd existen en el archivo CSV, se utiliza la funcion buscar usuario para validar si existe.
    validado = VerificarUsuario(user,passw)
    if validado == 1:
        messagebox.showinfo("Bienvenido!","usuario: "+user)
        CerrarVentanaInicioSesion()
        VentanaP()
    elif user == '':
        messagebox.showwarning("Error","Debe ingresar un usuario")
    elif passw == '':
        messagebox.showwarning("Error","Debe ingresar una contraseña") 
    else:
        messagebox.showwarning("¡Error!","usuario y/o contraseña invalida")

def CerrarVentanaInicioSesion():
    ventanaInicioSesion.destroy()
    VentanaP()


# Funcion para borrar los datos del excel
def Ventana5():
    # se define como global la ventana para utilizarla en otras funciones
    global VentanaBorrarDatos
    #Ventana Tkinter
    VentanaBorrarDatos = Tk()
    VentanaBorrarDatos.title("")
    VentanaBorrarDatos.configure(bg="#B7B5C6")

    #Se establece estos parametros para establecer una posicion de despliegue a la ventana
    ancho = 200
    alto = 200
    eje_x = VentanaBorrarDatos.winfo_screenwidth() // 2 - ancho // 2
    eje_y = VentanaBorrarDatos.winfo_screenheight() // 2 - alto // 2
    posicion = str(ancho) + "x" + str(alto) + "+" + str(eje_x) + "+" + str(eje_y)
    VentanaBorrarDatos.geometry(posicion)

    #Etiquetas
    EtiquetaBorrarDatos = Label(VentanaBorrarDatos)
    EtiquetaBorrarDatos.pack()
    EtiquetaBorrarDatos.configure(font=("Courier", 14, "italic"),bg="#B7B5C6",text="¿Esta seguro?")
    EtiquetaBorrarDatos.place(x=30, y=0)

    #Botones
    button = Button(VentanaBorrarDatos,text="Si",fg="black",bg="red",width=6,command=BorrarDatos)
    button.pack()
    button.place(x=80, y=60)

    button1 = Button(VentanaBorrarDatos,text="No",fg="black",bg="yellow",width=6,command=cerrarVentanaBorrarDatos)
    button1.pack()
    button1.place(x=80, y=120)

def cerrarVentanaBorrarDatos():
    VentanaBorrarDatos.destroy()

def BorrarDatos():
    # se abre el archivo excel sobreescribe writeheader(para limpiar el excel y escribir los encabezados)
    with open ("GestionUsuarios.csv", 'w') as csvfile:
        messagebox.showinfo("ATENCION","se han eliminado los datos")
        writer = csv.DictWriter(csvfile, delimiter=';', lineterminator='\n',fieldnames=headers)
        writer.writeheader()
    VentanaBorrarDatos.destroy()    
        
# INICIAR VENTANA PRINCIPAL
VentanaP()