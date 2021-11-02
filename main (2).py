import os

n=0;
k=0;
	

while (k <= 0):
		print("Please enter a number greater than 0 to run the Collatz Conjecture.\n"); 
		k = int(input())

pid = os.fork();

if (pid == 0):
		
			print("Child is working...\n");
			print(k);
			while (k!=1):
				if (k%2 == 0):
				    k = k/2;
				elif (k%2 == 1):
					k = 3 * (k) + 1;
				print(k);
		
			print("Child process is done.\n")
else :
		
			    print("Parents is waiting on child process...\n");
			    os.wait();
			    print("Parent process is done.\n");

