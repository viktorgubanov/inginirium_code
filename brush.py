import tkinter as tk

def paint(event):
    canvas.create_oval(x-size, y-size, x+size, y+size, outline=color, fill=color)


def sizeble(event):
    global size, oval
    if event.keysym == "Up"and size < 100:
        size += 1
    elif event.keysym == 'Down' and size > 0:
        size -= 1
    Label.config(text="size of brush" + str(size) + 'px')
    canvas.delete(oval)
    oval = canvas.create_oval(x - size, y - size, x + size, y + size, fill=color)


def mouse_pos(event):
    global x, y
    x = event.x
    y = event.y
    canvas.moveto(oval, x-size, y-size)


root = tk.Tk()
root.title("brush")
size = 5
x, y = 0, 0
color = '#0f0'
Label = tk.Label(root, text=f"size of brush {size} px")
Label.pack()
canvas = tk.Canvas(root, bg="#fff", width=640, height=640)
oval = canvas.create_oval(x - size, y - size, x + size, y + size, fill=color)
canvas.pack()
root.bind("<KeyPress>", sizeble)
root.bind('<Motion>', mouse_pos)
root.bind('<Button-1>', paint)
root.mainloop()
