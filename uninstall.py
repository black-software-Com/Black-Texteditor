#!/usr/bin/python3
# Black-Texteditor v1.0
import os,subprocess,platform
try:
    from tkinter import *
    from tkinter.ttk import *
    from tkinter.messagebox import showerror
except ImportError:
    subprocess.getoutput("pip uninstall tk-tools")

class black_texteditor(Tk):
    def __init__(self):
        super(black_texteditor,self).__init__()
        self.title('Black-Text/Uninstall')
        label_l = Label(self,text='Black-Textrditor',background='white',foreground='black',font=("None",15))
        label_l.place(bordermode=INSIDE,x=120,y=20)
        self.uninstall_b = Button(self,text='Uninstall',command=self.uninstall)
        self.uninstall_b.place(bordermode=OUTSIDE,x=160,y=110)
        self.exit_b = Button(self,text='Exit',command=self.ext)
        self.exit_b.place(bordermode=OUTSIDE,x=160,y=135)

        self.config(background='white')
        self.resizable(False,False)
        self.geometry("400x300")
        self.photo = PhotoImage(file = './Scr/black.png')
        self.iconphoto(False,self.photo)
        self.mainloop()
    def uninstall(self):
        global pr,label_progressbar
        label_progressbar = Label(self,text='Uninstalling...')
        label_progressbar.place(bordermode=INSIDE,x=105,y=40)
        pr = Progressbar(self,orient='horizontal',mode='determinate',length=200)
        pr.place(bordermode=INSIDE,x=105,y=65)
        pr.start(55)
        pr.after(6000,self.uninstall_2)
    def uninstall_2(self):
        if platform.system() == 'Linux':
            subprocess.getoutput("cd .. && rm -r Black-Texteditor")
            subprocess.getoutput("cd /usr/bin/local && rm black")
        else:
            subprocess.getoutput("cd .. && rm -r Black-Texteditor")
        label_progressbar.destroy()
        pr.stop()
        pr.destroy()
        label_mess = Label(self,text='Complete!',foreground='black',background='white')
        label_mess.place(bordermode=INSIDE,x=170,y=65)
        self.uninstall_b.destroy()
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