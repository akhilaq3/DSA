#returning true when providing correct change to the customer otherwise false
def lemonadeChange(bills):
    five=0
    ten=0
    for i in bills:
        if i==5:
            five+=1
        elif i==10:
            if five>0:
                ten+=1
                five-=1
            else:
                return False
        else:
            if five>0 and ten>0:
                five-=1
                ten-=1
            elif five>=3:
                five-=3
            else:
                return False
    return True
bills=[5,5,5,10,10,5,5,20]
print(lemonadeChange(bills))

    