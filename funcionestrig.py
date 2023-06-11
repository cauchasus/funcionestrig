import matplotlib.pyplot as plt
import numpy as np
import math

pi = math.pi

print("Welcome to FUNTRIG")

print(" ")
print(" ")

print("Enter your A")
a = float(input())
print("Enter your B")
b = float(input())
print("Enter your C")
c = float(input())
print("Enter your D")
D = float(input())

amplitud = a
periodo = (float(2) * pi / float(b))
anguloDeFase = (float(c) / float(b))
desplazamientoEnY = D
incrementos = periodo / 4


yes = ["yes", "si", "y", "s"] 
no = ["no", "n"]

sincos = ["seno", "sin", "cos", "coseno", "sen"]



def main():




    respuestaSemi = ("AMP = ", amplitud, "PER = ", periodo,
                     "FasAng = ", anguloDeFase, "YMovement = ", desplazamientoEnY)

    print("Do you want the values for you to make your own graph? (y/n)")
    respuestaValores = input()

    if respuestaValores.lower() in yes:
        print(respuestaSemi)
        pregGraf()

    elif respuestaValores.lower() in no:

        print("Ok sure, lets move on")
        pregGraf()


def pregGraf():
    print("Do you want me to graph? (y / n)")
    respuestaGraf = input()

    if respuestaGraf.lower() in yes:
        print("Ok sure, lets graph")
        enterSinCos()
    elif respuestaGraf.lower() in no:
        print("Ok, Goodbye")
    else:
        print("You entered something wrong, try again")
        pregGraf()

sini = ["sin", "sen", "seno"]
cosi = [ "cos", "coseno"]

def enterSinCos():
    print("Seno o Coseno")
    global eleccionsoc
    eleccionsoc = input()
    if eleccionsoc.lower() in sincos:
        print("Ok sure, lets move on")
        graph()
    else:
        print("You entered data wrong")
        
def graph():
    if eleccionsoc in sini:
        x = np.linspace(0, 2*np.pi, 100)
        y = a*np.sin(b*x - c*np.pi) + D
        
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()
    elif eleccionsoc in cosi:
        x = np.linspace(0, 2*np.pi, 100)
        y = a*np.cos(b*x - c*np.pi) + D
        
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()
    
    

main()
