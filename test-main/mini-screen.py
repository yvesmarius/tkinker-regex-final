from tkinter import *
import json
import sys
from tkinter.filedialog import *
import re
from PIL import ImageTk, Image
from tkinter import Tk, ttk
import sqlite3


root = Tk()
root.geometry("600x600")
root.withdraw()
# gui.configure(background="blue")
log=Toplevel(root,bg='#e0d0ce')
log.title("inscription")
log.geometry("600x600")
log.resizable(width=False,height=False)

menu_gui=Menu(log)
log.configure(menu=menu_gui)

op=Menu(menu_gui,tearoff=0)
menu_gui.add_cascade(label='options',menu=op)
op.add_command(label='settings')
op.add_command(label='contact us')
op.add_command(label='help')
log1=Toplevel(root,bg='#e0d0ce')
# def login():
    # success = False
    # files=open("user_detail.json","r")        
    # if ma_variable1.get()==ma_variable1.get() and variable_nom_pass.get()==ma_variable4.get() in files  :
    #     success = True
      
    
    #     if(success):
    #         statut_login['text']='chargement'
    #         log1.after(2000)
    #         statut_login['fg']='green'
            

        
    #     else:
    #         statut_login['fg']='red'
    #         statut_login['text']='vous etes connectez'

log1.title("login")
log1.geometry("600x600")
log1.resizable(width=False,height=False)
label_titre_inscript=Label(log1,text='se connectez',font=('verdana',12),bg='#e0d0ce')
label_titre_inscript.place(x=242,y=70)

label_login_nom=Label(log1,text='nom',bg='#e0d0ce')
label_login_nom.place(x=281,y=143)
variable_nom_pass1=StringVar
label_login_ent=Entry(log1,textvariable=variable_nom_pass1,insertofftime=1200)
label_login_ent.place(x=235,y=170)

label_login_pass=Label(log1,text='password',bg='#e0d0ce')
label_login_pass.place(x=270,y=200)
variable_nom_pass=StringVar
label_login_ent1=Entry(log1,textvariable=variable_nom_pass,insertofftime=1200)
label_login_ent1.place(x=235,y=228)


# button_pass=Button(log1,text='connexion',command=login)
# button_pass.place(x=265,y=300)

statut_login=Label(log1,text='statut')
statut_login.place(x=265,y=260)

menu_gui1=Menu(log1)
log1.configure(menu=menu_gui1)

op=Menu(menu_gui,tearoff=0)
menu_gui1.add_cascade(label='options',menu=op)
op.add_command(label='settings')
op.add_command(label='contact us')
op.add_command(label='help')
menu_gui1.add_command(label='inscrivez-vous')
def sortir1():
    sys.exit()
menu_gui1.add_command(label='exit',command=sortir1)


def quit_log():
    log.destroy()
    if closed[1]:
        root.destroy()
    else:
        closed[0]=True
    
def quit_log1():
    log1.destroy()
    if closed[0]:
        root.destroy()
    else:
        closed[1]=True
closed=[False, False]
log.protocol("WM_DELETE_WINDOW", quit_log)
log1.protocol("WM_DELETE_WINDOW", quit_log1)

menu_gui.add_command(label='connectez-vous',command=quit_log)        
# filepath = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')])
# photo = PhotoImage(file=filepath)

# canv = Canvas(gui, width=600, height=600, bg='white')
# canv.grid(row=2, column=3)

# img = ImageTk.PhotoImage(Image.open("check.png"))  # PIL solution
# canv.create_image(0, 0, anchor=NW, image=img)
canvas= Canvas(log,bg="#1b1b1b",bd=0)
img = ImageTk.PhotoImage(Image.open("Gallet.png"))  # PIL solution
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.pack(fill=BOTH,expand=TRUE)
btn_active1 =Image.open("y.png")
btn_active=Image.open("i.png")

log.btn_active1 = ImageTk.PhotoImage(btn_active1)
log.btn_active = ImageTk.PhotoImage(btn_active)


            
def valider():
 
    
    
    user_info = {
       
    "Nom":ma_variable1.get() ,
    "prenom": ma_variable2.get(),
    "email": ma_variable3.get(),
    "password": ma_variable4.get(),
    "sexe": type_people.get()}
    

    if ma_variable1.get()=="":
        error_nom['fg']='red'
        error_nom['text']='veuillez entrez un nom X'
        statut_bar['fg']='red'
        statut_bar['text']='erreur'
        valider()

    if ma_variable1.get()!="":
        error_nom['fg']='green'
        error_nom['text']='valide♥'
        user_info["Nom"]=ma_variable1.get()
                
    if ma_variable2.get()=="":
        error_prenom['fg']='red'
        error_prenom['text']='veuillez entré un prenom X '
        statut_bar['fg']='red'
        statut_bar['text']='erreur'
        valider()
    if ma_variable2.get()!="":
        error_prenom['fg']='green'
        error_prenom['text']='valide♥'
        user_info["prenom"]=ma_variable2.get() 
    def isValid(email):    

        if ma_variable3.get()=="":
            error_Email['fg']='red'
            error_Email['text']='veuillez entré votre email X'
            statut_bar['fg']='red'
            statut_bar['text']='erreur'
            valider()
        regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    
        if re.fullmatch(regex, email):
            error_Email['fg']='green'
            error_Email['text']='valide♥'
            print("Valid email")
            user_info["email"]=ma_variable3.get()
        else:
            error_Email['fg']='red'
            error_Email['text']='email invalide'
            statut_bar['fg']='red'
            statut_bar['text']='erreur'
            valider()        
    isValid(ma_variable3.get())

    def isValid_pwd(passw):

        if ma_variable4.get()=="":
            error_password['fg']='red' 
            error_password['text']='veuillez entré un mot de pass X'
            statut_bar['fg']='red'
            statut_bar['text']='erreur'
            valider()
        
        regex=re.compile(r'^.{8,32}$')
        if re.fullmatch(regex,passw):
            error_password['fg']='green'
            error_password['text']='valide♥'    
            user_info["password"]=ma_variable4.get()
        else:
            error_password['fg']='red' 
            error_password['text']='mot de pass doit contenir au moins 8 caractères X'
            statut_bar['fg']='red'
            statut_bar['text']='erreur' 
            valider()
    isValid_pwd(ma_variable4.get())
        
               
    if type_people.get()=="male":
        user_info["sexe"]=type_people.get()
        verify_radio['fg']='green'
        verify_radio['text']='valide♥'
        
    if type_people.get()=="femelle":
        user_info["sexe"]=type_people.get()
        verify_radio['fg']='green'
        verify_radio['text']='valide♥'
        
    if type_people.get()=='Non defini':
        verify_radio['fg']='red'
        verify_radio['text']='veuillez indiquer votre sexe'
        user_info["sexe"]="Non-defini"
        statut_bar['fg']='red'
        statut_bar['text']='erreur'
        
        valider() 

    if ma_variable2.get()!="" and ma_variable1.get()!="" and ma_variable3.get()!="" and ma_variable4.get()!="" and type_people.get()=="femelle"or"male" :
        connexion=sqlite3.connect('data_user.db')
        curseur=connexion.cursor()
        curseur.execute("""CREATE TABLE IF NOT EXISTS data_sc(
            Nom text ,
            prenom text,
            email text,
            password text,
            sexe text
            )""")

        curseur.execute("INSERT INTO data_sc VALUES (:Nom,:prenom,:email,:password,:sexe)",user_info)
        connexion.commit()
        connexion.close()
        
        statut_bar['fg']='black'
        statut_bar['text']='verification.....'
        progress.start()
        def anim(value):    
            if progress['value']<value:
                progress.stop() 
                progress["value"] = progress['maximum']
            lbl_inscrpit.after(10, anim, progress["value"])
            if  progress["value"] == progress['maximum']:
                statut_bar['fg']='green'
                statut_bar['text']='inscription réussie'
                log.after(1000,quit_log)                            
        anim(0)
        def register():
            data_user={ma_variable1.get():ma_variable4.get()}
            data_user[ma_variable1.get()]=ma_variable4.get()
            list_user={}
            list_user.update(data_user)
            with open("user_detail.json","w")as h:
                donnée=json.dump(list_user,h,indent=4)

        register()            
    

    
    # login()    
    
    

def sortir():
    sys.exit()

lbl_inscrpit= LabelFrame(log,height=400,width=400,bd=0,bg="white")
lbl_inscrpit.place(x=100,y=100)

button=Button(lbl_inscrpit,image=log.btn_active,bg="white",bd=0,relief="sunken",activebackground="white",border=0,command=sortir)
button.place(x=330,y=350)

button1=Button(lbl_inscrpit,image=log.btn_active1,bg="white",bd=0,relief="sunken",activebackground="white",border=0,width=32,height=32,command=valider)
button1.place(x=30,y=350)

type_people=StringVar()
type_people.set('Non defini')
sexe=Radiobutton(lbl_inscrpit,text="Male",variable=type_people,font=("verdana",10),value='male',bg='white')
sexe1=Radiobutton(lbl_inscrpit,text="Femelle",variable=type_people,font=("verdana",10),value='femelle',bg='white')
sexe.place(x=50,y=250)
sexe1.place(x=280,y=250)
verify_radio=Label(lbl_inscrpit,bg='white')
verify_radio.place(x=50,y=280)

progress=ttk.Progressbar(lbl_inscrpit,length=350,maximum=200,value=0)
progress.place(x=25,y=320)

statut_bar=Label(lbl_inscrpit,text="statut:Non-verifier",bg="white")
statut_bar.place(x=160,y=296)

def go_in(event):
    button['bg']="#f44336"
  
def go_out(event):
    button['bg']="white"
    
def go_in1(event):
    button1['bg']="#0ed145"
def go_out1(event):
    button1['bg']="white"
button.bind('<Enter>', go_in)
button.bind('<Leave>', go_out)
button1.bind('<Enter>', go_in1)
button1.bind('<Leave>', go_out1)

lbl0=Label(log,text="Inscriver-vous",font=('verdana',12),fg='black')
lbl0.place(x=228,y=70)

lbl1=Label(lbl_inscrpit,text="Nom",fg="black",bg="white")
lbl1.place(x=85,y=10)

lbl2=Label(lbl_inscrpit,text="prénom",fg="black",bg="white")
lbl2.place(x=85,y=60)

lbl3=Label(lbl_inscrpit,text="Email",fg="black",bg="white",border=2)
lbl3.place(x=85,y=110)

lbl4=Label(lbl_inscrpit,text="password",fg="black",bg="white",border=2)
lbl4.place(x=75,y=160)

ma_variable1=StringVar()
ent=Entry(lbl_inscrpit,width=20,textvariable=ma_variable1,insertofftime=1200,border=3)
ent.place(x=140,y=10)

error_nom=Label(lbl_inscrpit,fg='red',bg='white')
error_nom.place(x=140,y=30)

ma_variable2=StringVar()
ent1=Entry(lbl_inscrpit,width=20,textvariable=ma_variable2,insertofftime=1200,border=3)
ent1.place(x=140,y=60)

error_prenom=Label(lbl_inscrpit,fg='red',bg='white')
error_prenom.place(x=140,y=82)

ma_variable3=StringVar()
ent2=Entry(lbl_inscrpit,width=20,textvariable=ma_variable3,insertofftime=1200,border=3)
ent2.place(x=140,y=110)

error_Email=Label(lbl_inscrpit,fg='red',bg='white')
error_Email.place(x=140,y=132)

ma_variable4=StringVar()
ent3=Entry(lbl_inscrpit,width=20,textvariable=ma_variable4,insertofftime=1200,border=3)
ent3.place(x=140,y=160)

error_password=Label(lbl_inscrpit,fg='red',bg='white')
error_password.place(x=140,y=184)

supp=Label(lbl_inscrpit,text="sortir",font=("verdana",10),bg="white")
supp.place(x=271,y=352)

supp1=Label(lbl_inscrpit,text="Valider",font=("verdana",10),bg="white")
supp1.place(x=70,y=352)

root.mainloop()



