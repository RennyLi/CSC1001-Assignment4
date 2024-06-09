new = None  # The new rod the disk will move into
now = None  # The current rod that the disk will move out of 

def now_rod(i,stackA,stackB,stackC):
    global now
    if i in stackA:
        now = "A"
        return stackA
    elif i in stackB:
        now = "B"
        return stackB
    else:
        now = "C"
        return stackC
 
def next_rod(n,i,stackA,stackB,stackC):
    global new
    if n % 2==0:  # If n is even, then all the disks can move to the C tower
        if i in stackA:
            if i % 2 != 0:
                new_rod = stackB
                new = "B"
            else:
                new_rod = stackC
                new = "C"
        if i in stackB:
            if i % 2 != 0:
                new_rod = stackC
                new = "C"
            else:
                new_rod = stackA
                new = "A"
        if i in stackC:
            if i % 2 != 0:
                new_rod = stackA
                new = "A"
            else:
                new_rod = stackB
                new = "B"
    else:  
    # If n is odd, then all the disks can move to the B tower
    # By changing tower name, we can move all the disks to tower C
        if i in stackA:
            if i % 2 == 0:
                new_rod = stackB
                new = "B"
            else:
                new_rod = stackC
                new = "C"
        if i in stackB:
            if i % 2 == 0:
                new_rod = stackC
                new = "C"
            else:
                new_rod = stackA
                new = "A"
        if i in stackC:
            if i % 2 == 0:
                new_rod = stackA
                new = "A"
            else:
                new_rod = stackB
                new = "B"
    return new_rod

def move(now_rod,next_rod):  # Define the move function to move disks between stacks(rods)
    global new
    global now
    n = now_rod.pop()
    next_rod.append(n)
    print(now,"-->",new)
 
def HanoiTower(n):
    stackA = []
    stackB = []
    stackC = []
    end = []
    for i in range(0,n):
        stackA.append(n-i)
        end.append(n-i)
 
    while(stackC != end):  # All the disks haven't been moved to rod C
        for i in range(1,n+1):
            if (now_rod(i,stackA,stackB,stackC).index(i) == len(now_rod(i,stackA,stackB,stackC))-1 and (next_rod(n,i,stackA,stackB,stackC) == [] or i < next_rod(n,i,stackA,stackB,stackC)[-1])):
                move(now_rod(i,stackA,stackB,stackC),next_rod(n,i,stackA,stackB,stackC))
            else:
                continue

def main():
    number_of_disks = int(input("Please enter the number of disks you want to move:"))
    HanoiTower(number_of_disks)
main()