import tkinter as tk #don't from tikinter import * (bad)
from model import Model as m


test = 0

class View:
    def __init__(self, root, model):
        self.root = root #tkinter root
        self.model = model #model instance
       

        self.dx = 9
        self.dy = 4
        self.dx1= 6
        self.dy1= 3

        self.pd = tk.StringVar()
        self.cd = tk.StringVar()
        self.pd.set("Programable")
        self.cd.set("Calculator")
        global test
        test += 1
        print(" ")
        print ("order number " + str(test))

    #BUTTON FUNCTIONS START HERE
    def number (self):
        global test
        test += 1
      
        print(" ")
        print("Gyoza Ann Bar™ all right reserve")
        print(" ")
        print("_____________________________________")
        print ("order number " + str(test))
        self.model.cancel()
        self.cd.set("0")
        
    def un(self):
        print("button with some function")
    def ex(self):
        self.pd.set("Fucking Hell")
    def b4 (self):
        self.calc_input("+")
        self.calc_input("7")
        self.pd.set("7$ Spicy Goza")
        print ("1 spicy gyoza")

    def b5 (self):
        self.calc_input("+")
        self.calc_input("7")
        self.pd.set("7$ vegeterian gyoza")
        print("1 vegeterian gyoza")
    def b6 (self):
        self.calc_input("+")
        self.calc_input("7")
        self.pd.set("7$ chicken gyoza")
        print("1 chicken gyoza")
    def b7 (self):
        self.calc_input("+")
        self.calc_input("7")
        self.pd.set("7$ pork gyoza")
        print("1 pork gyoza")

    def b8 (self):
        self.calc_input("+")
        self.calc_input("7")
        self.pd.set("7$ shrimp gyoza")
        print("1 shrimp gyoza")

    def b9 (self):
        self.calc_input("+")
        self.calc_input("7")
        self.pd.set("seafood gyoza")
        print("1 seafood gyoza")
    def b10 (self):
        self.calc_input("+")
        self.calc_input("9")
        self.pd.set("7$ teriyaki chicken")
        print("1 teriyaki chicken")

    def b11 (self):
        self.calc_input("+")
        self.calc_input("1")
        self.calc_input("0")
        self.pd.set("10$ teriyaki salmon")
        print("1 teriyaki salmon")

    def b12 (self):
        self.calc_input("+")
        self.calc_input("5")
        self.pd.set("5$ vanilla ice cream")
        print("1 vanilla ice cream")

    def b13 (self):
        self.calc_input("+")
        self.calc_input("5")
        self.calc_input(".")
        self.calc_input("5")
        self.pd.set("5.50$ green tea ice cream")
        print("1 green tea ice cream")

    def b14 (self):
        self.calc_input("+")
        self.calc_input("5")
        self.pd.set("5$ akane")
        print("1 akane")

    def b15 (self):
        self.calc_input("+")
        self.calc_input("5")
        self.pd.set("5$ daiki")
        print("1 daiki")


    def b16 (self):
        self.calc_input("+")
        self.calc_input("5")
        self.pd.set("5$ sake ginger")
        print("1 sake ginger")
    def b17 (self):
        self.calc_input("+")
        self.calc_input("5")

        self.pd.set("5$ ninja")
        print("1 ninja")
    def b18 (self):
        self.calc_input("+")
        self.calc_input("5")

        self.pd.set("5$ samurai")
        print("1 samurai")

    def b19 (self):
        self.calc_input("+")
        self.calc_input("5")

        self.pd.set("5$ sora")
        print("1 sora")
    def req (self):
        top = tk.Toplevel()
        top.title("Special Request")
        self.ent = tk.Entry(top)
        self.ent.pack()
        msg= tk.Button(top, text = 'ok',command=(self.rohan))
        msg.pack()
    def a95 (self) :
        print("discount an item : 95%")
        self.calc_input("*")
        self.calc_input("0")
        self.calc_input(".")
        self.calc_input("9")
        self.calc_input("5")
        
    def a85 (self) :
        print("discount an item : 85%")
        self.calc_input("*")
        self.calc_input("0")
        self.calc_input(".")
        self.calc_input("8")
        self.calc_input("5")
    def a75 (self) :
        print("discount an item : 75%")
        self.calc_input("*")
        self.calc_input("0")
        self.calc_input(".")
        self.calc_input("7")
        self.calc_input("5")
    
    def rohan (self):
        print("###-----____________________*IMPORTANT!!!*____________________-----###")
        print(' '*32+self.ent.get())
        print("-------------------Customer is always right!!!-----------------------")
        
        
        




    def m1 (self):
        self.calc_input("-")
        self.calc_input("3")

        self.pd.set("meal discount gyoza & drink -3$ ")
        print("meal discount gyoza & drink -3$")

    def m2 (self):
        self.calc_input("-")
        self.calc_input("5")

        self.pd.set("meal discount gyoza & drink & ice cream -5$ ")
        print("meal discount gyoza & drink & ice cream -5$")

    def m3 (self):
        self.calc_input("-")
        self.calc_input("2")

        self.pd.set("meal discount gyoza ice cream -2$ ")
        print("meal discount gyoza & ice cream -2$")

    def m4 (self):
        self.calc_input("-")
        self.calc_input("3")

        self.pd.set("hot meal with drink discount -3$ ")
        print("hot meal & drink discount -3$")
    def n1(self):
        self.calc_input("1")

    def n2(self):
        self.calc_input("2")

    def n3(self):
        self.calc_input("3")

    def n4(self):
        self.calc_input("4")

    def n5(self):
        self.calc_input("5")

    def n6(self):
        self.calc_input("6")

    def n7(self):
        self.calc_input("7")

    def n8(self):
        self.calc_input("8")

    def n9(self):
        self.calc_input("9")

    def n0(self):
        self.calc_input("0")

    def np(self):
        self.model.input("+")

    def nm(self):
        self.model.input("-")
        print("###-----____________________*IMPORTANT!!!*____________________-----###")
        print("cancel an item")
        print("----------------------------------------------------------------------")

    def nd(self):
        self.model.input("/")

    def nt(self):
        self.model.input("*")
    def do(self):
        self.model.input(".")


    def ne(self):
        self.model.input("=")
        self.cd.set(str(self.model.get_result()))

    def nc(self):
        self.model.cancel()
        self.cd.set("0")

    def calc_input(self, i): #inputs number into calculator model and updates the display
        self.model.input(i)
        self.cd.set(self.model.get_buffer())
    #BUTTON FUNCTIONS END HERE

    def make_gui(self): #consttructs the gui
        #frame which widgets attach to
        f = tk.Frame(self.root)
        f.pack(side=tk.LEFT)
        

        #labels above and below buttons
        
        imagelabel = tk.Label(f, textvariable=self.pd,bg="#888080",wrap=300,width=4*self.dx,height=self.dy)
        #photo999 = tk.PhotoImage(file="hot.png")
        #imagelabel.config(image=photo999,width="280",height="10")
        #imagelabel.image=photo999
        imagelabel.grid(row=0,column=0,columnspan=4,sticky=tk.N+tk.E+tk.S+tk.W)

        tk.Button(f, text="special request: ",bg="#728888",wrap=300,width=8*self.dx,height=self.dy,command=self.req).grid(row=6,column=0,columnspan=13,sticky=tk.N+tk.E+tk.S+tk.W)


      
        

        tk.Label(f,bg="#888080",textvariable=self.cd,width=4*self.dx,height=self.dy).grid(row=0,column=5,columnspan=4,sticky=tk.N+tk.E+tk.S+tk.W)
    

        #logo to the left (by default) of the buttons
        logo = tk.PhotoImage(file='m.gif')
        i=tk.Label(f,bg="#888888",image=logo,width=4*self.dx,height=6*self.dy)
        i.config(image=logo,width="190",height="400")
        i.image=logo
        i.grid(row=0,column=9,columnspan=4,rowspan=6,sticky=tk.N+tk.E+tk.S+tk.W)

        #blankspace between buttons
        imagelabel = tk.Label(f,width=self.dx,height=self.dy,bg="#bfffff")
        photo999 = tk.PhotoImage(file="hot.png")
        imagelabel.config(image=photo999,width="30",height="20")
        imagelabel.image=photo999
        imagelabel.grid(row=0,column=4,rowspan=6,sticky=tk.N+tk.E+tk.S+tk.W)
  

        imagebutton001= tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.m1,borderwidth=1,text="B14")
        photo001 = tk.PhotoImage(file="meal1.png")
        imagebutton001.config(image=photo001,width="60",height="60")
        imagebutton001.image=photo001
        imagebutton001.grid(row=1,column=0)
        imagebutton002= tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.m2,borderwidth=1,text="B14")
        photo002 = tk.PhotoImage(file="meal2.png")
        imagebutton002.config(image=photo002,width="60",height="60")
        imagebutton002.image=photo002
        imagebutton002.grid(row=1,column=1)
        imagebutton003= tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.m3,borderwidth=1,text="B14")
        photo003 = tk.PhotoImage(file="meal3.png")
        imagebutton003.config(image=photo003,width="60",height="60")
        imagebutton003.image=photo003
        imagebutton003.grid(row=1,column=2)
        imagebutton004= tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.m4,borderwidth=1,text="B14")
        photo004 = tk.PhotoImage(file="meal4.png")
        imagebutton004.config(image=photo004,width="60",height="60")
        imagebutton004.image=photo004
        imagebutton004.grid(row=1,column=3)

        tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.nc,borderwidth=2,text="C").grid(row=1,column=5)#calc
        tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.nd,borderwidth=2,text="/").grid(row=1,column=6)#calc
        tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.nt,borderwidth=2,text="*").grid(row=1,column=7)#calc
        tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.nm,borderwidth=2,text="-").grid(row=1,column=8)#calc

        imagebutton4 = tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="grey",command=self.b4,borderwidth=1,text="B8")
        photo4 = tk.PhotoImage(file="pepper.gif")
        imagebutton4.config(image=photo4,width="60",height="60")
        imagebutton4.image=photo4
        imagebutton4.grid(row=2,column=0)
        #IMAGE BUTTON EXAMPLE START
        imagebutton1 = tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.b5,borderwidth=1,text="B5")
        photo1 = tk.PhotoImage(file="b.gif")
        imagebutton1.config(image=photo1,width="60",height="60")
        imagebutton1.image=photo1
        imagebutton1.grid(row=2,column=1)
        #IMAGE BUTTON EXAMPLE END
        imagebutton2 = tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.b6,borderwidth=1,text="B6")
        photo2 = tk.PhotoImage(file="CHICKEN.gif")
        imagebutton2.config(image=photo2,width="60",height="60")
        imagebutton2.image=photo2
        imagebutton2.grid(row=2,column=2)
        imagebutton3 = tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.b7,borderwidth=1,text="B7")
        photo3 = tk.PhotoImage(file="pork.gif")
        imagebutton3.config(image=photo3,width="60",height="60")
        imagebutton3.image=photo3
        imagebutton3.grid(row=2,column=3)
        tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.n7,borderwidth=2,text="7").grid(row=2,column=5)#calc
        tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.n8,borderwidth=2,text="8").grid(row=2,column=6)#calc
        tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.n9,borderwidth=2,text="9").grid(row=2,column=7)#calc
        tk.Button(f,width=self.dx,bg="black",fg="white",command=self.np,borderwidth=2,text="+").grid(row=2,column=8,rowspan=2,sticky=tk.N+tk.E+tk.S+tk.W)#calc

        imagebutton5 = tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.b8,borderwidth=1,text="B8")
        photo5 = tk.PhotoImage(file="pawn.gif")
        imagebutton5.config(image=photo5,width="60",height="60")
        imagebutton5.image=photo5
        imagebutton5.grid(row=3,column=0)
        
        imagebutton6 = tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.b9,borderwidth=1,text="B9")
        photo6 = tk.PhotoImage(file="seafood.gif")
        imagebutton6.config(image=photo6,width="60",height="60")
        imagebutton6.image=photo6
        imagebutton6.grid(row=3,column=1)
        
        imagebutton7 = tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.b10,borderwidth=1,text="B10")
        photo7 = tk.PhotoImage(file="TeriSal.png")
        imagebutton7.config(image=photo7,width="60",height="60")
        imagebutton7.image=photo7
        imagebutton7.grid(row=3,column=2)
        imagebutton8 = tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.b11,borderwidth=1,text="B10")
        photo8 = tk.PhotoImage(file="TeriChick.png")
        imagebutton8.config(image=photo8,width="60",height="60")
        imagebutton8.image=photo8
        imagebutton8.grid(row=3,column=3)
        imagebutton9 = tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.b12,borderwidth=1,text="B10")
        photo9 = tk.PhotoImage(file="Vice.png")
        imagebutton9.config(image=photo9,width="60",height="60")
        imagebutton9.image=photo9
        imagebutton9.grid(row=4,column=0)
        imagebutton10 = tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.b13,borderwidth=1,text="B10")
        photo10 = tk.PhotoImage(file="Gice.png")
        imagebutton10.config(image=photo10,width="60",height="60")
        imagebutton10.image=photo10
        imagebutton10.grid(row=4,column=1)
        tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.n4,borderwidth=2,text="4").grid(row=3,column=5)#calc
        tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.n5,borderwidth=2,text="5").grid(row=3,column=6)#calc
        tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.n6,borderwidth=2,text="6").grid(row=3,column=7)#calc
        #tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.un,borderwidth=2,text="B0").grid(row=3,column=7)

        
        imagebutton11= tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.b14,borderwidth=1,text="B14")
        photo11 = tk.PhotoImage(file="akane.png")
        imagebutton11.config(image=photo11,width="60",height="60")
        imagebutton11.image=photo11
        imagebutton11.grid(row=4,column=2)
        imagebutton12= tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.b15,borderwidth=1,text="B14")
        photo12 = tk.PhotoImage(file="dai.png")
        imagebutton12.config(image=photo12,width="60",height="60")
        imagebutton12.image=photo12
        imagebutton12.grid(row=4,column=3)
        tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.n1,borderwidth=2,text="1").grid(row=4,column=5)#calc
        tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.n2,borderwidth=2,text="2").grid(row=4,column=6)#calc
        tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.n3,borderwidth=2,text="3").grid(row=4,column=7)#calc
        tk.Button(f,width=self.dx,bg="black",fg="white",command=self.ne,borderwidth=2,text="=").grid(row=4,column=8,rowspan=2,sticky=tk.N+tk.E+tk.S+tk.W)#calc

        imagebutton13= tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.b16,borderwidth=1,text="B14")
        photo13 = tk.PhotoImage(file="gin.png")
        imagebutton13.config(image=photo13,width="60",height="60")
        imagebutton13.image=photo13
        imagebutton13.grid(row=5,column=0)
        imagebutton14= tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.b17,borderwidth=1,text="B14")
        photo14 = tk.PhotoImage(file="nija.png")
        imagebutton14.config(image=photo14,width="60",height="60")
        imagebutton14.image=photo14
        imagebutton14.grid(row=5,column=1)
        imagebutton15= tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.b18,borderwidth=1,text="B14")
        photo15 = tk.PhotoImage(file="samu.png")
        imagebutton15.config(image=photo15,width="60",height="60")
        imagebutton15.image=photo15
        imagebutton15.grid(row=5,column=2)
        imagebutton16= tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.b19,borderwidth=1,text="B14")
        photo16 = tk.PhotoImage(file="sora.png")
        imagebutton16.config(image=photo16,width="60",height="60")
        imagebutton16.image=photo16
        imagebutton16.grid(row=5,column=3)
        tk.Button(f,width=self.dx,bg="black",fg="white",command=self.n0,borderwidth=2,text="0").grid(row=5,column=5,columnspan=2,sticky=tk.N+tk.E+tk.S+tk.W)#calc
        tk.Button(f,width=self.dx1,height=self.dy1,bg="#708888",fg="white",command=self.a95,borderwidth=2,text="95%").grid(row=5,column=9)
        #tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.a90,borderwidth=2,text="90%").grid(row=5,column=8)
        tk.Button(f,width=self.dx1,height=self.dy1,bg="#708888",fg="white",command=self.a85,borderwidth=2,text="85%").grid(row=5,column=10)
        #tk.Button(f,width=self.dx,height=self.dy,bg="black",fg="white",command=self.a80,borderwidth=2,text="80%").grid(row=5,column=11)
        tk.Button(f,width=self.dx1,height=self.dy1,bg="#708888",fg="white",command=self.a75,borderwidth=2,text="75%").grid(row=5,column=11)#calc
        tk.Button(f,width=self.dx,height=self.dy,bg="#383838",fg="#888888",command=self.number,borderwidth=3,text="new order").grid(row=5,column=7)
        

