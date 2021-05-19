num=int(input())
print(num,end=" " )
while num!=1:
    print(num,end=" ")
    if num%2:
        num=3*num+1
    else :
        num=num//2
     
print(num)         
