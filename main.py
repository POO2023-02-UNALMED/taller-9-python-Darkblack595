from tkinter import Tk, Button, Entry,END

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("265x252")

# Configuración pantalla de salida 
pantalla = Entry(root, width=20, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=2)

# Configuración botones
boton_1 = Button(root, text="1", width=6, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda : botones(1)).grid(row=1, column=0, padx=1, pady=1,sticky ="nsew")
boton_2 = Button(root, text="2", width=6, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda : botones(2)).grid(row=1, column=1, padx=1, pady=1,sticky ="nsew")
boton_3 = Button(root, text="3", width=6, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda : botones(3)).grid(row=1, column=2, padx=1, pady=1,sticky ="nsew")
boton_4 = Button(root, text="4", width=6, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda : botones(4)).grid(row=2, column=0, padx=1, pady=1,sticky ="nsew")
boton_5 = Button(root, text="5", width=6, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda : botones(5)).grid(row=2, column=1, padx=1, pady=1,sticky ="nsew")
boton_6 = Button(root, text="6", width=6, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda : botones(6)).grid(row=2, column=2, padx=1, pady=1,sticky ="nsew")
boton_7 = Button(root, text="7", width=6, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda : botones(7)).grid(row=3, column=0, padx=1, pady=1,sticky ="nsew")
boton_8 = Button(root, text="8", width=6, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda : botones(8)).grid(row=3, column=1, padx=1, pady=1,sticky ="nsew")
boton_9 = Button(root, text="9", width=6, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda : botones(9)).grid(row=3, column=2, padx=1, pady=1,sticky ="nsew")
boton_igual = Button(root, text="=", width=9, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2",command=lambda : resultado()).grid(row=4, column=0, columnspan=2, padx=1, pady=1,sticky ="nsew")
boton_punto = Button(root, text=".", width=6, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0,command=lambda : botones(".")).grid(row=4, column=2, padx=1, pady=1,sticky ="nsew")
boton_mas = Button(root, text="+", width=6, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda : botones("+")).grid(row=1, column=3, padx=1, pady=1,sticky ="nsew")
boton_menos = Button(root, text="-", width=6, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda : botones("-")).grid(row=2, column=3, padx=1, pady=1,sticky ="nsew")
boton_multiplicacion = Button(root, text="*",  width=6, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda : botones("*")).grid(row=3, column=3, padx=1, pady=1,sticky ="nsew")
boton_division = Button(root, text="/", width=6, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda : botones("/")).grid(row=4, column=3, padx=1, pady=1,sticky ="nsew")

x = 0
def botones(num):
    global x
    pantalla.insert(x,num)
    x += 1

def resultado():
    operacion = pantalla.get()
    resultado = eval(operacion)
    pantalla.delete(0,END)
    pantalla.insert(0,resultado)
    x = 0

root.mainloop()