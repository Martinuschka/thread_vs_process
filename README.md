# thread_vs_process

small programs for benchmarking

executes calculations on a given number of (logical) cores

uses either processes or threads in python for comparison

processes do not share memory;
main script can not access information in process;
processes use full CPU power

threads share memory;
main script can access information in thread;
threads do not use full CPU power

(two separate scripts, using tkinter for window GUI) 
