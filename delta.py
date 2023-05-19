import subprocess
import sys

size = int(sys.argv[1])
interesting = sys.argv[2]

interestingLst = list(range(size))
#n = size
p = []
turn = 0
def DD(p: list, a: list) -> list:
    global turn
    num = 0
    #print(p,a)
    n = len(a)
    if n == 1:
        return a
    #print(n)
    p1 = a[:n//2]
    p2 = a[n//2:]
    union1 = p + p1
    command1 = [i for i in interesting.split()]
    #print(command1)
    for i in union1:
        command1.append(str(i))
    #print(command1)
    union2 = p + p2
    command2 = [i for i in interesting.split()]
    for j in union2:
        command2.append(str(j))  
    # print (command1)
    # print (command2)
    result1 = subprocess.run(command1)
    result2 = subprocess.run(command2)
    #turn +=1
    #print(result.returncode)
    turn += 2
    if result1.returncode == 1:
        #print(command1)
        # print(turn)
        #turn +=1
        return DD(p,p1)
    elif result2.returncode == 1:
        #print(command2)
        #turn+=1
        # print(turn)
        return DD(p,p2) 
    else:
        
        union3 = p + p2
        union4 = p + p1
        return DD(union3, p1) + DD(union4, p2)
        # result = 
        # print(sorted(result))
        
    #return DD(p2)
if __name__ == '__main__':
    
    print(DD(p, interestingLst))
    print(turn)
#print(None+[6,8])