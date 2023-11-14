import tkinter as tk
from tkinter.colorchooser import askcolor

def startDrawing(event):
    global isDrawing, prevX, prevY
    isDrawing = True
    prevX, prevY=event.x, event.y

def draw(event):
    global isDrawing, prevX, prevY
    if isDrawing:
        currentX, currentY = event.x, event.y
        canvas.create_line(prevX, prevY, currentX, currentY, fill=drawingColour, width=lineWidth, capstyle=tk.ROUND, smooth= True)
        prevX, prevY= currentX, currentY

def stopDrawing(event):
    global isDrawing
    isDrawing = False

def changePenColour():
    global drawingColour
    colour = askcolor()[1]
    if colour:
        drawingColour = colour

def changeLineWidth(value):
    global lineWidth
    lineWidth = int(value)

root = tk.Tk()
root.title("Whiteboard App")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

isDrawing = False
drawingColour = "black"
lineWidth = 2

root.geometry("800x600")

controlsFrame = tk.Frame(root)
controlsFrame.pack(side="top", fill="x")

colourButton = tk.Button(controlsFrame, text="Change Colour", command=changePenColour)
clearButton = tk.Button(controlsFrame, text="Clear Canvas", command=lambda: canvas.delete("all"))
colourButton.pack(side="left", padx=5, pady=5)
clearButton.pack(side="left", padx=5, pady=5)

lineWidthLabel = tk.Label(controlsFrame, text="Line Width:")
lineWidthLabel.pack(side="left", padx=5, pady=5)

lineWidthSlider = tk.Scale(controlsFrame, from_=1, to=10, orient="horizontal", command=lambda val: changeLineWidth(val))
lineWidthSlider.set(lineWidth)
lineWidthSlider.pack(side="left", padx=5, pady=5)

canvas.bind("<Button-1>", startDrawing)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stopDrawing)

root.mainloop()


