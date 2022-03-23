 
def loop(n):
    if n > 0:
        loop(n - 1)
        print(n, end = ' ')
# Driver code
loop(5)

def PrintReverseOrder(N):
     
    for i in range(N, 0, -1):
        print(i, end = " ");
 
# Driver code
if __name__ == '__main__':
     
   
    PrintReverseOrder(4);
  