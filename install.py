#!/usr/bin/python3
# Black-Texteditor v1.0
import os,subprocess,platform
try:
    from tkinter import *
    from tkinter.ttk import *
    from tkinter.messagebox import showerror
except ImportError:
    subprocess.getoutput("pip install tk-tools")

class black_texteditor(Tk):
    def __init__(self):
        super(black_texteditor,self).__init__()
        self.title('Black-Texteditor/Installing')
        label_l = Label(self,text='Black-Texteditor',background='white',foreground='black',font=("None",15))
        label_l.place(bordermode=INSIDE,x=120,y=20)
        self.install_b = Button(self,text='Install',command=self.install)
        self.install_b.place(bordermode=OUTSIDE,x=160,y=110)
        self.exit_b = Button(self,text='Exit',command=self.ext)
        self.exit_b.place(bordermode=OUTSIDE,x=160,y=135)

        self.config(background='white')
        self.resizable(False,False)
        self.geometry("400x300")
        self.photo = PhotoImage(file = './Scr/black.png')
        self.iconphoto(False,self.photo)
        self.mainloop()
    def install(self):
        global pr,label_progressbar
        label_progressbar = Label(self,text='Installing...')
        label_progressbar.place(bordermode=INSIDE,x=105,y=40)
        pr = Progressbar(self,orient='horizontal',mode='determinate',length=200)
        pr.place(bordermode=INSIDE,x=105,y=65)
        pr.start(55)
        pr.after(6000,self.install_2)
    def install_2(self):
        if platform.system() == 'Linux':
            if os.path.exists("./usr/local/bin"):
                subprocess.getoutput("chmod a+x black.py")
                os.system("mv black.py black")
                os.system("cp black /usr/local/bin")
            else:
                print(False)
        else:
            print(f"Os: {platform.system()}")
        label_progressbar.destroy()
        pr.stop()
        pr.destroy()
        label_mess = Label(self,text='Complete!',foreground='black',background='white')
        label_mess.place(bordermode=INSIDE,x=170,y=65)
        self.install_b.destroy()
        self.exit_b.place(bordermode=OUTSIDE,x=160,y=110)

    def ext(self):
        self.destroy()
        self.quit()
        quit()
if __name__ == '__main__':
    if platform.system() == 'Linux':
        if os.getuid() == 0:
          window = black_texteditor()
        else:
            showerror(title='Cannot Running',message='Please, Check Root!')
    else:
        window = black_texteditor()