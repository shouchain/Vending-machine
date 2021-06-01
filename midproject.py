#所有需要的變數與模組
from prettytable import PrettyTable
import time as T
product = []
price = []
cost = []
stock = []
expiration_date = []
total = 0 
Now = T.localtime ()
Year = Now.tm_year
Mon = Now.tm_mon
Day = Now.tm_mday
TIME = '''%s/%s/%s'''% (Year,Mon,Day)

#讀Inventory檔
F = open('inventory1.txt','a+')
F.seek(0)
allproduct = F.readlines()
F.close()

for i in range(len(allproduct)):
        allproduct[i] = allproduct[i].split(',')
        product.append(allproduct[i][0])
        price.append(allproduct[i][1])
        cost.append(allproduct[i][2])
        stock.append(allproduct[i][3])
        expiration_date.append(allproduct[i][4])
cokesale = product[0]+','+price[0]+','+TIME
teasale = product[1]+','+price[1]+','+TIME
coffeesale = product[2]+','+price[2]+','+TIME

#後台系統介面
def backstage():
    num = input('1.Update the price of an item\n2.Update the value of the stock of an item\n3.Check the Profit\n4.Go back to the initial screen\n')
    if num == '1':
        changeprice()
        backstage()
    elif num == '2' :
        changestock()
        backstage()
    elif num =='3' :
        profit()
        machine()
    elif num =='4' :
        machine()

        
#更改價錢系統        
def changeprice():
    changeproduct = int(input('你要改什麼產品？'))
    changingprice = input('你要改成多少錢？')
    price[changeproduct-1] = changingprice
    CHP = open('inventory1.txt','w')
    #CHP.truncate()
    CHP.seek(0)
    with open('inventory1.txt','a') as W :
        for i in range(len(product)):
            print('%s,%s,%s,%s,%s'%(product[i],price[i],cost[i],stock[i],expiration_date[i]),end='',file=W)
    CHP.close()
    
#更改庫存系統     
def changestock():
    changeproduct1 = int(input('你要改什麼產品？'))
    changingstock = input('你要改成多少庫存？')
    stock[changeproduct1-1] = changingstock
    CHP = open('inventory1.txt','w')
    #CHP.truncate()
    CHP.seek(0)
    with open('inventory1.txt','a') as W :
        for i in range(len(product)):
            print('%s,%s,%s,%s,%s'%(product[i],price[i],cost[i],stock[i],expiration_date[i]),end='',file=W)
    CHP.close()
    
#買東西之後要扣掉庫存    
def buybuy(): #FOR COKE
    stock[0] =str(int(stock[0])-1)
    CHP = open('inventory1.txt','w')
    CHP.seek(0)
    with open('inventory1.txt','a') as W :
        for i in range(len(product)):
            print('%s,%s,%s,%s,%s'%(product[i],price[i],cost[i],stock[i],expiration_date[i]),end='',file=W)
    CHP.close()    
def buybuy1(): #FOR Greentea
    stock[1] =str(int(stock[1])-1)
    CHP = open('inventory1.txt','w')
    CHP.seek(0)
    with open('inventory1.txt','a') as W :
        for i in range(len(product)):
            print('%s,%s,%s,%s,%s'%(product[i],price[i],cost[i],stock[i],expiration_date[i]),end='',file=W)
    CHP.close()   
def buybuy2(): #FOR Coffee
    stock[2] =str(int(stock[2])-1)
    CHP = open('inventory1.txt','w')
    CHP.seek(0)
    with open('inventory1.txt','a') as W :
        for i in range(len(product)):
            print('%s,%s,%s,%s,%s'%(product[i],price[i],cost[i],stock[i],expiration_date[i]),end='',file=W)
    CHP.close()
def buybuy3(): #FOR 7UP
    stock[3] =str(int(stock[3])-1)
    CHP = open('inventory1.txt','w')
    CHP.seek(0)
    with open('inventory1.txt','a') as W :
        for i in range(len(product)):
            print('%s,%s,%s,%s,%s'%(product[i],price[i],cost[i],stock[i],expiration_date[i]),end='',file=W)
    CHP.close()
def buybuy4(): #FOR WATER
    stock[4] =str(int(stock[4])-1)
    CHP = open('inventory1.txt','w')
    CHP.seek(0)
    with open('inventory1.txt','a') as W :
        for i in range(len(product)):
            print('%s,%s,%s,%s,%s'%(product[i],price[i],cost[i],stock[i],expiration_date[i]),end='',file=W)
    CHP.close()    
    
#個別利潤跟總利潤
def profit():
    F = open('FinStat.txt','r')
    F.seek(0)
    profit = F.readlines()
    F.close()
    profitlist = []
    COKE =[]
    GREENTEA = []
    COFFEE = []
    UP7=[]
    WATER=[]
    for i in range(0,len(profit)):
        profit1 = profit[i].split(',')
        profitlist.append(profit1)
    for j in range(0,len(profitlist)):
        if profitlist[j][0]=='COKE':
            COKE.append(int(profitlist[j][1]))
        elif profitlist[j][0]=='GREENTEA':
            GREENTEA.append(int(profitlist[j][1]))
        elif profitlist[j][0]=='COFFEE':
            COFFEE.append(int(profitlist[j][1]))
        elif profitlist[j][0]=='7UP':
            UP7.append(int(profitlist[j][1]))
        elif profitlist[j][0]=='WATER':
            WATER.append(int(profitlist[j][1]))
    sumcoke = sum(COKE)-(len(COKE)*int(cost[0]))
    sumtea = sum(GREENTEA)-(len(GREENTEA)*int(cost[1]))
    sumcoffee = sum(COFFEE)-(len(COFFEE)*int(cost[2]))
    sum7up = sum(UP7)-(len(UP7)*int(cost[3]))
    sumwater = sum(WATER)-(len(WATER)*int(cost[4]))
    print('Profit from COKE:',sumcoke)
    print('Profit from GREENTEA:',sumtea)
    print('Profit from COFFEE:',sumcoffee)
    print('Profit from 7UP:',sum7up)
    print('Profit from WATER:',sumwater)
    print('TOTAL PROFIT:',sumcoke+sumtea+sumcoffee+sum7up+sumwater)
    
#支付系統
def payment():
    global total
    print('Please type the number of the three types of coins sequentially')
    ten = int(input('The number of $10 coins:'))
    five = int(input('The number of $5 coins:'))
    one = int(input('The number of $1 coins:'))
    total = 10*ten + 5*five + one

#成功購買之後把資料放進報表
def fin():
    cokesale = product[0]+','+price[0]+','+TIME
    with open('FinStat.txt','a') as W :
        print(cokesale, file=W)
def fin1():
    cokesale = product[1]+','+price[1]+','+TIME
    with open('FinStat.txt','a') as W :
        print(cokesale, file=W)
def fin2():
    cokesale = product[2]+','+price[2]+','+TIME
    with open('FinStat.txt','a') as W :
        print(cokesale, file=W)
def fin3():
    cokesale = product[3]+','+price[3]+','+TIME
    with open('FinStat.txt','a') as W :
        print(cokesale, file=W)
def fin4():
    cokesale = product[4]+','+price[4]+','+TIME
    with open('FinStat.txt','a') as W :
        print(cokesale, file=W)
    
#介面做Beverage Number表
def BN(): 
    table = PrettyTable(["name", "Price","Stock"])
    table.add_row([product[0], price[0],stock[0]])
    table.add_row([product[1], price[1],stock[1]])
    table.add_row([product[2], price[2],stock[2]])
    table.add_row([product[3], price[3],stock[3]])
    table.add_row([product[4], price[4],stock[4]])
    table.sort_key("name")
    table.reversesort = True

    print(table)
        
#排行系統 
def rank11():
    import operator
    ranking1 = [0,0,0,0,0]
    file = open('FinStat.txt','a+')
    file.seek(0)
    tryout = file.readlines()
    file.close()

    for i in range(0,len(tryout)):
        if tryout[i][0:3] == 'COK':
            ranking1[0]+=1
        elif tryout[i][0:3] == 'GRE':
            ranking1[1]+=1
        elif tryout[i][0:3] == 'COF':
            ranking1[2]+=1
        elif tryout[i][0:3] == '7UP':
            ranking1[3]+=1
        elif tryout[i][0:3] == 'WAT':
            ranking1[4]+=1
        
    ranking1 = tuple(ranking1)
    ranking2 = list(ranking1)

    BR = []
    for i in range(0,len(ranking2)) :
        for j in range(0,len(ranking2)-1-i):
            if int(ranking2[j+1]) > int(ranking2[j]):
                ranking2[j],ranking2[j+1] = ranking2[j+1],ranking2[j]

    for i in range(0,len(ranking2)):
        for j in range(0,len(ranking2)):
            if ranking2[j] == ranking1[i]:
                BR.append(j)

    table = PrettyTable(["NAME", "SALES"])
    table.add_row([product[0], ranking1[0]])
    table.add_row([product[1], ranking1[1]])
    table.add_row([product[2], ranking1[2]])
    table.add_row([product[3], ranking1[3]])
    table.add_row([product[4], ranking1[4]])
    table.sort_key("SALES")
    print(table.get_string(sort_key=operator.itemgetter(0, 1), sortby="SALES",reversesort=True))
    print('\n--------------------------------')  
#呼叫販賣機及介面
def machine(): 
    print('Welcome to my vending machine!')
    print('--------------------------------')
    print('Ranking List:')
    rank11()
    print('\nBeverage Number:')
    BN()
    
    command = input('Type a beverage number for the purchase, Type “AAA” for the administrative interface, Type "QQQ" to leave:')
    if command == 'AAA':
        backstage()
    elif command == '1':
        print('You going to buy COKE $%s'%price[0])
        payment()
        if total>=int(price[0]):
            fin()
            buybuy()
            print('You get a COKE and the change $',total-int(price[0]),',THANKS')
        else:
            print('Money aint enought!')
        machine()
    elif command == '2':
        print('You are going to buy GreenTea $%s'%price[1])
        payment()
        if total>=int(price[1]):
            fin1()
            buybuy1()
            print('You get a Greentea and the change $',total-int(price[1]),',THANKS')
        else:
            print('Money aint enought!')
        machine()
    elif command == '3':
        print('You are going to buy Coffee $%s'%price[2])
        payment()
        if total>=int(price[2]):
            fin2()
            buybuy2()
            print('You get a Coffee and the change $',total-int(price[2]),',THANKS')
        else:
            print('Money aint enought!')
        machine()
    elif command == '4':
        print('You are going to buy 7UP $%s'%price[3])
        payment()
        if total>=int(price[3]):
            fin3()
            buybuy3()
            print('You get a 7UP and the change $',total-int(price[3]),',THANKS')
        else:
            print('Money aint enought!')
        machine()
    elif command == '5':
        print('You are going to buy Water $%s'%price[4])
        payment()
        if total>=int(price[4]):
            fin4()
            buybuy4()
            print('You get a Water and the change $',total-int(price[4]),',THANKS')
        else:
            print('Money aint enought!')
        machine()
    elif command =='QQQ':
        return

machine()