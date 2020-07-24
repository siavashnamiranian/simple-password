from tkinter import *
import random

def password_creator(v):
    weak = ['a','b', 'c', 'd', 'e', 'f','g','h','i','j',
            'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    medium = ['a','b', 'c', 'd', 'e', 'f','g','h','i','j',
            'k','l','m','n','o','p','q','r','s','t','u','v',
            'w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    strong = ['a','b', 'c', 'd', 'e', 'f','g','h','i','j',
            'k','l','m','n','o','p','q','r','s','t','u','v',
            'w','x','y','z','1','2','3','4','5','6','7','8',
            '9','0','/','#','-','_','%','&','@','$']
    if str(var.get())=="1":
        p =  "".join(random.sample(weak,int(v)))
        label.config(text = p)
    elif str(var.get())=="2":
        p =  "".join(random.sample(medium,int(v)))
        label.config(text = p)
    elif str(var.get())=="3":
        p =  "".join(random.sample(strong,int(v)))
        label.config(text = p)
    else:
        label.config(text = "choose one of options")

#gui
root = Tk()
root.title("password creator")
root.geometry("300x200")
#scale
pass_lenght = DoubleVar() 
s1 = Scale( root, variable = pass_lenght, from_ = 5, to = 20, orient = HORIZONTAL, command = password_creator)
s1.pack(anchor = CENTER)
#scale

#radio button
var = IntVar(value=1)
r1 = Radiobutton(root, text = "weak", variable = var, value = 1)
r1.pack(anchor = W)

r2 = Radiobutton(root, text = "medium", variable = var, value = 2)
r2.pack(anchor = W)

r3 = Radiobutton(root, text = "hard", variable = var, value = 3 )
r3.pack(anchor = W)

label = Label(root)
label.pack()
root.mainloop()
