import tkinter

def actualizar_label(asd):
    # Obtener el índice del elemento seleccionado en el Listbox
    seleccion = listbox.curselection()

    # Si hay un elemento seleccionado, actualizar la etiqueta con su texto
    if seleccion:
        texto_seleccionado = listbox.get(seleccion[0])
        etiqueta.config(text=texto_seleccionado)
        print(texto_seleccionado)
    else:
        etiqueta.config(text="")


window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

lista = ['Car', 'Bus', 'train','Boat']
lista_items = tkinter.StringVar (value=lista)
listbox = tkinter.Listbox(window, height=10, listvariable=lista_items)
listbox.grid(column=0, row=0, sticky=tkinter.W)

etiqueta = tkinter.Label(window,text="Seleccione medio de transporte")
etiqueta.grid(column=0, row=1, pady=5, padx=5)

listbox.bind('<<ListboxSelect>>',actualizar_label)


window.mainloop() 