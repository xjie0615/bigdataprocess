def total():
    sum = 0
    for i in range (1,10):
        sum += i
        return sum
    
    def main():
            t=total()
            print('summation of 1 to 100',t)
 
main()
    
def printstar(n):
     for i in range(1,100):
       print('*',end='')
     print()

def main():
    printstar(20)
    printstar(30)
    printstar(50)
 
main()

def total(a,b):
    sum= 0
    for i in range(a,b+1):
        sum +=1
        