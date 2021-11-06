'''The Collatz conjecture concerns what happens when we take any positive
integer n and apply the following algorithm:
n = { n∕2, if n is even
3 × n + 1, if n is odd
The conjecture states that when this algorithm is continually applied,
all positive integers will eventually reach 1. For example, if n = 35, the
sequence is
35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1

Write a C program using the fork() system call that generates this
sequence in the child process. The starting number will be provided
from the command line. For example, if 8 is passed as a parameter on
the command line, the child process will output 8, 4, 2, 1. Because the
parent and child processes have their own copies of the data, it will be
necessary for the child to output the sequence. Have the parent invoke
the wait() call to wait for the child process to complete before exiting
the program. Perform necessary error checking to ensure that a positive
integer is passed on the command line'''


import os

n = 0;
k = 0;
	

while (k <= 0):
		print("Enter a number greater than 0 \n"); 
		k = int(input())  #Taking user input

pid = os.fork(); #create child process

if (pid == 0):  #for child process
	        print("Child is working...\n");
		print(k);
		while (k != 1):
		if (k%2 == 0): #when even
		  k = k/2;
		elif (k%2 == 1):   #when odd
		  k = 3*(k) + 1;
		print(k);
		print("Child process is done.\n")
		
else :          #for parent process
	        print("Parent is waiting on child process...\n");
	        os.wait();  #Waits for child process to complete
	        print("Parent process is completed.\n");

