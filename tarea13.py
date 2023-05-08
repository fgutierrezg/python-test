import tkinter

window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

seleccionado = tkinter.StringVar(value=False)
r1 = tkinter.Radiobutton(window, text='Si', value='Si', variable=seleccionado)
r2 = tkinter.Radiobutton (window, text='No', value= 'No', variable=seleccionado)
r3 = tkinter.Radiobutton (window, text= 'Quizas',value= 'Quizas', variable=seleccionado)

r1.grid(column=0, row=1, pady=5, padx=5)
r2.grid(column=0, row=2, pady=5, padx=5)
r3.grid(column=0, row=3, pady=5, padx=5)

label_opcion = tkinter.Label(window,textvariable=seleccionado)

def resetear(event):
    seleccionado.set(value=False)

def obtener_valor():
    valor_seleccionado = seleccionado.cget('text')
    label_opcion.config(text=valor_seleccionado)

btn_reset = tkinter.Button(window, text="reiniciar")
btn_reset.bind('<Button-1>',resetear)

r1.bind('<Button-1>',obtener_valor)
r2.bind('<Button-1>',obtener_valor)
r3.bind('<Button-1>',obtener_valor)


label_opcion.grid(column=0, row=4, pady=5, padx=5)
btn_reset.grid(column=0, row=5, pady=5, padx=5)

window.mainloop() 