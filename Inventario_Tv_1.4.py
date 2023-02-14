from tkinter import ttk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


import pymysql
import os


pnt =Tk()
pnt.title("Registro de inventario Tv")


wtotal = pnt.winfo_screenwidth()
htotal = pnt.winfo_screenheight()
wventana = 515
hventana = 200



ID_SERIE = StringVar()
MARCA = StringVar()
MODELO = StringVar()
TECNOLOGIA = StringVar()
PULGADAS = StringVar()
RESOLUCION = StringVar()
SMART_TV = StringVar()
ROKU = StringVar()
CANTIDAD = StringVar()
PRECIO = StringVar()
PRECIO_VENTA = StringVar()



connectio = pymysql.connect(
    host='localhost',
    user='root',
    password='basededatos',
    db='TELEVISIONES'
)
def validate_entry(text):
    return text.isdecimal()
class App:
   
    def imprimir():
        if ID_SERIE.get() =="" or MARCA.get() =="" or MODELO.get()=="" or TECNOLOGIA.get()=="" or PULGADAS.get()=="" or RESOLUCION.get()=="" or SMART_TV.get()=="" or ROKU.get()=="" or CANTIDAD.get()=="" or PRECIO.get()=="":
            messagebox.showinfo(message="Existen espacios vacios")
        else:
            cursor = connectio.cursor()
            A =float(PRECIO.get())
            b =A + 700
            cantidad_tv= float(CANTIDAD.get())
            precio_tv = float(PRECIO.get())
            total = cantidad_tv * precio_tv
            sql ="insert into INVENTARIOTV(ID_SERIE,MARCA,MODELO,TECNOLOGIA,PULGADAS,RESOLUCION,SMART_TV,ROKU,CANTIDAD,PRECIO,PRECIO_DE_VENTA,VALOR_TOTAL_MERCANCIA) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format("SNTV00" + ID_SERIE.get(),MARCA.get(),MODELO.get(),TECNOLOGIA.get(),PULGADAS.get(),RESOLUCION.get(),SMART_TV.get(),ROKU.get(),CANTIDAD.get(),PRECIO.get(),b,total)
            cursor.execute(sql)
            connectio.commit()
            messagebox.showinfo(message="Elementos enviados",title="Estado de ingreso de datos")
            aplicacion.limpiar()
    def limpiar():
        ID_SERIE_ENTRY.delete(0,END)
        MARCA_C.delete(0,END)
        MODELO_ENTRY.delete(0,END)
        TECNOLOGIA_C.delete(0,END)
        PULGADAS_ENTRY.delete(0,END)
        RESOLUCION_C.delete(0,END)
        SMART_TV_C.delete(0,END)
        ROKU_C.delete(0,END)
        CANTIDAD_ENTRY.delete(0,END)
        PRECIO_ENTRY.delete(0,END)
    def Actualizar(str):
        ID_SERIE_ENTRY.delete(0,END)
        MARCA_C.delete(0,END)
        MODELO_ENTRY.delete(0,END)
        TECNOLOGIA_C.delete(0,END)
        PULGADAS_ENTRY.delete(0,END)
        RESOLUCION_C.delete(0,END)
        SMART_TV_C.delete(0,END)
        ROKU_C.delete(0,END)
        CANTIDAD_ENTRY.delete(0,END)
        PRECIO_ENTRY.delete(0,END)
        pass
    def mensje(self):
     
        global ID_SERIE_ENTRY
        global MARCA_C
        global MODELO_ENTRY
        global TECNOLOGIA_C
        global PULGADAS_ENTRY
        global RESOLUCION_C
        global SMART_TV_C
        global ROKU_C
        global CANTIDAD_ENTRY
        global PRECIO_ENTRY
        ID_SERIE_ENTRY = Entry(validate="key",validatecommand=(pnt.register(validate_entry),"%S"),textvariable=ID_SERIE,font=('Bahnschrift',10))
        ID_SERIE_ENTRY.grid(row=1,column=3)
        MARCA_C = ttk.Combobox(pnt,values =["ONN","TCL","HISENSE","RCA","LG","JVC","SPECTER","WESTINGHOUSE"],width=17,textvariable=MARCA,font=('Bahnschrift',10))
        MARCA_C.grid(row=2,column=3)
        MODELO_ENTRY = Entry(pnt,textvariable=MODELO,font=('Bahnschrift',10))
        MODELO_ENTRY.grid(row=2,column=15)
        TECNOLOGIA_C = ttk.Combobox(pnt,values=["LED","QLED","OLED"],width=17,textvariable=TECNOLOGIA,font=('Bahnschrift',10))
        TECNOLOGIA_C.grid(row=4,column=3)
        PULGADAS_ENTRY = Entry(pnt,textvariable=PULGADAS,font=('Bahnschrift',10))
        PULGADAS_ENTRY.grid(row=5,column=3)
        RESOLUCION_C = ttk.Combobox(pnt,values=["720P","1080P","2K","4K"],width=17,textvariable=RESOLUCION,font=('Bahnschrift',10))
        RESOLUCION_C.grid(row=5,column=15)
        SMART_TV_C= ttk.Combobox(pnt,values=["SI","NO"],width=17,textvariable=SMART_TV,font=('Bahnschrift',10))
        SMART_TV_C.grid(row=7,column=3)
        ROKU_C = ttk.Combobox(pnt,values=["SI","NO"],width=17,textvariable=ROKU,font=('Bahnschrift',10))
        ROKU_C.grid(row=7,column=15)
        CANTIDAD_ENTRY = Entry(validate="key",validatecommand=(pnt.register(validate_entry),"%S"),textvariable=CANTIDAD,font=('Bahnschrift',10))
        CANTIDAD_ENTRY.grid(row=9,column=3)
        PRECIO_ENTRY = Entry(pnt,textvariable=PRECIO,font=('Bahnschrift',10))
        PRECIO_ENTRY.grid(row=10,column=3)

        global LABEL_ID_SERIE
        global LABEL_MARCA
        global LABEL_MODELO
        global LABEL_TECNOLOGIA
        global LABEL_PULGADAS
        global LABEL_RESOLUCION
        global LABEL_SMART_TV
        global LABEL_ROKU
        global LABEL_CANTIDAD
        global LABEL_PRECIO
        
        LABEL_ID_SERIE = Label(pnt,text="ID_SERIE: ",font=('Bahnschrift',10))
        LABEL_ID_SERIE.grid(row=1,column=2)
        LABEL_MARCA = Label(pnt,text="MARCA: ",font=('Bahnschrift',10))
        LABEL_MARCA.grid(row=2,column=2)
        LABEL_MODELO = Label(pnt,text="MODELO: ",font=('Bahnschrift',10))
        LABEL_MODELO.grid(row=2,column=10)
        LABEL_TECNOLOGIA = Label(pnt,text="TECNOLOGIA: ",font=('Bahnschrift',10))
        LABEL_TECNOLOGIA.grid(row=4,column=2)
        LABEL_PULGADAS = Label(pnt,text="PULGADAS: ",font=('Bahnschrift',10))
        LABEL_PULGADAS.grid(row=5,column=2)
        LABEL_RESOLUCION = Label(pnt,text="RESOLUCION: ",font=('Bahnschrift',10))
        LABEL_RESOLUCION.grid(row=5,column=10)
        LABEL_SMART_TV = Label(pnt,text="SMART_TV: ",font=('Bahnschrift',10))
        LABEL_SMART_TV.grid(row=7,column=2)
        LABEL_ROKU = Label(pnt,text="ROKU: ",font=('Bahnschrift',10))
        LABEL_ROKU.grid(row=7,column=10)
        LABEL_CANTIDAD = Label(pnt,text="CANTIDAD: ",font=('Bahnschrift',10))
        LABEL_CANTIDAD.grid(row=9,column=2)
        LABEL_PRECIO = Label(pnt,text="PRECIO POR UNIDAD: ",font=('Bahnschrift',10))
        LABEL_PRECIO.grid(row=10,column=2)
    global botonenviar
    botonenviar = Button(pnt,text="ENVIAR",command=imprimir)
    botonenviar.grid(row=12,column=10)
class ventana():
    def hola():
        print("hola")
        ventana.borra()
    def borra():
        ID_SERIE_ENTRY.destroy()
        MARCA_C.destroy()
        MODELO_ENTRY.destroy()
        TECNOLOGIA_C.destroy()
        PULGADAS_ENTRY.destroy()
        RESOLUCION_C.destroy()
        SMART_TV_C.destroy()
        ROKU_C.destroy()
        CANTIDAD_ENTRY.destroy()
        PRECIO_ENTRY.destroy()
        LABEL_ID_SERIE.destroy()
        LABEL_MARCA.destroy()
        LABEL_MODELO.destroy()
        LABEL_TECNOLOGIA.destroy()
        LABEL_PULGADAS.destroy()
        LABEL_RESOLUCION.destroy()
        LABEL_SMART_TV.destroy()
        LABEL_ROKU.destroy()
        LABEL_CANTIDAD.destroy()
        LABEL_PRECIO.destroy()
        botonenviar.destroy()
 
menubar = Menu(pnt)
pnt.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Actualizar tabla",command=ventana.hola)
menubar.add_cascade(label="Editar tabla", menu=filemenu)

   
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)

pnt.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

aplicacion =App()
aplicacion.mensje()
pnt.mainloop()
