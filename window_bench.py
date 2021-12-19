import tkinter as tk
import multiprocessing

running=False
all_processes=[]

def bench(number):
	print("Thread ",number," started.")	
	i=0
	while True:
		i+=1

def only_numbers(char):
	return char.isdigit()

def start():
	global running

	if entryThreads.get()=="":
		threads=0
	else:
		threads=int(entryThreads.get())

	if running:
		for process in all_processes:
			process.terminate()
		all_processes.clear()
		running=False
		print("All threads killed.")
		labelStatus.config(text="Idle")
		buttonStart.config(text="Start")
		labelCount.config(text="")
		entryThreads.config(state="normal")
	else:
		if threads>0:
			running=True
			for i in range(threads):
				process=multiprocessing.Process(target=bench, args=(i+1,))
				process.start()
				all_processes.append(process)
			labelStatus.config(text="Running")
			buttonStart.config(text="Stop")
			labelCount.config(text=str(threads)+" Thread(s)")
			entryThreads.config(state="disabled")

window=tk.Tk()
window.title("Benchmark")
window.geometry("300x200")
window.resizable(False,False)

validation=window.register(only_numbers)

labelThreads=tk.Label(text="Number of threads",font=("Arial",15))
labelThreads.pack(pady=2)
entryThreads=tk.Entry(window,font=("Arial",15), validate="key", validatecommand=(validation,"%S"))
entryThreads.focus()
entryThreads.pack(pady=2)
buttonStart=tk.Button(window, text="Start",font=("Arial",15),command=start)
buttonStart.pack(pady=2)
labelStatus=tk.Label(text="Idle",font=("Arial",20))
labelStatus.pack(pady=2)
labelCount=tk.Label(text="",font=("Arial",20))
labelCount.pack(pady=2)

window.mainloop()