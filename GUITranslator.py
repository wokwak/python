# GUITranslator.py
from tkinter import *
#from library anme tkinter, * is all features
from tkinter import ttk #ttk is theme of tk
#---------------------------------
from googletrans import Translator
translator = Translator()
    
GUI = Tk() #make main window
GUI.geometry('500x300') #width x height
GUI.title('BunBun Translator')

#--------Config---------
FONT = ('Angsana New',15)

# -------Label----------
L = ttk.Label(GUI,text='Please enter',font=FONT)
L.pack()


# -------Data Entry----------
v_vocab = StringVar()
E1 = ttk.Entry(GUI,textvariable=v_vocab,font=FONT,widt=40)
E1.pack(ipady=20)


# -------Button----------
def Translate() :
    vocab = v_vocab.get()
    meaning = translator.translate(vocab,dest='th')
    print(vocab +' : ' +meaning.text)
    print(meaning.pronunciation)
    v_result.set(vocab +' : ' +meaning.text)
    
B1 = ttk.Button(GUI,text='Translate',command=Translate) #สร้างปุ่มขึ้นมา
B1.pack(ipadx=20,ipady=10) #button size

# -------Label----------
L = ttk.Label(GUI,text='Meaning',font=FONT)
L.pack()

# -------Result----------
v_result = StringVar()
FONT2=('Angsana New',20)
R1 = ttk.Label(GUI,textvariable=v_result,font=FONT2,foreground='green')
R1.pack()


# -------Button----------

# -------Button----------

# -------Button----------

GUI.mainloop() #make program forever run util close
