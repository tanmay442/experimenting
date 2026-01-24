#a=lenght of input list
#b = list istelf
#idk where to use a cant finad any use but was in the test case input so pased down as arg

import sys

def exec():
    num = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))


    def endcheck(a,b):
        if b[0] != -1 and b[-1] != -1:
            c = abs(b[0]-b[-1]) 
            return c
        elif b[0] == -1 and b[-1] != -1:
            b[0] =  b[-1]
            c = abs(b[0]-b[-1])
            return c
        elif b[-1] == -1 and b[0] != -1:
            b[-1] =  b[0]
            c = abs(b[0]-b[-1])
            return c
        else: 
            b[-1] =  0
            b[0] =  0
            return 0

    def zeroallwrongone(b):
        for i in range(len(b)):
            if b[i] == -1:
                b[i] = 0
        return b

    def finalsol(a,b):
        diff = endcheck(a,b)
        finalarray = zeroallwrongone(b)
        print(diff)
        print(*finalarray)
        #return diff, finalarray


    finalsol(num,nums)

def main():
    total_tes_cases = int(sys.stdin.readline())
    for i in range(total_tes_cases):
        exec()
    
main()
