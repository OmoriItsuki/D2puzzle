import random
from enum import Enum

class Type(Enum):
    sen=1
    ark=2
    a=3
    kom=4

status=[2,1,2,2,1,4,1,3,1]
#status=[1,1,1,1,1,1,1,1,1]

ans=list()


def monte(s):
    global status
    t = 0
    for k in range(100000):
        #print("--------------------------------------------------")
        #printStatus()
        t+=1
        for i in range(s):
            if(checkAns()):
                print(str(s)+"文字以内"+str(t)+"回目で終了　答え→"+str(list(map(lambda x : x+1, ans))))
                ans.clear()
                status = [2, 1, 2, 2, 1, 4, 1, 3, 1]
                monte(s-1)
                return ans
            #print(str(t)+"-"+str(i)+"回目")
            push = random.randrange(9)
            change(push)
            norm()
            ans.append(push)
            #print(push+1)
            #printStatus()
        status=[2,1,2,2,1,4,1,3,1]
        ans.clear()
    print(ans)
    return ans

def change(rand):
    if(rand%3 == 0):
        status[rand]+=1
        status[rand+1]+=1
        status[rand+2]+=1
        status[(rand+3)%9]+=1
        status[(rand+6)%9]+=1
    elif(rand%3 == 1):
        status[rand]+=1
        status[rand+1]+=1
        status[rand-1]+=1
        status[(rand+3)%9]+=1
        status[(rand+6)%9]+=1
    elif(rand%3 == 2):
        status[rand]+=1
        status[rand-1]+=1
        status[rand-2]+=1
        status[(rand+3)%9]+=1
        status[(rand+6)%9]+=1

def norm():
    for i in range(9):
        status[i]%=4
        if status[i]==0:
            status[i]=4

def checkAns():
    for i in range(9):
        if(not status[i] == 1):
            return False
    return True

def printStatus():
    for i in range(3):
        for j in range(3):
            print(status[j + 3 * i], end="")
        print()
    print()

def main():
    monte(20)

main()