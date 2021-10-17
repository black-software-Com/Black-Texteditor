#!/usr/bin/python3
# Black-TextEditor
from tkinter import *
from tkinter.ttk import Button as TButton, Label,Notebook
from tkinter.messagebox import showinfo,showerror
from tkinter.colorchooser import askcolor
from tkinter.scrolledtext import ScrolledText
from tkhtmlview import HTMLLabel
from tkinter import filedialog
import subprocess
import webbrowser
class black_texteditor(Tk):
    def __init__(self):
        super(black_texteditor,self).__init__()
        global tab1,f,sc
        self.title('Black Texteditor')
        self.bind("<Control-n>",lambda x: self.new_tab_2(x))
        self.bind("<Control-r>",lambda x: self.new_2(x))
        self.bind("<Control-o>",lambda x: self.open_file_3(x))
        self.bind("<Control-s>",lambda x: self.save_3(x))
        self.bind("<Control-l>",lambda x: self.save_as_3(x))
        self.bind("<Control-w>",lambda x: self.close_all_2(x))
        self.photo = PhotoImage(file = './Scr/black.png')
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.i = False
        menu = Menu(self)
        filemenu = Menu(menu,tearoff=0)
        aboutmenu = Menu(menu,tearoff=0)
        fontfile = Menu(menu,tearoff=0)
        themefile = Menu(menu,tearoff=0)
        helpfile = Menu(menu,tearoff=0)
        self.check_tab = False
        self.check_button = False
        filemenu.add_command(label='New',accelerator='Ctrl+N',command=self.new_tab)
        filemenu.add_command(label='New Window',accelerator='Ctrl+r',command=self.new)
        filemenu.add_command(label='Open',accelerator='Ctrl+O',command=self.open_file)
        filemenu.add_command(label='Save',accelerator='Ctrl+S',command=self.save)
        filemenu.add_command(label='Save As',accelerator='Ctrl+l',command=self.save_as)
        filemenu.add_separator()
        filemenu.add_command(label='Close All',accelerator='Ctrl+w',command=self.close_all)
        filemenu.add_separator()
        filemenu.add_command(label='Exit',accelerator='Ctrl+F4',command=self.ext)  
        aboutmenu.add_command(label='Black',command=self.black)
        aboutmenu.add_command(label='Dev',command=self.dev)
        aboutmenu.add_command(label='Tools',command=self.tools)
        aboutmenu.add_command(label='License',command=self.license)   
        fontstyle = Menu(fontfile,tearoff=0) 
        fontsize = Menu(fontfile,tearoff=0)
        fontcolorfile = Menu(fontfile,tearoff=0)
        self.check_tab = False
        
        self.check_f = False
        self.welcome_date = open("welcome_date","r+")
        txt_welcome_d = self.welcome_date.read()
        self.welcome_date.close()
        self.check_nl = False
        f = Notebook(self)
        self.welcome = Frame(f)
        self.y = False
        self.check_nothing_l = False
        self.check_open_file = False
        if txt_welcome_d == "False":
            self.welcome = Frame(f)
            self.y = True
            tab1 = Frame(f)
            # tab1 = Frame(f)
            f.add(self.welcome,text='Welcome Black')    
            f.pack(fill='both',expand=1)
            # self.txt = Text(tab1,height=55)
            # self.txt.grid(row=0,column=0,sticky="ew")
            # sc = Scrollbar(tab1,orient='vertical',command=self.txt.yview)
            # sc.grid(row=0,column=1,sticky='ns')
            # self.txt['yscrollcommand'] = sc.set
            self.check_nothing_l = True
            self.nothinglabel = Label(self,foreground='gray',background='black',font=("None",20))
            self.nothinglabel.place(bordermode=INSIDE,x=400,y=210)
            self.welcome_label = Label(self.welcome,text='Black-Texteditor',font=("None",40),background='black',foreground='white')
            self.welcome_label.place(bordermode=INSIDE,x=300,y=35)
            github_link = HTMLLabel(self.welcome,html='<a href="https://github.com/mrprogrammer2938" target="_blank"> Github </a>')
            github_link.place(bordermode=INSIDE,x=20,y=530)
            instagram_link = HTMLLabel(self.welcome,html='<a href="https://instagram.com/black_software_company" target="_blank"> Instagram </a>')
            instagram_link.place(bordermode=INSIDE,x=90,y=530)
            website_link = HTMLLabel(self.welcome,html='<a href="https://black-software.ir" target="_blank"> Black </a>')
            website_link.place(bordermode=INSIDE,x=185,y=530)
            start = TButton(self.welcome,text='Start Project',command=self.new_tab)
            start.place(bordermode=OUTSIDE,x=350,y=120)
            newwindow = TButton(self.welcome,text='New Window',command=self.new)
            newwindow.place(bordermode=OUTSIDE,x=350,y=150)
            openfile = TButton(self.welcome,text='Open File',command=self.open_file)
            openfile.place(bordermode=OUTSIDE,x=350,y=180)
            devb = TButton(self.welcome,text='Dev',command=self.dev)
            devb.place(bordermode=OUTSIDE,x=350,y=210)
            feedback = TButton(self.welcome,text='Feedback',command=self.feedback)
            feedback.place(bordermode=OUTSIDE,x=350,y=240)
            exitb = TButton(self.welcome,text='Exit',command=self.ext)
            exitb.place(bordermode=OUTSIDE,x=350,y=270)
            self.nothinglabel = Label(self,foreground='gray',background='black',font=("None",20))
            self.nothinglabel.place(bordermode=INSIDE,x=400,y=210)
            self.welcome_date = open("welcome_date","w")
            self.welcome_date.write("True")
            self.welcome_date.close()
            self.hellomenucheck = True
        else:
            print()
            self.check_tab = True
            self.new_tab()
        self.o = True
        self.ch = IntVar()
        self.check_f = False
        self.chs = StringVar()  
        fontsize.add_radiobutton(label=10,command=self._10,variable=self.ch,value=10)
        fontsize.add_radiobutton(label=20,command=self._20,variable=self.ch,value=20)
        fontsize.add_radiobutton(label=30,command=self._30,variable=self.ch,value=30)
        fontsize.add_radiobutton(label=40,command=self._40,variable=self.ch,value=40)
        fontsize.add_radiobutton(label=50,command=self._50,variable=self.ch,value=50)
        fontsize.add_radiobutton(label=60,command=self._60,variable=self.ch,value=60)
        fontsize.add_radiobutton(label=70,command=self._70,variable=self.ch,value=70)
        fontsize.add_radiobutton(label=80,command=self._80,variable=self.ch,value=80)
        fontstyle.add_command(label='None',command=self.none_s)
        fontstyle.add_command(label='Broadway',command=self.Broadway)
        fontstyle.add_command(label='Bodoni MT',command=self.Bodoni_MT)
        fontstyle.add_command(label='Snap ITC',command=self.Snap_ITC)
        fontstyle.add_command(label='Small Fonts',command=self.Small_Fonts)
        fontstyle.add_command(label='Goudy Stout',command=self.Goudy_Stout)
        fontstyle.add_separator()
        fontstyle.add_command(label='Find',command=self.find_font)
        fontcolorfile.add_command(label='Black',command=self.fontblack)
        fontcolorfile.add_command(label='White',command=self.fontwhite)
        fontcolorfile.add_command(label='Costumize',command=self.fontcolor)
        # fontstyle.add_command(label='Broadway',command=s
        # fontsize.add_radiobutton()
        fontfile.add_cascade(label='Style',menu=fontstyle)
        fontfile.add_cascade(label='Size',menu=fontsize)
        fontfile.add_cascade(label='Color',menu=fontcolorfile) 
        themefile.add_command(label='Dark',command=self.dark)
        themefile.add_command(label='Light',command=self.light)
        themefile.add_separator()
        themefile.add_command(label='Costumize',command=self.costumize)
        helpfile.add_command(label='Help',command=self.help)
        helpfile.add_separator()
        helpfile.add_command(label='Send Feedback',command=self.feedback)
        menu.add_cascade(label='File',menu=filemenu)  
        menu.add_cascade(label='About',menu=aboutmenu)
        menu.add_cascade(label='Font',menu=fontfile)
        menu.add_cascade(label='Theme',menu=themefile)
        menu.add_cascade(label='Help',menu=helpfile)
        self.check_nl = False
        self.check_tab = False
        self.config(menu=menu)
        self.geometry("1000x600")
        self.check_s = "None"
        self.iconphoto(False,self.photo)
        self.mainloop()
    def help(self):
        webbrowser.open_new_tab('')
    def feedback(self):
        webbrowser.open_new_tab('https://black-software.ir/contact/')
    def close_all(self):
        f.destroy()
        if self.check_clear_s == True:
            self.txt.destroy()
            if self.check_nothing_l == True:
                self.nothinglabel.destroy()
            else:
                pass
        else:
            pass
        self.config(background='black')
        self.nothinglabel = Label(self,text='Nothing',foreground='gray',background='black',font=("None",20))
        self.nothinglabel.place(bordermode=INSIDE,x=400,y=210)
        self.check_tab = True
        self.check_nl = True
        self.hellomenucheck = False
    def close_all_2(self,x):
        f.destroy()
        if self.check_clear_s == True:
            self.txt.destroy()
            if self.check_nothing_l == True:
                self.nothinglabel.destroy()
            else:
                pass
        else:
            pass
        self.config(background='black')
        self.nothinglabel = Label(self,text='Nothing',foreground='gray',background='black',font=("None",20))
        self.nothinglabel.place(bordermode=INSIDE,x=400,y=210)
        self.check_tab = True
        self.check_nl = True
        self.hellomenucheck = False
    def new_tab(self):
        global tab1,f
        self.config(background='white')
        if self.check_nl == True:
           self.nothinglabel.destroy()
        else:
            print()
        if self.check_tab == True:
            self.config(background='white')
            if self.check_nothing_l == True:
                self.nothinglabel.destroy()
            else:
                pass
            if self.check_open_file == True:
                tab1 = Frame(f)
                f.add(tab1,text='Untitled')
                f.pack()
                self.check_clear_s = True
                self.txt = Text(tab1,height=150,width=210)
                self.txt.grid(row=0,column=0,sticky="ew")
                sc_2 = Scrollbar(tab1,orient='vertical',command=self.txt.yview)
                sc_2.grid(row=0,column=2,sticky='ns') 
                self.check_f = True
                self.check_tab = False
            else:
                f.destroy()
                f = Notebook(self)
                tab1 = Frame(f)
                f.add(tab1,text='Untitled')
                f.pack()
                self.check_clear_s = True
                self.txt = Text(tab1,height=150,width=210)
                self.txt.grid(row=0,column=0,sticky="ew")
                sc_2 = Scrollbar(tab1,orient='vertical',command=self.txt.yview)
                sc_2.grid(row=0,column=2,sticky='ns') 
                self.check_f = True
                self.check_tab = False
        else:
            if self.check_f == False:
                tab1 = Frame(f)
                f.add(tab1,text='Untitled')
                f.pack()
                self.check_clear_s = True
                self.txt = Text(tab1,height=150,width=210)
                self.txt.grid(row=0,column=1,sticky="ew")
                sc_3 = Scrollbar(tab1,orient='vertical',command=self.txt.yview)
                sc_3.grid(row=0,column=2,sticky='ns')    
            else:
                self.check_f = False
                tab1 = Frame(f)
                f.add(tab1,text='Untitled')
                f.pack()
                self.check_clear_s = True
                self.txt = Text(tab1,height=150,width=210)
                self.txt.grid(row=0,column=1,sticky="ew")
                sc = Scrollbar(tab1,orient='vertical',command=self.txt.yview)
                sc.grid(row=0,column=2,sticky='ns')
    def new_tab_2(self,x):
        global tab1,f
        self.config(background='white')
        if self.check_nl == True:
           self.nothinglabel.destroy()
        else:
            print()
        if self.check_tab == True:
            self.config(background='white')
            if self.check_nothing_l == True:
                self.nothinglabel.destroy()
            else:
                pass
            if self.check_open_file == True:
                tab1 = Frame(f)
                f.add(tab1,text='Untitled')
                f.pack()
                self.check_clear_s = True
                self.txt = Text(tab1,height=150,width=210)
                self.txt.grid(row=0,column=0,sticky="ew")
                sc_2 = Scrollbar(tab1,orient='vertical',command=self.txt.yview)
                sc_2.grid(row=0,column=2,sticky='ns') 
                self.check_f = True
                self.check_tab = False
            else:
                f.destroy()
                f = Notebook(self)
                tab1 = Frame(f)
                f.add(tab1,text='Untitled')
                f.pack()
                self.check_clear_s = True
                self.txt = Text(tab1,height=150,width=210)
                self.txt.grid(row=0,column=0,sticky="ew")
                sc_2 = Scrollbar(tab1,orient='vertical',command=self.txt.yview)
                sc_2.grid(row=0,column=2,sticky='ns') 
                self.check_f = True
                self.check_tab = False
        else:
            if self.check_f == False:
                tab1 = Frame(f)
                f.add(tab1,text='Untitled')
                f.pack()
                self.check_clear_s = True
                self.txt = Text(tab1,height=150,width=210)
                self.txt.grid(row=0,column=1,sticky="ew")
                sc_3 = Scrollbar(tab1,orient='vertical',command=self.txt.yview)
                sc_3.grid(row=0,column=2,sticky='ns')    
            else:
                self.check_f = False
                tab1 = Frame(f)
                f.add(tab1,text='Untitled')
                f.pack()
                self.check_clear_s = True
                self.txt = Text(tab1,height=150,width=210)
                self.txt.grid(row=0,column=1,sticky="ew")
                sc = Scrollbar(tab1,orient='vertical',command=self.txt.yview)
                sc.grid(row=0,column=2,sticky='ns')    
    def Goudy_Stout(self):
        self.txt.config(font=("Goudy Stout",self.ch.get()))
        self.check_s = "Goudy Stout"
    def Small_Fonts(self):
        self.txt.config(font=("Small Fonts",self.ch.get()))
        self.check_s = "Small Fonts"
    def fontblack(self):
        self.txt.config(foreground='black')
    def fontwhite(self):
        self.txt.config(foreground='white')
    def Snap_ITC(self):
        self.txt.config(font=("Snap ITC",self.ch.get()))
        self.check_s = "Snap ITC"
    def Bodoni_MT(self):
        self.txt.config(font=("Bodoni MT",self.ch.get()))
        self.check_s = "Bodoni MT"
    def find_font(self):
        window3 = Tk()
        window3.title('Black-texteditor/font/Find')
        fontinput = Entry(window3,borderwidth=3)
        fontinput.place(bordermode=OUTSIDE,x=80,y=20)
        submit_b = Button(self,text='Submit',command=self.submit_font)
        linklabel = HTMLLabel(window3,html='<a href="http://www.github.com/mrprogrammer2938"> Github </a>')
        linklabel.place(bordermode=INSIDE,x=20,y=180)
        window3.geometry("500x400")
        window3.mainloop()
    def submit_font(self):
        self.font_file = open("./Font/font.txt","r").read()
    def Broadway(self):
        self.txt.config(font=("Broadway",self.ch.get()))
        self.check_s = "Broadway"
    def none_s(self):
        self.txt.config(font=("None",self.ch.get()))
        self.check_s = "None"
    def _10(self):
        self.txt.config(font=(self.check_s,10))
    def _20(self):
        self.txt.config(font=(self.check_s,20))
    def _30(self):
        self.txt.config(font=(self.check_s,30))
    def _40(self):
        self.txt.config(font=(self.check_s,40))
    def _50(self):
        self.txt.config(font=(self.check_s,50))
    def _60(self):
        self.txt.config(font=(self.check_s,60))
    def _70(self):
        self.txt.config(font=(self.check_s,70))
    def _80(self):
        self.txt.config(font=(self.check_s,80))
    def _90(self):
        self.txt.config(font=(self.check_s,90))
    def _100(self):
        self.txt.config(font=(self.check_s,100))    
    def fontcolor(self):
        font_color = askcolor(title='Choose Color')
        self.txt.config(foreground=font_color[1])
    def dark(self):
        try:
            self.txt.config(background='black',foreground='green')
        except AttributeError:            
            print(False)
    def light(self):
        try:
            self.txt.config(background='white',foreground='black')
        except AttributeError:
            print(False)
    def costumize(self):
        color = askcolor(title='Choose Color')
        # print(color)
        if color[1] == '#ffffff': 
            self.txt.config(background=color[1],foreground='black')
        elif color[1] == '#000000' or color[1] == '#606060' or color[1] == '#400000' or color[1] == '#000040' or color[1] == '#400040' or color[1] == '#000040' or color[1] == '#000080' or color[1] == '#004040' or color[1] == '#004000' or color[1] == '#004080':
            self.txt.config(background=color[1],foreground='white')
        else:
            self.txt.config(background=color[1])
    def black(self):
        webbrowser.open_new_tab('https://black-software.ir')
    def dev(self):
        webbrowser.open_new_tab('https://github.com/mrprogrammer2938')
    def tools(self):
        webbrowser.open_new_tab('https://github.com/black-software-com')
    def license(self):
        global window2
        window2 = Tk()
        window2.title('Black-Texteditor/License')
        window2.geometry("600x400")
        window2.resizable(0,0)
        menu = Menu(window2)
        filemenu = Menu(menu,tearoff=0)
        filemenu.add_command(label='Exit',accelerator='Ctrl+F4',command=self.ext_3)
        menu.add_cascade(label='File',menu=filemenu)
        window2.config(menu=menu)
        license_file = open("License.txt","r").read()
        license_txt = ScrolledText(window2)
        license_txt.pack()
        license_txt.insert(END,str(license_file))
        license_txt['state'] = 'disabled'
        window2.mainloop()
    def ext_3(self):
        window2.destroy()
        window2.quit()
    def new(self):
        global window
        self.i = False
        window = Tk()
        window.title('Black Texteditor')
        window.geometry("660x600")
        window.resizable(0,0)
        if self.check_open_file == True:
            pass
        else:
            self.txt2 = Text(window,height=50)
            self.txt2.grid(row=0,column=0,sticky="ew")
            sc2 = Scrollbar(window,orient='vertical',command=self.txt2.yview)
            sc2.grid(row=0,column=1,sticky='ns')
            self.txt2['yscrollcommand'] = sc2.set
        menu = Menu(window)
        filemenu = Menu(menu,tearoff=0)
        filemenu.add_command(label='New',accelerator='Ctrl+N',command=self.new)
        filemenu.add_command(label='Open',accelerator='Ctrl+O',command=self.open_file_2)
        filemenu.add_command(label='Save',accelerator='Ctrl+S',command=self.save_2)
        filemenu.add_command(label='Save As',accelerator='Ctrl+l',command=self.save_as_3)
        filemenu.add_separator()
        filemenu.add_command(label='Exit',accelerator='Ctrl+F4',command=self.ext_4)      
        menu.add_cascade(label='File',menu=filemenu)
        window.bind("<Control-n>",lambda x: self.new_2(x))
        window.bind("<Control-o>",lambda x: self.open_file_3(x))
        window.bind("<Control-s>",lambda x: self.save_3(x))
        window.bind("<Control-l>",lambda x: self.save_as_3)
        window.config(menu=menu)  
        window.mainloop()
    def new_2(self,x):
        global window
        self.i = False
        window = Tk()
        window.title('Black Texteditor')
        window.geometry("660x600")
        window.resizable(0,0)
        if self.check_open_file == True:
            pass
        else:
            self.txt2 = Text(window,height=50)
            self.txt2.grid(row=0,column=0,sticky="ew")
            sc2 = Scrollbar(window,orient='vertical',command=self.txt2.yview)
            sc2.grid(row=0,column=1,sticky='ns')
            self.txt2['yscrollcommand'] = sc2.set
        menu = Menu(window)
        filemenu = Menu(menu,tearoff=0)
        filemenu.add_command(label='New',accelerator='Ctrl+N',command=self.new)
        filemenu.add_command(label='Open',accelerator='Ctrl+O',command=self.open_file_2)
        filemenu.add_command(label='Save',accelerator='Ctrl+S',command=self.save_2)
        filemenu.add_command(label='Save As',accelerator='Ctrl+l',command=self.save_as_3)
        filemenu.add_separator()
        filemenu.add_commd(label='Exit',accelerator='Ctrl+F4',command=self.ext_4)      
        menu.add_cascade(label='File',menu=filemenu)
        window.bind("<Control-n>",lambda x: self.new_2(x))
        window.bind("<Control-o>",lambda x: self.open_file_3(x))
        window.bind("<Control-s>",lambda x: self.save_3(x))
        window.bind("<Control-l>",lambda x: self.save_as_3(x))
        window.config(menu=menu)  
        window.mainloop()
    def open_file_2(self):
        try:
            self.file_3 = filedialog.askopenfile(title='Select File',mode="r")
            t_2 = self.file_3.read()
            self.file_3.close()
            self.title(f'Black-Texteditor/{self.file_3.name}')
            f.tab("current",text=[f"{self.file_3.name}"])
            self.i = True
            self.e = False
            self.txt2.destroy()
            self.txt2 = Text(tab1,height=50)
            self.txt2.grid(row=0,column=0,sticky="ew")
            sc2 = Scrollbar(tab1,orient='vertical',command=self.txt2.yview)
            sc2.grid(row=0,column=1,sticky='ns')
            self.txt2['yscrollcommand'] = sc2.set
            self.txt2.insert(END,t_2)
            self.i_3 = True
        except (AttributeError,FileNotFoundError):
            self.i = False
            print(False)
    def save_as_3(self):
        self.file_save_4 = filedialog.asksaveasfile(title='Save As')
        self.file_save_4.write(str(self.txt2.get(1.0,END)))
        self.file_save_4.close()
        self.title(f'Black-Texteditor/{self.file_save_4.name}')
    def save_2(self):
        global file_save_3
        if self.i_3 == True:
            self.file_save_3 = open(self.file_save_4.name,"w")
            self.file_save_3.write(str(self.self.txt2.get(1.0,END)))
            self.file_save_3.close()
            self.title(f'Black-Texteditor/{self.file_save_3.name}')
            f.tab("current",text=[f"{self.file_save_3.name}"])
        else:
            self.file_save_3 = filedialog.asksaveasfile(title='Save As',mode="w")
            self.file_save_3.write(str(self.txt3.get(1.0,END)))
            self.file_save_3.close()
            self.title(f'Black-Texteditor/{self.file_save_3.name}')
            f.tab("current",text=[f"{self.file_save_3.name}"])
            self.i_3 = True
    def ext_4(self):
        window.destroy()
        window.quit()
    def open_file(self):
        global f,tab1
        try:
            if self.o == False:
                self.file_4 = filedialog.askopenfile(title='Select File',mode="r+")
                t = self.file_4.read()
                self.file_4.close()
                self.txt.insert(END,t)
                self.title(f'Black-Texteditor/{self.file_4.name}')
                tab1.config(text=[f"{self.file_4.name}"])
                self.check_open_file = True
                self.i = True
            else:
                if self.check_tab == True:
                    self.file_4 = filedialog.askopenfile(title='Select File',mode="r+")
                    t = self.file_4.read()
                    self.file_4.close()
                    f = Notebook(self)
                    tab1 = Frame(f)
                    f.add(tab1,text=self.file_4.name)
                    f.pack()
                    self.check_open_file = True
                    # self.txt.destroy()
                    self.txt = Text(tab1,height=210,width=200)
                    self.txt.grid(row=0,column=0,sticky="ew")
                    sc = Scrollbar(tab1,orient='vertical',command=self.txt.yview)
                    sc.grid(row=0,column=1,sticky='ns')
                    self.title(f'Black-Texteditor/{self.file_4.name}')
                    f.tab("current",text=[f"{self.file_4.name}"])
                    # tab1.config(text=[f"{self.file_4.name}"])
                    if self.check_nl == False:
                        pass
                    else:
                        self.welcome.destroy()
                    self.txt['yscrollcommand'] = sc.set
                    self.txt.insert(END,t)
                    self.i = True
                    self.o = True
                else:
                    self.file_4 = filedialog.askopenfile(title='Select File',mode="r+")
                    t = self.file_4.read()
                    self.file_4.close()
                    f.add(tab1,text=self.file_4.name)
                    f.pack()
                    self.check_open_file = True
                    # self.txt.destroy()
                    self.txt = Text(tab1,height=210,width=200)
                    self.txt.grid(row=0,column=0,sticky="ew")
                    sc = Scrollbar(tab1,orient='vertical',command=self.txt.yview)
                    sc.grid(row=0,column=1,sticky='ns')
                    self.title(f'Black-Texteditor/{self.file_4.name}')
                    f.tab("current",text=[f"{self.file_4.name}"])
                    if self.welcome_date:
                        self.welcome.destroy()
                    else:
                        pass
                    self.txt['yscrollcommand'] = sc.set
                    self.txt.insert(END,t)
                    self.i = True
                    self.o = True
        except (AttributeError) as err:
            print(err)
            self.check_open_file = False
    def open_file_3(self,x):
        global f,tab1
        try:
            if self.o == False:
                self.file_4 = filedialog.askopenfile(title='Select File',mode="r+")
                t = self.file_4.read()
                self.file_4.close()
                self.txt.insert(END,t)
                self.title(f'Black-Texteditor/{self.file_4.name}')
                tab1.config(text=[f"{self.file_4.name}"])
                self.check_open_file = True
                self.i = True
            else:
                if self.check_tab == True:
                    self.file_4 = filedialog.askopenfile(title='Select File',mode="r+")
                    t = self.file_4.read()
                    self.file_4.close()
                    f = Notebook(self)
                    tab1 = Frame(f)
                    f.add(tab1,text=self.file_4.name)
                    f.pack()
                    self.check_open_file = True
                    # self.txt.destroy()
                    self.txt = Text(tab1,height=210,width=200)
                    self.txt.grid(row=0,column=0,sticky="ew")
                    sc = Scrollbar(tab1,orient='vertical',command=self.txt.yview)
                    sc.grid(row=0,column=1,sticky='ns')
                    self.title(f'Black-Texteditor/{self.file_4.name}')
                    f.tab("current",text=[f"{self.file_4.name}"])
                    # tab1.config(text=[f"{self.file_4.name}"])
                    if self.check_nl == False:
                        pass
                    else:
                        self.welcome.destroy()
                    self.txt['yscrollcommand'] = sc.set
                    self.txt.insert(END,t)
                    self.i = True
                    self.o = True
                else:
                    self.file_4 = filedialog.askopenfile(title='Select File',mode="r+")
                    t = self.file_4.read()
                    self.file_4.close()
                    f.add(tab1,text=self.file_4.name)
                    f.pack()
                    self.check_open_file = True
                    # self.txt.destroy()
                    self.txt = Text(tab1,height=210,width=200)
                    self.txt.grid(row=0,column=0,sticky="ew")
                    sc = Scrollbar(tab1,orient='vertical',command=self.txt.yview)
                    sc.grid(row=0,column=1,sticky='ns')
                    self.title(f'Black-Texteditor/{self.file_4.name}')
                    f.tab("current",text=[f"{self.file_4.name}"])
                    if self.welcome_date:
                        self.welcome.destroy()
                    else:
                        pass
                    self.txt['yscrollcommand'] = sc.set
                    self.txt.insert(END,t)
                    self.i = True
                    self.o = True
        except (AttributeError) as err:
            print(err)
            self.check_open_file = False
    def save_2(self):
        self.e = None
        if self.i == True:
            if self.e == True:
                self.file_save_2 = open(self.file_save_2.name,"r+")
                self.file_save_2.write(str(self.txt2.get(1.0,END)))
                self.file_save_2.close()
                self.title(f'Black-Texteditor/{self.file_save_2.name}')
                f.tab("current",text=[f"{self.file_save_2.name}"])
            else:
                self.file_save_2 = open(self.file_3.name,"r+")
                self.file_save_2.write(str(self.txt2.get(1.0,END)))
                self.file_save_2.close()
                self.title(f'Black-Texteditor/{self.file_save_2.name}')
                f.tab("current",text=[f"{self.file_save_2.name}"])
        else:
            try:
                self.file_save_2 = filedialog.asksaveasfile(title='Save As',mode="w")
                self.file_save_2.write(str(self.txt2.get(1.0,END)))
                self.file_save_2.close()
                self.title(f'Black-Texteditor/{self.file_save_2.name}')
                f.tab("current",text=[f"{self.file_save_2.name}"])
                self.i = True
                self.e = True
            except (AttributeError,FileNotFoundError):
                self.e = False
                print(False)    

    def save_as_2(self):
        self.file_save_3 = filedialog.asksaveasfile(title='Save As')
        self.file_save_3.write(str(self.txt2.get(1.0,END)))
        self.file_save_3.close()
        self.title(f'Black-Texteditor/{self.file_save_3.name}')
        f.tab("current",text=[f"{self.file_save_3.name}"])
    def ext_2(self):
        self.destroy()
        self.quit()
        quit()
    def save(self):
        global file_save
        if self.i == True:
            self.file_save_5 = open(self.file_4.name,"r+")
            self.file_save_5.write(str(self.txt.get(1.0,END)))
            self.file_save_5.close()
            self.title(f'Black-Texteditor/{self.file_save_5.name}')
            f.tab("current",text=[f"{self.file_save_5.name}"])
        else:
            try:
                self.file_save = filedialog.asksaveasfile(title='Save As',mode="w")
                self.file_save.write(str(self.txt.get(1.0,END)))
                self.file_save.close()
                self.title(f'Black-Texteditor/{self.file_save.name}')
                f.tab("current",text=[f"{self.file_save.name}"])
                self.i = True
            except (AttributeError,FileNotFoundError):
                print(False)
    def save_3(self,x):
        global file_save
        if self.i == True:
            self.file_save_5 = open(self.file_4.name,"r+")
            self.file_save_5.write(str(self.txt.get(1.0,END)))
            self.file_save_5.close()
            self.title(f'Black-Texteditor/{self.file_save_5.name}')
            f.tab("current",text=[f"{self.file_save_5.name}"])
        else:
            try:
                self.file_save = filedialog.asksaveasfile(title='Save As',mode="w")
                self.file_save.write(str(self.txt.get(1.0,END)))
                self.file_save.close()
                self.title(f'Black-Texteditor/{self.file_save.name}')
                f.tab("current",text=[f"{self.file_save.name}"])
                self.i = True
            except (AttributeError,FileNotFoundError):
                print(False)
    # def save_2(self):
    #     if self.i_2 == True:
    #         self.file_save_2 = open(file.name,"r+")
    #         self.file_save_2.write(str(self.txt2.get(1.0,END)))
    #         self.file_save_2.close()
    #     else:
    #         self.file_save_2 = filedialog.asksaveasfile(title='Save As',mode="r+")
    #         self.file_save_2.write(str(self.txt2.get(1.0,END)))
    #         self.file_save_2.close()
    #         self.i_2 = True
    def ext(self):
        self.destroy()
        self.quit()
        quit()
    def save_as(self):
        try:
            file_save = filedialog.asksaveasfile(title='Save As',mode="w")
            file_save.write(str(self.txt.get(1.0,END)))
            file_save.close()
            self.title(f'Black-Texteditor/{file_save.name}')
            if self.check_nl == False:
                pass
            else:
                f.tab("current",text=[f"{self.file_save.name}"])
        except (AttributeError,FileExistsError):
            print(False)
    def save_as_3(self,x):
        try:
            file_save = filedialog.asksaveasfile(title='Save As',mode="w")
            file_save.write(str(self.txt.get(1.0,END)))
            file_save.close()
            self.title(f'Black-Texteditor/{file_save.name}')
            if self.check_nl == False:
                pass
            else:
                f.tab("current",text=[f"{self.file_save.name}"])
        except (AttributeError,FileExistsError):
            print(False)
if __name__ == '__main__':
    window = black_texteditor()
# Black-Texteditor v1.0