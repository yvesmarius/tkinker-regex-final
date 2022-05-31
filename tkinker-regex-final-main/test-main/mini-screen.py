from tkinter import *
import sys
import re
from PIL import ImageTk, Image
from tkinter import Tk, ttk
import sqlite3
    
# gui.configure(background="blue")
def all_app():
    root = Tk()
    root.geometry("600x600")
    root.withdraw()
    def fenetreconnexion():
        log=Toplevel(root)
        log.title("inscription")
        log.geometry("600x600")
        log.resizable(width=False,height=False)

        canvas= Canvas(log,width=600,height=600)
        img = ImageTk.PhotoImage(Image.open('C:\\Users\\ykoua\\Desktop\\tkinker-regex-final-main\\test-main\\Gallet.png'))  # PIL solution
        canvas.img=img
        canvas.create_image(0, 0, anchor=NW, image=img)
        canvas.pack(fill=BOTH,expand=TRUE)
        btn_active1 =Image.open("test-main/y.png")
        btn_active=Image.open("test-main/i.png")

        log.btn_active1 = ImageTk.PhotoImage(btn_active1)
        log.btn_active = ImageTk.PhotoImage(btn_active)
        menu_gui=Menu(log)
        log.configure(menu=menu_gui)
        def quit_log():
            log.destroy()

        op=Menu(menu_gui,tearoff=0)
        menu_gui.add_cascade(label='options',menu=op)
        menu_gui.add_cascade(label='connectez vous',command=lambda:[fenetrelogin(),quit_log()])
        op.add_command(label='settings')
        op.add_command(label='contact us')
        op.add_command(label='help')
        lbl_inscrpit= LabelFrame(log,height=400,width=400,bd=0,bg="white")
        lbl_inscrpit.place(x=100,y=100)
        def sortir():
            sys.exit()
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
                regex = re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")
            
                if re.fullmatch(regex, email):
                    user_info["email"]=ma_variable3.get()
                    if(not ma_variable3.get().strip()):
                        error_Email['fg']='green'
                        error_Email['text']='valide♥'
                        print("Valid email")
                        user_info["email"]=ma_variable3.get()      
                    else :
                        pass
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
                
                regex1=re.compile("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
                if re.fullmatch(regex1,passw):
                    def space(text):
                        if ' ' in (text):
                            error_password['fg']='red'
                            error_password['text']='le pass doit pas contenir despace '    
                            valider()
                        else: 
                            error_password['fg']='green'
                            error_password['text']='valide♥'    
                            user_info["password"]=ma_variable4.get()
                           
                    space(ma_variable4.get())            
                else:
                    error_password['fg']='red' 
                    error_password['text']="""
                    mot de pass doit contenir au moins 
                    8 caractères X
                    une lettre majuscule et miniscule
                    un chiffre
                    un caractere speciale
                    aucun espace"""
                    statut_bar['fg']='red'
                    statut_bar['text']='erreur' 
                    valider()
                if ma_variable5.get()=="":
                    error_password_conf['fg']='red'
                    error_password_conf['text']='remplissez ce champ'
                if ma_variable5.get()!=ma_variable4.get(): 
                    error_password_conf['fg']='red'   
                    error_password_conf['text']='le mot de pass ne correspond pas'
                if ma_variable5.get()==ma_variable4.get():
                    error_password_conf['fg']='green'   
                    error_password_conf['text']='valide'    
                    
                if RecursionError:
                    pass    
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

            if ma_variable2.get()!="" and ma_variable1.get()!="" and ma_variable3.get()!="" and ma_variable4.get()!="" and type_people.get()=="femelle"or"male" and ma_variable4.get()==ma_variable5.get() :
                
                connexion=sqlite3.connect('data_user.db')
                # conn = sqlite3.connect("data_user.db")            
                curseur=connexion.cursor()
                # c = conn.cursor()
                curseur.execute("""CREATE TABLE IF NOT EXISTS data_sc(
                    Nom text ,
                    prenom text,
                    email text,
                    password text,
                    sexe text
                    )""")                
                curseur.execute("SELECT email FROM data_sc")    
                list_email=curseur.fetchall()
                verify_mail_box=[]
                for i in list_email:
                    for u in i:
                        print('ok')
                        verify_mail_box.append(u)            
                print(verify_mail_box)
                if ma_variable3.get() in verify_mail_box: 
                    error_Email['fg']='red'
                    error_Email['text']='l email existe deja'        
        
                else:
                    error_Email['fg']='green'
                    error_Email['text']='valide♥'
                    # c.execute('''CREATE TABLE IF NOT EXISTS accounts(uname text, pwd text)''')
                    # c.execute("INSERT INTO accounts VALUES (?, ?)", [ma_variable3.get(), ma_variable4.get()])
                    curseur.execute("INSERT INTO data_sc VALUES (:Nom,:prenom,:email,:password,:sexe)",user_info)
                    connexion.commit()
                    # conn.commit()
                    
                    connexion.close()
                    # conn.close()

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
                            log.after(1000,sortir)                            
                    anim(0)
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

        lbl5=Label(lbl_inscrpit,text="confirm_password",fg="black",bg="white",border=2)
        lbl5.place(x=25,y=210)

        ma_variable1=StringVar()
        ent=Entry(lbl_inscrpit,width=20,textvariable=ma_variable1,insertofftime=1200,border=3)
        ent.place(x=140,y=10)
        ent.focus_set()

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
        ent3=Entry(lbl_inscrpit,width=20,textvariable=ma_variable4,insertofftime=1200,border=3,show='')
        ent3.place(x=140,y=160)

        error_password=Label(lbl_inscrpit,fg='red',bg='white')
        error_password.place(x=140,y=184)

        ma_variable5=StringVar()
        ent4=Entry(lbl_inscrpit,width=20,textvariable=ma_variable5,insertofftime=1200,border=3)
        ent4.place(x=140,y=210)
        
        error_password_conf=Label(lbl_inscrpit,fg='red',bg='white')
        error_password_conf.place(x=140,y=236)
        
        def update_entry():
            global hidden
            hidden = True
            if hidden:
                ent3['show'] ='*'
                ent4['show']='*'
                btn['image'] = hide

                pass
            else:
                ent3['show'] = ''
                ent4['show']=''
                btn['image'] = view
            hidden = not hidden
                   
        hide = ImageTk.PhotoImage(file='test-main\hide.png')
        view = ImageTk.PhotoImage(file='test-main\show.png')
        btn = Button(lbl_inscrpit,image=view,command=update_entry,border=0)
        btn.place(x=280,y=157.6)
        
        supp=Label(lbl_inscrpit,text="sortir",font=("verdana",10),bg="white")
        supp.place(x=271,y=352)

        supp1=Label(lbl_inscrpit,text="Valider",font=("verdana",10),bg="white")
        supp1.place(x=70,y=352)
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

    def fenetrelogin():
        def sortir1():
            sys.exit()
        log1=Toplevel(root,bg='#e0d0ce')
        log1.title("login") 
        log1.geometry("600x600")
        log1.resizable(width=False,height=False)
        label_titre_inscript=Label(log1,text='se connectez',font=('verdana',12),bg='#e0d0ce')
        label_titre_inscript.place(x=242,y=70)

        label_login_nom=Label(log1,text='Email',bg='#e0d0ce')
        label_login_nom.place(x=281,y=143)
        variable_nom_pass1=StringVar()
        label_login_ent=Entry(log1,textvariable=variable_nom_pass1,insertofftime=1200)
        label_login_ent.place(x=235,y=170)

        label_login_pass=Label(log1,text='password',bg='#e0d0ce')
        label_login_pass.place(x=270,y=200)
        variable_nom_pass=StringVar()
        label_login_ent1=Entry(log1,textvariable=variable_nom_pass,insertofftime=1200)
        label_login_ent1.place(x=235,y=228)
       
        statut_login=Label(log1,text='statut')
        statut_login.place(x=265,y=260)

        menu_gui1=Menu(log1)
        log1.configure(menu=menu_gui1)

        op=Menu(menu_gui1,tearoff=0)
        menu_gui1.add_cascade(label='options',menu=op)
        op.add_command(label='settings')
        op.add_command(label='contact us')
        op.add_command(label='help')
        menu_gui1.add_command(label='inscrivez-vous',command=lambda:[fenetreconnexion(),quit_log1()])
        
        menu_gui1.add_command(label='exit',command=sortir1)
        def login():
            connexion=sqlite3.connect('data_user.db')
            curseur=connexion.cursor()
            curseur.execute("SELECT * FROM data_sc WHERE email=? and password=?", [variable_nom_pass1.get(), variable_nom_pass.get()])
            
            if curseur.fetchone() == None:
                statut_login['bg']='red'
                statut_login['text']='incorrect'
                
            else:
                statut_login['bg']='green'
                statut_login['text']='connexion success'
                
        butt_valider_login=Button(log1,text='valider',command=login)
        butt_valider_login.place(x=265,y=300)
        def quit_log1():
            log1.destroy()
        # def quit_log1():
        #     log1.destroy()
        #     if closed[0]:
        #         root.destroy()
        #     else:
        #         closed[1]=False
        # closed=[False, False]
        # log1.protocol("WM_DELETE_WINDOW", quit_log1)

    # def quit_log():
    #     log.destroy()
    #     if closed[1]:
    #         root.destroy()
    #     else:
    #         closed[0]=True
            
    # def quit_log1():
    #     log1.destroy()
    #     if closed[0]:
    #         root.destroy()
    #     else:
    #         closed[1]=True
    # closed=[False, False]
    # log.protocol("WM_DELETE_WINDOW", quit_log)
    # log1.protocol("WM_DELETE_WINDOW", quit_log1)    
    fenetreconnexion()
    
    root.mainloop()
all_app()        
        
    
    

# 
#        

#         menu_gui.add_command(label='connectez-vous',command=quit_log)        
#     # filepath = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')])
#     # photo = PhotoImage(file=filepath)

#     # canv = Canvas(gui, width=600, height=600, bg='white')
#     # canv.grid(row=2, column=3)

#     # img = ImageTk.PhotoImage(Image.open("check.png"))  # PIL solution
#     # canv.create_image(0, 0, anchor=NW, image=img)
        

#         def anim(value):    
#             if progress['value']<value:
#                 progress.stop() 
#                 progress["value"] = progress['maximum']
#             lbl_inscrpit.after(10, anim, progress["value"])
#             if  progress["value"] == progress['maximum']:
#                 statut_bar['fg']='green'
#                 statut_bar['text']='inscription réussie'
#                 log.after(1000,quit_log)                            
#         anim(0)
            

            
        

                   
    

    
#     # login()    
    
    

# def sortir():
#     sys.exit()










