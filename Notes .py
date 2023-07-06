from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from tkinter import messagebox
import webbrowser

root = Tk()
root.maxsize(650, 650)
root.minsize(650, 650)
open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
run_img = ImageTk.PhotoImage(Image.open("run.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))
label_file_name = Label(root, text="File:")
label_file_name.place(relx=0.32,rely=0.03,anchor= CENTER)
input_file_name = Entry(root)
input_file_name.place(relx=0.5,rely=0.03, anchor= CENTER)
my_text= Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor= CENTER)




name = ""
def openFile():
    global name
    my_text.delete(1.0, END)
    input_file_name.delete(0, END)
    text_file = filedialog.askopenfilename(title = "Open HTML File", 
                                           filetypes=(("HTML Files", "*.html"),))
    print(text_file)
    name = os.path.basename(text_file)
    formated_name = name.split('.')[0]
    input_file_name.insert(END,formated_name)
    root.title(formated_name)
    text_file = open(name, 'r')
    paragraph=text_file.read()
    my_text.insert(END.paragraph)
    text_file.close()
    
def saveFile():
    input_name = input_file_name.get()
    file = open(input_name+".html","w")
    data = my_text.get("1.0", END)
    print(data)
    file.write(data)
    input_file_name.delete(0, END)
    my_text.delete(1.0, END)
    messagebox.showinfo("Update", "Success")
    
def runFile():
    global name
    webbrowser.open(name)
    
def exitFile():
    root.destroy()
    
open_button=Button(root,image = open_img, text="openfile", command=openFile)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)
save_button=Button(root, image = save_img,text="savefile", command=saveFile)
save_button.place(relx=0.11,rely=0.03,anchor= CENTER)
run_button=Button(root, image = run_img, text="runfile", command=runFile)
run_button.place(relx = 0.24, rely = 0.03, anchor = CENTER)
exit_button=Button(root, image = exit_img, text="exitfile", command=exitFile)
exit_button.place(relx=0.17,rely=0.03,anchor= CENTER)

root.mainloop()