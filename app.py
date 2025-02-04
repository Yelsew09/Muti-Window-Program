#IMPORTS#
import tkinter as tk
from tkinter import messagebox

def start_grapher():
    global root
    grapher = tk.Toplevel(root)
    grapher.geometry("300x300")
    grapher.resizable(False, False)
    grapher.title("grapher")
    grapher.configure(bg = "#085c00")
    tbxOne = tk.Entry(grapher)
    tbxTwo = tk.Entry(grapher)
    tbxThree = tk.Entry(grapher)
    tbxFour = tk.Entry(grapher)
    num1 = int(tbxOne.get())
    num2 = int(tbxTwo.get())
    num3 = int(tbxThree.get())
    num4 = int(tbxFour.get())

    def graph():
        global num1, num2, num3, num4
        graphwindow = tk.Toplevel(grapher)
        graphwindow.geometry("600, 400")
        graphCanvas = tk.Canvas(graphwindow, width = "550", height = "390", bg = "blue")
        graphwindow.resizable(True, False)
        
        lblGraphOne = tk.Label(graphwindow, text = "-")
        lblGraphTwo = tk.Label(graphwindow, text = "-")
        lblGraphThree = tk.Label(graphwindow, text = "-")
        lblGraphFour = tk.Label(graphwindow, text = "-")
        lblGraphFive = tk.Label(graphwindow, text = "-")
        lblGraphSix = tk.Label(graphwindow, text = "-")
        lblGraphSeven = tk.Label(graphwindow, text = "-")
        lblGraphEight = tk.Label(graphwindow, text = "-")
        lblGraphNine = tk.Label(graphwindow, text = "-")
        lblGraphTen = tk.Label(graphwindow, text = "-")
        lblGraphZero = tk.Label(graphwindow, text = "-")

        def draw_lines():
            graphCanvas.create_line(0,42, 550,42, width = 2)
            graphCanvas.create_line(0,81, 550,81, width = 2)
            graphCanvas.create_line(0,120, 550,120, width = 2)
            graphCanvas.create_line(0,158, 550,158, width = 2)
            graphCanvas.create_line(0,197, 550,197, width = 2)
            graphCanvas.create_line(0,236, 550,236, width = 2)
            graphCanvas.create_line(0,275, 550,275, width = 2)
            graphCanvas.create_line(0,314, 550,314, width = 2)
            graphCanvas.create_line(0,353, 550,353, width = 2)
        
        
        unit = max(num1, num2, num3, num4)
        unit = unit/10
                
        #Updating labels to show units
        lblGraphOne.config(text = str(round(unit*10,1)))
        lblGraphTwo.config(text = str(round(unit*9,1)))
        lblGraphThree.config(text = str(round(unit*8,1)))
        lblGraphFour.config(text = str(round(unit*7,1)))
        lblGraphFive.config(text = str(round(unit*6,1)))
        lblGraphSix.config(text = str(round(unit*5,1)))
        lblGraphSeven.config(text = str(round(unit*4,1)))
        lblGraphEight.config(text = str(round(unit*3,1)))
        lblGraphNine.config(text = str(round(unit*2,1)))
        lblGraphTen.config(text = str(round(unit,1)))
        lblGraphZero.config(text = "0")

        #Drawing the bars
        num1 = num1/unit
        num1 = num1*39
        num2 = num2/unit
        num2 = num2*39
        num3 = num3/unit
        num3 = num3*39
        num4 = num4/unit
        num4 = num4*39
        graphCanvas.create_rectangle(50,550, 125,390 - num1, fill = "red")
        graphCanvas.create_rectangle(175, 550, 250, 390 - num2, fill = "green")
        graphCanvas.create_rectangle(300, 550, 375, 390 - num3, fill = "yellow")
        graphCanvas.create_rectangle(425, 550, 500, 390 - num4, fill = "purple")
    
    def clear():
        

    tk.Button(grapher, text = "Graph", font = ("Arial", 14), command = graph, bg = "#12ba02").grid(row = 4, column = 0)
    tk.Button(grapher, text = "Clear", font = ("Arial", 14), command = clear, bg = "#12ba02").gird(row = 4, column = 1)


#ROOT ATTRIBUTES#
root = tk.Tk()
root.geometry("500x500")
root.title("multi-window_app")
root.configure(bg = "#ff1100")
root.resizable(False, False)

#ROOT ELEMENTS#
lblTitle = tk.Label(root, text = "Multi Window App", font = ("Arial", 22), bg = "#ff1100")
btnGrapher = tk.Button(root, text = "Grapher", font = ("Arial", 14), bg = "#ff4133", command = start_grapher)
btnCalculator = tk.Button(root, text = "Calculator", font = ("Arial", 14), bg = "#ff4133", command = start_calculator)

lblTitle.pack()
btnGrapher.pack()
btnCalculator.pack()

root.mainloop()