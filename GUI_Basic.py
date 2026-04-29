import tkinter as tk 
from tkinter import messagebox
from PIL import Image, ImageTk
import random



#Grundlegendes Fenster
root = tk.Tk()                                                   
root.title("GUI Test Schach Widner Exenb.")

#Layout
Hauptrahmen = tk.Frame(root)
Hauptrahmen.pack()

#Zeichenfläche 
Zeichenfläche = tk.Canvas(Hauptrahmen, width=400, height=400)
Zeichenfläche.grid(row=0, column=0)

feld = 50

#Brett zeichnen
for row in range(8):
    for col in range(8):
        color = "white" if (row + col) % 2 == 0 else "black"
        Zeichenfläche.create_rectangle(col*feld, row*feld,
                                (col+1)*feld, (row+1)*feld,
                                fill=color)

#Rechte Seite
Rahmen_rechts = tk.Frame(Hauptrahmen)
Rahmen_rechts.grid(row=0, column=1, padx=20, sticky="n")

title = tk.Label(Rahmen_rechts, text="SCHACH", font=("Arial", 20, "bold"))
title.pack(pady=10)

opponent_label = tk.Label(Rahmen_rechts, text="Gegner: INOP", font=("Arial", 14))
opponent_label.pack(pady=10)

#Knöpfe
def reset():
    global x, y
    x, y = 0, 0
    Zeichenfläche.coords(figur, x*feld + feld//2, y*feld + feld//2)

def close():
    root.destroy()

Knopf_Rahmen = tk.Frame(Rahmen_rechts)
Knopf_Rahmen.pack(side="bottom", anchor="e", pady=10)

def ragequit():
    messagebox.showwarning("Ragequit", "Take the L")

    #Figuren wild durch die gegend schiessen
    Hauptrahmen.configure(bg="red")

    for _ in range(15):
        x = random.randint(0, 7)
        y = random.randint(0, 7)

        Zeichenfläche.coords(
            figur,
            x*feld + feld//2,
            y*feld + feld//2
        )
        Zeichenfläche.update()
        root.after(50)  # kleine Pause für Effekt

    # Ende
    root.destroy()

reset_Knopf = tk.Button(
    Knopf_Rahmen,
    text="Zurücksetzen",
    bg="green",
    fg="white",
    width=15,
    command=reset
)
reset_Knopf.pack(pady=5, anchor="e")

close_Knopf = tk.Button(
    Knopf_Rahmen,
    text="Fenster schließen",
    bg="red",
    fg="white",
    width=15,
    command=close
)
close_Knopf.pack(pady=5, anchor="e")


rage_Knopf = tk.Button(
    Knopf_Rahmen,
    text="RAGEQUIT",
    bg="black",
    fg="red",
    width=15,
    command=ragequit
)
rage_Knopf.pack(pady=5, anchor="e")
# Startposition Figur
x, y = 0, 0

# Bild laden
img = Image.open("pawn.png")
img = img.resize((40, 40))
pawn_img = ImageTk.PhotoImage(img)

Zeichenfläche.image = pawn_img

# Figur anzeigen
figur = Zeichenfläche.create_image(x*feld + feld//2,
                            y*feld + feld//2,
                            image=pawn_img)

# Bewegung
def Bewegung(event):
    global x, y

    col = event.x // feld
    row = event.y // feld

    if 0 <= col < 8 and 0 <= row < 8:
        x, y = col, row
        Zeichenfläche.coords(
            figur,
            x*feld + feld//2,
            y*feld + feld//2
        )
Zeichenfläche.bind("<Button-1>", Bewegung)

root.mainloop()