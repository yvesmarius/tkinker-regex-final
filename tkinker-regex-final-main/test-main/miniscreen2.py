

from cgitb import reset
from tkinter import *
import sys
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import Tk, ttk
from datetime import date
today=date.today()




def application():
    root1=Tk()
    root1.geometry('600x600')
    root1.resizable(width=False,height=False)
    
    canvas1= Canvas(root1,width=600,height=600)
    img = ImageTk.PhotoImage(Image.open('test-main/eye.jpeg'))  # PIL solution
    canvas1.img=img
    canvas1.create_image(0, 0, anchor=NW, image=img)
    canvas1.pack(fill=BOTH,expand=TRUE)

    label_jour=Label(root1,text='jours')
    label_jour.place(x=150,y=400)

    label_mois=Label(root1,text='mois')
    label_mois.place(x=280,y=400)

    label_années=Label(root1,text='années')
    label_années.place(x=400,y=400)

    Tjours=StringVar()
    Tlabel_jours=Entry(root1,textvariable=Tjours,width=10)
    Tlabel_jours.place(x=120,y=420)


    Tmois=StringVar()
    Tlabel_mois=Entry(root1,textvariable=Tmois,width=10)
    Tlabel_mois.place(x=250,y=420)

    Tannées=StringVar()
    Tlabel_années=Entry(root1,textvariable=Tannées,width=10)
    Tlabel_années.place(x=370,y=420)

    labelindicate=Label(root1,text='statut_age')
    labelindicate.place(x=250,y=500)

    labelindicateday=Label(root1,text='')
    labelindicateday.place(x=150,y=450)

    labelindicatemonth=Label(root1,text='')
    labelindicatemonth.place(x=280,y=450)

    labelindicateyear=Label(root1,text='')
    labelindicateyear.place(x=400,y=450)

    button_V=Button(root1,text='Validez',command=lambda:[calculator()])
    button_V.place(x=250,y=530)

    def blockfuntion():
        print('reset')
    
        
    def calculator():

        try:
            if Tannées.get()=='' or Tjours.get()=='' or Tannées.get()=='':
                messagebox.showerror(title=None, message='veuillez entrer des nombres', )
            else:        
                if Tannées.get() and Tjours.get() and Tannées.get():
                    if int(Tmois.get())>12 or int(Tjours.get())>31 or int(Tannées.get())>today.year:
                        labelindicate['bg']='red'
                        labelindicate['text']='Erreur'
                        messagebox.showerror(title=None, message='une des entrer est invalide', )
                        
                        if int(Tmois.get())>12:
                            labelindicatemonth['fg']='red'
                            labelindicatemonth['text']= 'invalide'  

                        if int(Tjours.get())>31:
                            labelindicateday['fg']='red'
                            labelindicateday['text']='invalide'
                            
                        if int(Tannées.get())>2022:
                            labelindicateyear['fg']='red'
                            labelindicateyear['text']='invalide'
                    else:    
                        
                        T_m=12 
                        t2=int(today.year)
                    
                        t1=int(Tannées.get())
                        t3=int(Tjours.get())
                        t4=int(Tmois.get())
                        calculate=t2 - t1
                        calculate2=T_m-t4+today.month
                        calculate3=T_m-t4-today.month
                        calculate4=t4+today.month
                        def call_labs():
                            labelindicate['text']=(f"vous avez {calculate} ans {calculate2} mois") 
                        def call_labs1():
                            labelindicate['text']=(f"vous avez {calculate} ans") 

                        def call_labs2():
                            labelindicate['text']=(f"vous avez {calculate} ans {calculate2} mois")
                        def call_labs3():
                            labelindicate['text']=(f"vous avez {calculate} ans {calculate4} mois")
                        if t3>today.day:
                            calculate=(t2 - t1)-1
                            call_labs()
                
                        if t4>today.month:
                            calculate=(t2 - t1)-1               
                            call_labs()

                        if t3==today.day and t4==today.month:
                            calculate=(t2 - t1)
                            call_labs1()

                        if t3<today.day or t4<today.month:
                            calculate=(t2 - t1)-1 
                            call_labs3()

                        if t3<today.day and t4>today.month:
                            calculate=(t2 - t1)-1  
                            call_labs2() 
                
        except ValueError:
            labelindicate['bg']='red'
            labelindicate['text']='Erreur'     
            messagebox.showerror(title=None, message='veuillez entrer des nombres', )
            print("Error")

            # if t4<T_limit_MOIS:
            #     calculate=(t2 - t1)+1
            #     labelindicate['text']=(f"vous avez {calculate} ans")
            # if t3<=T_limit_JOURS or t4<=T_limit_MOIS:
            #     calculate=(t2 - t1)
            #     labelindicate['text']=(f"vous avez {calculate} ans")

            # if t4>T_limit_MOIS or t3<T_limit_MOIS:
            #     calculate=(t2 - t1)-1
            #     labelindicate['text']=(f"vous avez {calculate} ans")
    
    root1.mainloop()
application()    