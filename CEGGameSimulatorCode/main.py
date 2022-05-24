from simulation import *
from results import *
import tkinter as tk
from tkinter.ttk import *

import sys
import argparse

def representsInt(s):
	try: 
		int(s)
		return True
	except ValueError:
		return False

def positiveInt(x):
	if not representsInt(x):
	    print("should be a integer")
	x = int(x)
	if x <= 0:
		print("should be bigger than 0")
	return x

def runSimulation():
    games = positiveInt(var1_entry.get())
    turns = positiveInt(var2_entry.get())
    cards = var3_check
    freeSpaceTravel = var4_check
    autoExploration = var5_check
    
    r = Results()

	# Go through set amount of simulations
    for i in range(0, games):
		# Start a new game, run it and save the results
        g = Game(turns, cards.get(), freeSpaceTravel.get(), autoExploration.get())
        g.run()
        
        r.addHitResults(g.hits)
        if g.wins: 
            r.addWins()

        pb.set(i/games*100)
        p_bar['value'] = pb.get()

	# Same the results to a csv
    r.writeHTML(games, turns, cards.get(), freeSpaceTravel.get(), autoExploration.get())
    

# UI 생성
root = tk.Tk()
root.title("CEG Game Simulator")
root.geometry("320x280")
root.resizable(width=False, height=False)

var1 = Label(root, text="Games")
var2 = Label(root, text="Turns")
var3 = Label(root, text="Cards")
var4 = Label(root, text="Free Space Travel")
var5 = Label(root, text="Auto Exploration")

var3_check=tk.IntVar()
var4_check=tk.IntVar()
var5_check=tk.IntVar()
pb = tk.DoubleVar()

title = Label(root, text="CEG Game Simulator", font=("", 20))
playSimulation = Button(root, text="Play Simulations", command=runSimulation)
p_bar = Progressbar(root, maximum=100, variable=pb)

var1_entry = Entry(root)
var2_entry = Entry(root)
var3_checkbutton = tk.Checkbutton(root, variable=var3_check)
var4_checkbutton = tk.Checkbutton(root, variable=var4_check)
var5_checkbutton = tk.Checkbutton(root, variable=var5_check)

title.grid(row=0, column=0, columnspan=2)
var1.grid(row=1, column=0, sticky="w", padx=10, pady=4)
var2.grid(row=2, column=0, sticky="w", padx=10, pady=4)
var3.grid(row=3, column=0, sticky="w", padx=10, pady=4)
var4.grid(row=4, column=0, sticky="w", padx=10, pady=4)
var5.grid(row=5, column=0, sticky="w", padx=10, pady=4)
var1_entry.grid(row=1, column=1)
var2_entry.grid(row=2, column=1)
var3_checkbutton.grid(row=3, column=1, sticky="w")
var4_checkbutton.grid(row=4, column=1, sticky="w")
var5_checkbutton.grid(row=5, column=1, sticky="w")
playSimulation.grid(row=6, column=0, columnspan=2)
p_bar.grid(row=7, column=0, columnspan=2, pady=4)

var1_entry.insert(0, "10000")
var2_entry.insert(0, "30")
var3_checkbutton.select()
var4_checkbutton.select()
var5_checkbutton.select()

root.mainloop()