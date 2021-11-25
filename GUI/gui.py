import PIL.Image
import PIL.ImageTk
from tkinter import *
from DFS import AI
from BFS import Game

window = Tk()
window.geometry("780x600")
window.title("Maze Solver AI")
window.resizable(0,0)

# background image
with PIL.Image.open('logo.png') as logo:
    logo1 = PIL.ImageTk.PhotoImage(logo)
    logo_label = Label(image=logo1)
    logo_label.image=logo
    logo_label.grid(column=1, row=1, pady=5)


get_grid = Label(window, text = "Enter maze", font= ("Arial Bold", 20), fg="blue")
get_grid.grid(column=1, row=2)

inputtxt = Text(window,height = 10,width = 20)
inputtxt.insert(1.0, "##A##\n#  ##\n# ###\n#B###")
inputtxt.grid(column=1, row=3, pady=5)


instructions = Label(window, text = "Enter # for wall, A for start, B for end, and space for path", font= ("Arial Bold", 20))
instructions.grid(column=1, row=4, padx=10, pady=20)

def browse():
    input = filedialog.askopenfile(initialdir="/", filetypes=[("Text file", ".txt")])
    inp = ""
    for i in input:
        inp+=i
    print(inp)
    inputtxt.delete("1.0", END)
    inputtxt.insert(1.0, inp)

def go_dfs():
    g = inputtxt.get("1.0", END)
    game = AI(g)
    game.generateImage()

def go_bfs():
    g = inputtxt.get("1.0", END)
    game = Game(g)
    game.generateImage()

def go_ai():
    g = inputtxt.get("1.0", END)
    inputtxt.delete("1.0", END)
    game = Game(g)
    ai = AI(g)
    dfs_path, dfs_dead = ai.solve()
    game.generateCombinedImage(dfs_path, dfs_dead)

grid1 = Button(window,text="Browse",font="Helvetica",bg="lightgreen",fg="black",height=2,width=20,command=browse)
grid1.grid(column=1, row=5, padx=5, pady=5)

grid2 = Button(window,text="DFS & BFS",font="Raleway",bg="cyan",fg="black",height=2,width=20,command=go_ai)
grid2.grid(column=1, row=9, padx=5, pady=5)


window.mainloop()
