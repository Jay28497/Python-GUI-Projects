import pygame, pygame.mixer
import sys
from tkinter import*

pygame.init()

def clear():
    texDisplay.delete(0, END)
    num1.set(0)
    return


def value_Cs():
    num1.set("C#")
    sound = pygame.mixer.Sound("1.wav")
    sound.play()
    return


def value_Ds():
    num1.set("D#")
    sound = pygame.mixer.Sound("2.wav")
    sound.play()
    return


def value_Fs():
    num1.set("F#")
    sound = pygame.mixer.Sound("3.wav")
    sound.play()
    return


def value_Gs():
    num1.set("G#")
    sound = pygame.mixer.Sound("4.wav")
    sound.play()
    return


def value_Bb():
    num1.set("Bb")
    sound = pygame.mixer.Sound("5.wav")
    sound.play()
    return


def value_Cs1():
    num1.set("C#1")
    sound = pygame.mixer.Sound("6.wav")
    sound.play()
    return


def value_Ds1():
    num1.set("D#1")
    sound = pygame.mixer.Sound("7.wav")
    sound.play()
    return


def value_C():
    num1.set("C")
    sound = pygame.mixer.Sound("8.wav")
    sound.play()
    return


def value_D():
    num1.set("D")
    sound = pygame.mixer.Sound("9.wav")
    sound.play()
    return


def value_E():
    num1.set("E")
    sound = pygame.mixer.Sound("10.wav")
    sound.play()
    return


def value_F():
    num1.set("F")
    sound = pygame.mixer.Sound("11.wav")
    sound.play()
    return


def value_G():
    num1.set("G")
    sound = pygame.mixer.Sound("12.wav")
    sound.play()
    return


def value_A():
    num1.set("A")
    sound = pygame.mixer.Sound("13.wav")
    sound.play()
    return


def value_B():
    num1.set("B")
    sound = pygame.mixer.Sound("14.wav")
    sound.play()
    return


def value_C1():
    num1.set("C1")
    sound = pygame.mixer.Sound("15.wav")
    sound.play()
    return


def value_D1():
    num1.set("D1")
    sound = pygame.mixer.Sound("16.wav")
    sound.play()
    return


def value_E1():
    num1.set("E1")
    sound = pygame.mixer.Sound("17.wav")
    sound.play()
    return


def value_F1():
    num1.set("F1")
    sound = pygame.mixer.Sound("18.wav")
    sound.play()
    return



root = Tk()
frame = Frame(root)
frame.pack()

root.title('PIANO')

num1 = StringVar()
num1.set(0)
num2 = StringVar()
operator = StringVar()

topframe = Frame(root)
topframe.pack(side = TOP)
txtDisplay = Entry(frame, textvariable=num1, bd=20, insertwidth=1, font=30, justify='right', width=4)
txtDisplay.pack(side =TOP)


button1 = Button(topframe, padx=8, height=6, pady=8, bd=8, text="C#", bg="black", fg="white", command=value_Cs)
button1.pack(side = LEFT)
button22 = Button(topframe, state=DISABLED, height=8, width=1, relife=RIDGE)
button22.pack(side = LEFT)

button2 = Button(topframe, padx=8, height=6, pady=8, bd=8, text="D#", bg="black", fg="white", command=value_Ds)
button2.pack(side = LEFT)
button22 = Button(topframe, state=DISABLED, height=8, width=1, relife=RIDGE)
button22.pack(side = LEFT)

button3 = Button(topframe, padx=8, height=6, pady=8, bd=8, text="F#", bg="black", fg="white", command=value_Fs)
button3.pack(side = LEFT)
button22 = Button(topframe, state=DISABLED, height=8, width=1, relife=RIDGE)
button22.pack(side = LEFT)

button4 = Button(topframe, padx=8, height=6, pady=8, bd=8, text="G#", bg="black", fg="white", command=value_Gs)
button4.pack(side = LEFT)
button22 = Button(topframe, state=DISABLED, height=8, width=1, relife=RIDGE)
button22.pack(side = LEFT)

button5 = Button(topframe, padx=8, height=6, pady=8, bd=8, text="Bb", bg="black", fg="white", command=value_Bb)
button5.pack(side = LEFT)
button22 = Button(topframe, state=DISABLED, height=8, width=1, relife=RIDGE)
button22.pack(side = LEFT)

button6 = Button(topframe, padx=8, height=6, pady=8, bd=8, text="C#1", bg="black", fg="white", command=value_Cs1)
button6.pack(side = LEFT)
button22 = Button(topframe, state=DISABLED, height=8, width=1, relife=RIDGE)
button22.pack(side = LEFT)

button7 = Button(topframe, padx=8, height=6, pady=8, bd=8, text="D#1", bg="black", fg="white", command=value_Ds1)
button7.pack(side = LEFT)


frame1 = Frame(root)
frame1.pack(side = TOP)


button1 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="C", fg="black", command=value_C)
button1.pack(side = LEFT)
button2 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="C", fg="black", command=value_D)
button2.pack(side = LEFT)
button3 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="C", fg="black", command=value_E)
button3.pack(side = LEFT)
button4 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="C", fg="black", command=value_F)
button4.pack(side = LEFT)
button5 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="C", fg="black", command=value_G)
button5.pack(side = LEFT)
button6 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="C", fg="black", command=value_A)
button6.pack(side = LEFT)
button7 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="C", fg="black", command=value_B)
button7.pack(side = LEFT)
button8 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="C", fg="black", command=value_C1)
button8.pack(side = LEFT)
button9 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="C", fg="black", command=value_D1)
button9.pack(side = LEFT)
button10 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="C", fg="black", command=value_E1)
button10.pack(side = LEFT)
button11 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="C", fg="black", command=value_F1)
button11.pack(side = LEFT)



root.mainloop()
