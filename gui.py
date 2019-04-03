import sys
import os
from tkinter import *


window=Tk()
window.title("AvFi")
window.geometry('300x350')
window.configure(background='lightgray')

w = Label(window, text="Welkom, ik ben AvFi.")
w.place(relx=0.5, rely=0.1, anchor=CENTER)
w.configure(background='lightgray')


def face_create_dataset():
    print('\n'*14)
    import a_toevoegen_nieuwe_lln
    a_toevoegen_nieuwe_lln.main()
    print("Train zodat je in de database komt en ik je kan herkennen :)")
a = Button(window, text="Toevoegen nieuwe lln", bg="dimgray", fg="white",command=face_create_dataset)
a.place(relx=0.5, rely=0.20, anchor=CENTER)



def face_train():
    print('\n'*14)
    try:
        import b_face_train
        b_face_train.main()
    except:
        print("Waarschijnlijk geen lln in het systeem, voeg eerst een nieuwe lln toe")
    from tkinter import messagebox
    messagebox.showinfo("Popup", "Alles is getrained")
    os.system('cls' if os.name=='nt' else 'clear')

b = Button(window, text="Trainen", bg="dimgray", fg="white",command=face_train)
b.place(relx=0.5, rely=0.3, anchor=CENTER)


def gezichten():
    print('\n'*14)
    import c_face_recognition
    c_face_recognition.main()
    os.system('cls' if os.name=='nt' else 'clear')
c = Button(window, text="Herkennen", bg="dimgray", fg="white",command=gezichten)
c.place(relx=0.5, rely=0.4, anchor=CENTER)


def inforamtie_opvragen():
    print("nog helaas niet beschikbaar")
d = Button(window, text="Info presentie vandaag", bg="dimgray", fg="white",command=inforamtie_opvragen)
d.place(relx=0.5, rely=0.6, anchor=CENTER)


def inforamtie_opvragen():
    print("nog helaas niet beschikbaar")
f = Button(window, text="Info domein-uren leerling", bg="dimgray", fg="white",command=inforamtie_opvragen)
f.place(relx=0.5, rely=0.7, anchor=CENTER)






def Help():
    from tkinter import messagebox
    messagebox.showinfo("Help popup", "Ik ben AvFi. Een app om leerlingen te registreren.\n"
                                      "Om te beginnen kies Toevoegen nieuwe lln.\nVerdere instructies volgen.\n "
                                      "Ik vraag je om op de foto te gaan en informatie te delen.Informatie die voor niemand anders beschikbaar zal zijn.\n "
                                      "Voor verdere vragen mail: erencantatar@gmail.com")
e = Button(window, text="Help", bg="dimgray", fg="white",command=Help)
e.place(relx=0.5, rely=0.9, anchor=CENTER)



window.mainloop()
