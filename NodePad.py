from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    Textarea.delete(1.0, END)
def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                            ("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        Textarea.delete(1.0, END)
        f = open(file, "r")
        Textarea.insert(1.0, f.read())
        f.close()

def savefile():
    global file
    if file == None:
        file=asksaveasfilename(initialfile='Untitled.txt',
                               defaultextension=".txt",
                               filetypes=[("All Files", "*.*"),
                                   ("Text Documents","*.txt")] )
        if file == "":
            file=None
        else:
            #save as a new file
            f = open(file,'w')
            f.write(Textarea.get(1.0,END)) #(1st line 0th column content write)
            f.close()

            root.title(os.path.basena(file) + "-Notepad")
            print("File Saved")
    else:
        #save the file
        f = open(file,'w')
        f.write(Textarea.get(1.0,END)) #(1st line 0th column content write)
        f.close()


def quitapp():
    root.destroy()

def cut():
    Textarea.event_generate(("<<Cut>>"))

def copy():
    Textarea.event_generate(("<<Copy>>"))

def paste():
    Textarea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Notepad with Rutuja")

if __name__ == '__main__':

    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("644x788")
    #add textarea
    Textarea = Text(root, font="lucida 13")
    file = None
    Textarea.pack(expand=True,fill=BOTH) #expand take all width 

    #Let's create menubar
    Menubar = Menu(root)
    #File menu starts
    filemenu = Menu(Menubar, tearoff=0)
    #To give features New, Open, Save, Exit
    #To open new file
    filemenu.add_command(label="New", command=newfile)

    #To open already existing file
    filemenu.add_command(label="Open", command=openfile)

    #To save the current file
    filemenu.add_command(label="Save", command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=quitapp)
    Menubar.add_cascade(label="File", menu=filemenu)
    #File menu ends

    #Edit menu starts
    Editmenu = Menu(Menubar, tearoff = 0)
    #To give a features of a cut, copy and paste
    Editmenu.add_command(label="Cut", command=cut)
    Editmenu.add_command(label="Copy", command=copy)
    Editmenu.add_command(label="Paste", command=paste)
    Menubar.add_cascade(label="Edit",menu=Editmenu)
    #Edit menu ends

    #Help menu start 
    Helpmenu = Menu(Menubar, tearoff=0)
    #To give features 
    Helpmenu.add_command(label="About Notepad", command=about)
    Menubar.add_cascade(label="Help", menu=Helpmenu)
    #Help menu ends




    root.config(menu=Menubar)

    #Add scrollbar
    scroll = Scrollbar(Textarea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=Textarea.yview)
    Textarea.config(yscrollcommand=scroll.set)



    root.mainloop()