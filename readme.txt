0853132 孫守謙

**若沒安裝過 prettytable 這個套件，可以先運行 pip3 install PrettyTable 安裝

**須將inventory1.txt, FinStat.txt, midproject.py 放置同一個目錄底下(放在同一個資料夾內），才能正常運作

**或者可以自行創造一個inventory1.txt 
  裡面包含COKE,WATER,GREENTEA,COFFEE,7UP 
  並以 產品名稱, 產品價格, 產品成本, 產品庫存, 產品期限 為格式
  EX :
    COKE,30,15,50,2020/1/1
    GREENTEA,35,20,49,2020/1/1
    COFFEE,40,25,50,2020/1/1
    7UP,25,15,50,2020/1/1
    WATER,25,10,50,2020/1/1



1.啟動程式 

--> 執行 machine()

會出現下列介面：

Welcome to my vending machine!
--------------------------------

Ranking List:
+----------+-------+
|   NAME   | SALES |
+----------+-------+
| GREENTEA |   6   |
|  WATER   |   4   |       <----- 銷售排行榜，根據SALES數量由上到下做排序
|   COKE   |   3   |
|  COFFEE  |   3   |                  
|   7UP    |   2   |
+----------+-------+

--------------------------------

Beverage Number:
+----------+-------+-------+
|   name   | Price | Stock |
+----------+-------+-------+
|   COKE   |   25  |   50  |
| GREENTEA |   35  |   50  |    <----- 商品資訊列表，商品編號由上到下是1~5
|  COFFEE  |   40  |   50  |
|   7UP    |   25  |   50  |
|  WATER   |   25  |   50  |
+----------+-------+-------+

Type a beverage number for the purchase, Type “AAA” for the administrative interface, Type "QQQ" to leave:
--> [此處可以輸入下一步指令]

指令步驟：
- 購買商品

直接輸入商品編號 (1~5)

	You going to buy COKE $25 <-- 接著出現你要購買的商品以及需要的價錢，並且開始投錢

	The number of $10 coins:
	The number of $5 coins:
	The number of $1 coins:  <-- 開始投錢，分為10,5,1元硬幣

	You get a COKE and the change $ 0 ,THANKS  <-- 若投的錢足夠買商品，則出現得到一件商品及找的錢
	Money ain‘t enought! 			   <-- 若投的錢不夠買商品，則出現”錢不夠“

	此時在FinStat.txt會新增一列購買紀錄
	COKE,12,2019/11/19 表 購買品項/販賣價格/販賣日期 
	且庫存會減少一個
	買完之後自動回到販賣機介面

- 後台系統 
輸入 AAA 進入後台系統

	1.Update the price of an item
	2.Update the value of the stock of an item
	3.Check the Profit
	4.Go back to the initial screen

輸入1, 2 進入更改資訊
	->你要改什麼產品？[ 輸入欲更改產品編號1~5 ]
	->你要改成多少錢？[ 輸入欲更改產品價格 ] , 你要改成多少庫存？ [ 輸入欲更改產品庫存 ]
	完成更動產品資訊，且會更新inventory1.txt中的資訊

輸入3 進入查詢利潤系統

	Profit from COKE: 
	Profit from GREENTEA: 
	Profit from COFFEE: 
	Profit from 7UP: 
	Profit from WATER: 
	TOTAL PROFIT: 

	出現個產品的個別利潤以及販賣機總利潤 （均為已扣除成本的淨利潤）

輸入4 回到販賣機介面

- 退出系統
數入 QQQ 即可結束系統運作
