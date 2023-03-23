from tkinter import*
 
root= Tk()

ventanaprincipal=Frame(root,bg="#293133")
ventanaprincipal.grid()
contras=StringVar()
confirmo=StringVar()

def contraseñas():
    if contras.get()==confirmo.get():
        print("SESION INICIADA")
        ventanaprincipal.config(bg="#293133")
        

        
    else:
        print("CONTRASEÑA INCORRECTA")

#imagen

titulo=Label(ventanaprincipal,text="LOG IN", bg="#293133", fg="#fbfbfb",font=("Arial",20))
titulo.grid(row=3,column=1,columnspan=2)

NAME=Label(ventanaprincipal,text="NOMBRE:", bg="#4c1929", fg="#fbfbfb",font=("Arial",15)).grid(row=4,column=1,padx=30,pady=30)
textonombre=Entry(ventanaprincipal,font=("roboto",15)).grid(row=4,column=2,padx=15,pady=15)

CONTRA=Label(ventanaprincipal, bg="#4c1929", fg="#fbfbfb",text="CONTRASEÑA:",font=("Arial",15)).grid(row=5,column=1,padx=15,pady=30)
textocontra=Entry(ventanaprincipal,font=("roboto",15),textvariable=contras).grid(row=5,column=2,padx=30,pady=15)

CONFIRM=Label(ventanaprincipal, bg="#4c1929", fg="#fbfbfb",text="CONFIRMAR CONTRASEÑA:",font=("Arial",15)).grid(row=6,column=1,padx=15,pady=30)
textoconfir=Entry(ventanaprincipal,font=("roboto",15),textvariable=confirmo).grid(row=6,column=2,padx=30,pady=15)
control1=IntVar()

HOMBRE=Checkbutton(ventanaprincipal, text="HOMBRE",variable=control1, bg="#476087", fg="#fbfbfb",font=("Arial",15))
HOMBRE.grid(row=7,column=1)
control2=IntVar()

MUJER=Checkbutton(ventanaprincipal, text="MUJER",variable=control2, bg="#476087", fg="#fbfbfb",font=("Arial",15))
MUJER.grid(row=7,column=2)
control3=IntVar()

ACEPTO=Checkbutton(ventanaprincipal, text="ACEPTO TERMINOS",variable=control3, bg="#000000", fg="#fbfbfb",font=("Arial",15))
ACEPTO.grid(row=8,column=1,columnspan=2)

INICIAR=Button(ventanaprincipal,text="INICIAR",command=contraseñas,width=20,height=2).grid(row=9,column=1,columnspan=2)

root.mainloop()

