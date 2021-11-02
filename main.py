from threading import Thread;

arr = [90,81,78,95,79,72,85]
n = len(arr)
average=0
minimum=0
maximum=0

def min():
        global minimum
        minimum=arr[1];
        for i in range(0,n):
                if minimum>arr[i] :
                   minimum=arr[i]
                i=i+1
def avg():
        sum=0;
        global average
        for i in range(0,n):
                sum=sum+arr[i];
                i=i+1
        average=sum/n;
        
  
def max():
   global maximum
   maximum=arr[1];
   for i in range(0,n):
            if maximum<arr[i] :
                maximum=arr[i];
            i=i+1
            
def threaded_function():
    for i in range(0,5):
        print("running")
            
if __name__ == "__main__":
    thread1 = Thread(target = avg)
    thread1.start()
    thread2 = Thread(target = min)
    thread2.start()
    thread3 = Thread(target = max)
    thread3.start()
    
    thread1.join()
    thread2.join()
    thread3.join()
    print(round(average))  
    print(round(minimum)) 
    print(round(maximum)) 
    


                
                
                