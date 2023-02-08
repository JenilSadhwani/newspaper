from tkinter import *
from PIL import ImageTk,Image
#for line break
def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text += text[i]
        if i%100==0 and i!=0:
            final_text += "\n"
    return final_text


root = Tk()
root.title("The Jenil Times")
root.geometry("1000x334")

texts = []
photos =[]
for i in range(0, 2):
   with open(f"{i+1}.txt")as f:
        text = f.read()
        texts.append(every_100(text))
        
        image = Image.open(f"{i+1}.png")
        image = image.resize((225,225),Image.ANTIALIAS)
        photos.append(ImageTk.PhotoImage(image))

    
    
#title frame

f0 = Frame(root,width=800,height=70)
Label(f0,text="Jenil's news", font="lucida 33 bold").pack()
Label(f0,text="7 february 2023",font="lucida 15 bold").pack()
f0.pack()
#creating one frame
f1 = Frame(root,width=900,height=200,padx=20,pady=20)
Label(f1,text=texts[0]).pack(side=LEFT,padx=10,pady=20)
Label(f1,image=photos[0],anchor="w").pack()
f1.pack(anchor="w")

f2 = Frame(root,width=900,height=200,pady=34,padx=20)
Label(f2,text=texts[1]).pack(side=RIGHT,padx=10,pady=20)
Label(f2,image=photos[1],anchor="w").pack()
f2.pack(anchor="w")




root.mainloop()