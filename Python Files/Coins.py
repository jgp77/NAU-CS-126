def coins_dollars(amount):
    amount=amount.split('.')
    amount[0]=amount[0][1:]
    coins=int(amount[1])
    dollars=int(amount[0])
    pennies=0
    nickels=0
    dimes=0
    quarters=0
    ones=0
    fives=0
    tens=0
    twenties=0
    hundreds=0
    while coins > 25:
        coins-=25
        quarters += 1
    coins=int(amount[1]) - (25*quarters)
    while coins > 10:
        coins-=10
        dimes+= 1
    coins=int(amount[1]) - (10*dimes)- (25*quarters)
    while coins > 5:
        coins -=5
        nickels += 1
    coins=int(amount[1]) - (5*nickels)- (10*dimes)- (25*quarters)
    while coins >= 1:
        coins -=1
        pennies += 1
    while dollars > 100:
        dollars -= 100
        hundreds+=1
    dollars=int(amount[0]) - (100*hundreds)
    while dollars > 100:
        dollars -= 20
        twenties+=1
    dollars=int(amount[0]) - (100*hundreds) - (20*twenties)
    while dollars > 10:
        dollars -= 10
        tens+=1
    dollars=int(amount[0]) - (100*hundreds) - (20*twenties) - (tens*10)
    while dollars > 5:
        dollars -= 5
        fives+=1
    dollars=int(amount[0]) - (100*hundreds)- (20*twenties) - (tens*10) - (5*fives)
    while dollars > 0:
        dollars -= 1
        ones+=1
    print(str(hundreds) +' Hundreds. ' +str(twenties)+ ' Twenties. '+str(tens)+' Tens. '+str(fives)+' Fives. '+str(ones)+' Ones. ' +
          str(quarters)+' Quarters. '+str(dimes) +' Dimes. ' +str(nickels)+' Nickels. ' +str(pennies) + ' Pennies.')
