from tkinter import *

raiz=Tk()
raiz.title("Andora")
#raiz.iconbitmap("logoico.ico")
raiz.config(bg="blue")
raiz.resizable(False,False)

miframe=Frame(raiz)
miframe.pack()
miframe.config(bg="blue")
miframe.config(cursor="hand2")



numeroPantalla=StringVar() 
Pantallacalcu=Entry(miframe, width=35, textvariable=numeroPantalla)
Pantallacalcu.grid(row=1, column=1, padx=0, pady=20, columnspan=4) 
Pantallacalcu.config(background="white", fg="black", justify="right")

#------------fila de botones numero 1------------------------------------------------------------------------------------
botonCE=Button(miframe, text="CE", width=5, height=2)
botonCE.config(bd=10)
botonCE.config(relief="groove")
botonCE.grid(row=2, column=1)

botonporciento=Button(miframe, text="%", width=5, height=2)
botonporciento.config(bd=10)
botonporciento.config(relief="groove")
botonporciento.grid(row=2, column=2)

botonpotencia=Button(miframe, text="x²", width=5, height=2)
botonpotencia.config(bd=10)
botonpotencia.config(relief="groove")
botonpotencia.grid(row=2, column=3)
 
botonraiz=Button(miframe, text="√", width=5, height=2)
botonraiz.config(bd=10)
botonraiz.config(relief="groove")
botonraiz.grid(row=2, column=4)

#------------fila de botones numero 2------------------------------------------------------------------------------------
boton7=Button(miframe, text="7", width=5, height=2)
boton7.config(bd=10)
boton7.config(relief="groove")
boton7.grid(row=3, column=1)

boton8=Button(miframe, text="8", width=5, height=2)
boton8.config(bd=10)
boton8.config(relief="groove")
boton8.grid(row=3, column=2)

boton9=Button(miframe, text="9", width=5, height=2)
boton9.config(bd=10)
boton9.config(relief="groove")
boton9.grid(row=3, column=3)
 
botondivi=Button(miframe, text="/", width=5, height=2)
botondivi.config(bd=10)
botondivi.config(relief="groove")
botondivi.grid(row=3, column=4)

#----------------fila de botones numero 3------------------------------------------------------------------------
boton6=Button(miframe, text="6", width=5, height=2)
boton6.config(bd=10)
boton6.config(relief="groove")
boton6.grid(row=4, column=3)

boton5=Button(miframe, text="5", width=5, height=2)
boton5.config(bd=10)
boton5.config(relief="groove")
boton5.grid(row=4, column=2)

boton4=Button(miframe, text="4", width=5, height=2)
boton4.config(bd=10)
boton4.config(relief="groove")
boton4.grid(row=4, column=1)
 
botonmulti=Button(miframe, text="x", width=5, height=2)
botonmulti.config(bd=10)
botonmulti.config(relief="groove")
botonmulti.grid(row=4, column=4)

#----------------fila de botones numero 4------------------------------------------------------------------------
boton3=Button(miframe, text="3", width=5, height=2)
boton3.config(bd=10)
boton3.config(relief="groove")
boton3.grid(row=5, column=3)

boton2=Button(miframe, text="2", width=5, height=2)
boton2.config(bd=10)
boton2.config(relief="groove")
boton2.grid(row=5, column=2)

boton1=Button(miframe, text="1", width=5, height=2)
boton1.config(bd=10)
boton1.config(relief="groove")
boton1.grid(row=5, column=1)
 
botonresta=Button(miframe, text="-", width=5, height=2)
botonresta.config(bd=10)
botonresta.config(relief="groove")
botonresta.grid(row=5, column=4)
#----------------fila de botones numero 5------------------------------------------------------------------------
botoncoma=Button(miframe, text=".", width=5, height=2)
botoncoma.config(bd=10)
botoncoma.config(relief="groove")
botoncoma.grid(row=6, column=1)

boton0=Button(miframe, text="0", width=5, height=2)
boton0.config(bd=10)
boton0.config(relief="groove")
boton0.grid(row=6, column=2)

botonigual=Button(miframe, text="=", width=5, height=2)
botonigual.config(bd=10)
botonigual.config(relief="groove")
botonigual.grid(row=6, column=3)
 
botonsuma=Button(miframe, text="+", width=5, height=2)
botonsuma.config(bd=10)
botonsuma.config(relief="groove")
botonsuma.grid(row=6, column=4)











raiz.mainloop()
