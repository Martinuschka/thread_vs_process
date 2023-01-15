# thread_vs_process

small programs for benchmarking

executes calculations on a given number of (logical) cores

uses either processes or threads in python for comparison

processes do not share memory, so can not be accessed when terminated
processes use full CPU power

threads share memory and can access calculation when killed
threads do not use full CPU power

(two separate scripts, using tkinter for window GUI) 
