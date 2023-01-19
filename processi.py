import tkinter as tk
import multiprocessing
import random
import math


class ProcessBenchmark:
	def __init__(self, window):
		self.window = window
		self.running = False  # flag only for state of button, since processes don't share memory
		self.all_processes = []  # list for terminating processes

	# backup function for simulating stress
	@staticmethod
	def bench(number):
		print("Process ", number, " started.")
		i = 0
		while True:
			i += 1

	# approximating pi
	@staticmethod
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
			if anzahl % 10000000 == 0:
				print("Process ", number, ", Pi: ", pi_calculated)

	def start(self):
		if self.window.entryProcesses.get() == "":
			processes = 0
		else:
			processes = int(self.window.entryProcesses.get())

		if self.running:
			for process in self.all_processes:
				process.terminate()
			self.all_processes.clear()
			self.running = False
			print("All processes killed.")
			self.window.labelStatus.config(text="Idle")
			self.window.buttonStart.config(text="Start")
			self.window.labelCount.config(text="")
			self.window.entryProcesses.config(state="normal")
		else:
			if processes > 0:
				self.running = True
				for i in range(processes):
					process = multiprocessing.Process(target=self.pi, args=(i+1,))
					process.start()
					self.all_processes.append(process)
				self.window.labelStatus.config(text="Running")
				self.window.buttonStart.config(text="Stop")
				self.window.labelCount.config(text=str(processes)+" process(es)")
				self.window.entryProcesses.config(state="disabled")


class Window(tk.Frame):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
		self.validation = self.register(self.only_numbers)

		self.labelProcesses = tk.Label(self, text="Number of processes", font=("Arial", 15))
		self.labelProcesses.pack(pady=2)
		self.entryProcesses = tk.Entry(self, font=("Arial", 15), validate="key", validatecommand=(self.validation, "%S"))
		self.entryProcesses.focus()
		self.entryProcesses.pack(pady=2)
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
	root.title("Processi")
	root.geometry("300x200")
	root.resizable(False, False)

	window = Window(root)
	benchmark = ProcessBenchmark(window)
	window.buttonStart.configure(command=benchmark.start)


	def on_closing():
		for process in benchmark.all_processes:
			process.terminate()
		benchmark.all_processes.clear()
		print("All processes killed.")
		root.destroy()


	root.protocol("WM_DELETE_WINDOW", on_closing)
	root.mainloop()
