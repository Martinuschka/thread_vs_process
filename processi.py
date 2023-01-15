import tkinter as tk
import multiprocessing
import random
import math


running = False
all_processes = []


def bench(number):
	print("Process ", number, " started.")
	i = 0
	while True:
		i += 1


def pi(number):
	print("Process ", number, " started.")
	innerhalb = 0
	anzahl = 0
	while True:
		anzahl += 1
		x = random.random()
		y = random.random()
		z = math.sqrt(math.pow(x, 2)+math.pow(y, 2))
		if z < 1:
			innerhalb += 1
		pi_calculated = 4*innerhalb/anzahl
		global running
		if not running:
			print("Pi: ", pi_calculated)
			break


def only_numbers(char):
	return char.isdigit()


def start():
	global running
	global all_processes

	if entryProcesses.get() == "":
		processes = 0
	else:
		processes = int(entryProcesses.get())

	if running:
		for process in all_processes:
			process.terminate()
		all_processes.clear()
		running = False
		print("All processes killed.")
		labelStatus.config(text="Idle")
		buttonStart.config(text="Start")
		labelCount.config(text="")
		entryProcesses.config(state="normal")
	else:
		if processes > 0:
			running = True
			for i in range(processes):
				process = multiprocessing.Process(target=pi, args=(i+1,))
				process.daemon = True
				process.start()
				all_processes.append(process)
			labelStatus.config(text="Running")
			buttonStart.config(text="Stop")
			labelCount.config(text=str(processes)+" process(es)")
			entryProcesses.config(state="disabled")


window = tk.Tk()
window.title("Processi")
window.geometry("300x200")
window.resizable(False, False)

validation = window.register(only_numbers)

labelProcesses = tk.Label(text="Number of processes", font=("Arial", 15))
labelProcesses.pack(pady=2)
entryProcesses = tk.Entry(window, font=("Arial", 15), validate="key", validatecommand=(validation, "%S"))
entryProcesses.focus()
entryProcesses.pack(pady=2)
buttonStart = tk.Button(window, text="Start", font=("Arial", 15), command=start)
buttonStart.pack(pady=2)
labelStatus = tk.Label(text="Idle", font=("Arial", 20))
labelStatus.pack(pady=2)
labelCount = tk.Label(text="", font=("Arial", 20))
labelCount.pack(pady=2)


def on_closing():
	global running
	global all_processes
	running = False
	for process in all_processes:
		process.terminate()
	all_processes.clear()
	print("All processes killed.")
	window.destroy()


window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
