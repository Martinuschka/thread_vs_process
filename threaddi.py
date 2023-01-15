import tkinter as tk
from threading import Thread
import random
import math


# flag for killing threads and state of button
running = False


# backup function for simulating stress
def bench(number):
	print("Process ", number, " started.")
	i = 0
	while True:
		global running
		if not running:
			break
		i += 1


# approximating pi
def pi(number):
	print("Thread ", number, " started.")
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
			# print("Thread ", number, ", Pi: ", pi_calculated)
			# printing this was too much at the same time for simultaneous threads
			print(pi_calculated)
			break


def only_numbers(char):
	return char.isdigit()


def start():
	global running

	if entryThreads.get() == "":
		threads = 0
	else:
		threads = int(entryThreads.get())

	if running:
		running = False
		print("All threads killed.")
		labelStatus.config(text="Idle")
		buttonStart.config(text="Start")
		labelCount.config(text="")
		entryThreads.config(state="normal")
	else:
		if threads > 0:
			running = True
			for i in range(threads):
				thread = Thread(target=pi, args=(i+1,))
				thread.daemon = True
				thread.start()
			labelStatus.config(text="Running")
			buttonStart.config(text="Stop")
			labelCount.config(text=str(threads)+" Thread(s)")
			entryThreads.config(state="disabled")


window = tk.Tk()
window.title("Threaddi")
window.geometry("300x200")
window.resizable(False, False)

validation = window.register(only_numbers)

labelThreads = tk.Label(text="Number of threads", font=("Arial", 15))
labelThreads.pack(pady=2)
entryThreads = tk.Entry(window, font=("Arial", 15), validate="key", validatecommand=(validation, "%S"))
entryThreads.focus()
entryThreads.pack(pady=2)
buttonStart = tk.Button(window, text="Start", font=("Arial", 15), command=start)
buttonStart.pack(pady=2)
labelStatus = tk.Label(text="Idle", font=("Arial", 20))
labelStatus.pack(pady=2)
labelCount = tk.Label(text="", font=("Arial", 20))
labelCount.pack(pady=2)


def on_closing():
	# threads killed automatically since daemon-threads
	print("All threads killed.")
	window.destroy()


window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
