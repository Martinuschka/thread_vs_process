import tkinter as tk
from threading import Thread
import random
import math


class ThreadBenchmark:
	def __init__(self, window):
		self.window = window
		self.running = False  # flag for killing threads and state of button

	# backup function for simulating stress
	def bench(self, number):
		print("Process ", number, " started.")
		i = 0
		while True:
			if not self.running:
				break
			i += 1

	# approximating pi
	def pi(self, number):
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
			if not self.running:
				# print("Thread ", number, ", Pi: ", pi_calculated)
				# printing this was too much at the same time for simultaneous threads
				print(pi_calculated)
				break

	def start(self):
		if self.window.entryThreads.get() == "":
			threads = 0
		else:
			threads = int(self.window.entryThreads.get())

		if self.running:
			self.running = False
			print("All threads killed.")
			self.window.labelStatus.config(text="Idle")
			self.window.buttonStart.config(text="Start")
			self.window.labelCount.config(text="")
			self.window.entryThreads.config(state="normal")
		else:
			if threads > 0:
				self.running = True
				for i in range(threads):
					thread = Thread(target=self.pi, args=(i+1,))
					thread.daemon = True
					thread.start()
				self.window.labelStatus.config(text="Running")
				self.window.buttonStart.config(text="Stop")
				self.window.labelCount.config(text=str(threads)+" Thread(s)")
				self.window.entryThreads.config(state="disabled")


class Window(tk.Frame):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
		self.validation = self.register(self.only_numbers)

		self.labelThreads = tk.Label(self, text="Number of threads", font=("Arial", 15))
		self.labelThreads.pack(pady=2)
		self.entryThreads = tk.Entry(self, font=("Arial", 15), validate="key", validatecommand=(self.validation, "%S"))
		self.entryThreads.focus()
		self.entryThreads.pack(pady=2)
		self.buttonStart = tk.Button(self, text="Start", font=("Arial", 15))
		self.buttonStart.pack(pady=2)
		self.labelStatus = tk.Label(self, text="Idle", font=("Arial", 20))
		self.labelStatus.pack(pady=2)
		self.labelCount = tk.Label(self, text="", font=("Arial", 20))
		self.labelCount.pack(pady=2)
		self.pack()

	@staticmethod
	def only_numbers(char):
		return char.isdigit() or char == "\b"


if __name__ == "__main__":
	root = tk.Tk()
	root.title("Threaddi")
	root.geometry("300x200")
	root.resizable(False, False)

	window = Window(root)
	benchmark = ThreadBenchmark(window)
	window.buttonStart.configure(command=benchmark.start)


	def on_closing():
		# threads killed automatically since daemon-threads
		print("All threads killed.")
		root.destroy()


	root.protocol("WM_DELETE_WINDOW", on_closing)
	root.mainloop()
