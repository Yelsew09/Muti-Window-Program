#IMPORTS#
import time
import tkinter as tk
from tkinter import messagebox

def start_grapher():
    global root
    grapher = tk.Toplevel(root)
    grapher.geometry("210x140")
    grapher.resizable(False, False)
    grapher.title("grapher")
    grapher.configure(bg = "#085c00")
    tbxOne = tk.Entry(grapher)
    tbxTwo = tk.Entry(grapher)
    tbxThree = tk.Entry(grapher)
    tbxFour = tk.Entry(grapher)

    def graph():
        global graphup, graphwindow
        graphup = True
        num1 = int(tbxOne.get())
        num2 = int(tbxTwo.get())
        num3 = int(tbxThree.get())
        num4 = int(tbxFour.get())
        graphwindow = tk.Toplevel(grapher)
        graphwindow.geometry("585x425")
        graphCanvas = tk.Canvas(graphwindow, width = "550", height = "390", bg = "blue")
        graphwindow.maxsize(700, 425)
        graphwindow.minsize(585, 425)
        
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

        lblGraphOne.grid(row = 0, column = 0)
        lblGraphTwo.grid(row = 1, column = 0)
        lblGraphThree.grid(row = 2, column = 0)
        lblGraphFour.grid(row = 3, column = 0)
        lblGraphFive.grid(row = 4, column = 0)
        lblGraphSix.grid(row = 5, column = 0)
        lblGraphSeven.grid(row = 6, column = 0)
        lblGraphEight.grid(row = 7, column = 0)
        lblGraphNine.grid(row = 8, column = 0)
        lblGraphTen.grid(row = 9, column = 0)
        lblGraphZero.grid(row = 10, column = 0)
        graphCanvas.grid(row = 0, column = 1, rowspan = 11, pady = 15)

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
        
        draw_lines()
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
        global graphup, graphwindow
        if graphup:
            graphwindow.destroy()
        tbxOne.delete(0, tk.END)
        tbxTwo.delete(0, tk.END)
        tbxThree.delete(0, tk.END)
        tbxFour.delete(0, tk.END)

    tk.Button(grapher, text = "Graph", font = ("Arial", 12), command = graph, bg = "#12ba02").grid(row = 4, column = 0)
    tk.Button(grapher, text = "Clear", font = ("Arial", 12), command = clear, bg = "#12ba02").grid(row = 4, column = 1)
    tk.Label(grapher, text = "Number 1:", font = ("Arial", 12), bg = "#085c00").grid(row = 0, column = 0)
    tk.Label(grapher, text = "Number 2:", font = ("Arial", 12), bg = "#085c00").grid(row = 1, column = 0)
    tk.Label(grapher, text = "Number 3:", font = ("Arial", 12), bg = "#085c00").grid(row = 2, column = 0)
    tk.Label(grapher, text = "Number 4:", font = ("Arial", 12), bg = "#085c00").grid(row = 3, column = 0)
    tbxOne.grid(row = 0, column = 1)
    tbxTwo.grid(row = 1, column = 1)
    tbxThree.grid(row = 2, column = 1)
    tbxFour.grid(row = 3, column = 1)
def start_calculator():
    global operation
    calcwindow = tk.Toplevel(root)
    calcwindow.geometry("275x125")
    calcwindow.configure(bg = "blue")
    calcwindow.title("calculator")
    calcwindow.resizable(False, False)


    tk.Label(calcwindow, text = "First number:", font = ("Arial", 14), bg = "blue").grid(row = 0, column = 0)
    tk.Label(calcwindow, text = "Second number:", font = ("Arial", 14), bg = "blue").grid(row = 1, column = 0)
    tk.Label(calcwindow, text = "Operation:", font = ("Arial", 14), bg = "blue").grid(row = 2, column = 0)
    tbxFirstNum = tk.Entry(calcwindow)
    tbxSecondNum = tk.Entry(calcwindow)

    options = [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division"
    ]

    operation = tk.StringVar()
    operation.set("Addition")
    menuOperation = tk.OptionMenu(calcwindow, operation, *options)
    menuOperation.config(bg = "blue")

    def calculate():
        global operation
        num1 = tbxFirstNum.get()
        num2 = tbxSecondNum.get()
        operational = operation.get()
        try:
            if operational == "Addition":
                answer = int(num1) + int(num2)
            elif operational == "Subtraction":
                answer = int(num1) - int(num2)
            elif operational == "Multiplication":
                answer = int(num1) * int(num2)
            elif operational == "Division":
                answer = float(num1)/float(num2)    
            calcwindow.destroy()
            messagebox.showinfo("calc_complete", "Your answer is: " + str(answer))

        except ValueError:
            btnCalc.config(text = "Invalid Input")


    btnCalc = tk.Button(calcwindow, text = "Calculate", font = ("Arial",12), command = calculate, bg = "blue")
    btnCalc.grid(row = 3, column = 0)
    menuOperation.grid(row = 2, column = 0)
    tbxFirstNum.grid(row = 0, column = 1)
    tbxSecondNum.grid(row = 1, column = 1)


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