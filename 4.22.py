''' Write a multithreaded program that calculates various statistical values
for a list of numbers. This program will be passed a series of numbers
on the command line and will then create three separate worker threads.
One thread will determine the average of the numbers, the second will
determine the maximum value, and the third will determine the minimum
value. For example, suppose your program is passed the integers
90 81 78 95 79 72 85
The program will report
The average value is 82
The minimum value is 72
The maximum value is 95
The variables representing the average, minimum, and maximum values
will be stored globally. The worker threads will set these values, and
the parent thread will output the values once the workers have exited.

Credits - https://itprospt.com/qa/247165/write-in-c-program-write-a-multi-threaded-program'''


from threading import Thread;

arr = []

print("Type the length of the Array")
n = int(input())
i = 0
print("Type the values of the Array")

while(i < n):  #loop to take inputs
        next = int(input())
        arr.append(next)
        i = i + 1
    
n = len(arr)

avg = 0
min = 0
max = 0

def minimum():  #function to calculate minimum
        global min
        min = arr[1];
        for i in range(0,n):
                if min > arr[i] :
                   min = arr[i]
                i = i+1
                
                
def average():  #function to calculate average
        sum = 0
        global avg
        for i in range(0,n):
                sum = sum + arr[i]
                i = i+1
        avg = sum/n
        
  
def maximum():  #function to calculate maximum
   global max
   max = int(arr[1])
   for i in range(0,n):
            if max < arr[i] :
                max = arr[i]
            i = i+1
        
            
if __name__ == "__main__":  #main runs as parent thread
    #defining thread with target as corresponding functions
    thread1 = Thread(target = average)
    thread1.start()  #start thread 1
    thread2 = Thread(target = minimum)
    thread2.start()  #start thread 2
    thread3 = Thread(target = maximum)
    thread3.start()  #start thread 3
    
    thread1.join()   #join thread 1
    thread2.join()   #join thread 2
    thread3.join()   #join thread 3
    
    #print minimum, maximum and average
    print("The average value is ",int(avg))  
    print("The minimum value is ",round(min)) 
    print("The maximum value is ",round(max)) 
    
