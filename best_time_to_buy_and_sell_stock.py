/*
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
*/

def OneTimeTrade(a):
	buy=-float('inf')
	sell=0
	for i in range(0,len(a)):
		if -a[i]>buy:
			buy_date=i
		buy=max(buy,-a[i])
		if buy+a[i]>sell:
			sell_date=i
		sell=max(sell,buy+a[i])
	return [buy_date,sell_date,a[buy_date],a[sell_date]]
  
  if __name__=='__main__':
    a=[700,100,900,800,500]
    l=OneTimeTrade(a)
    print("buy_date : "+ str(l[0])+ "\nSell_date : "+ str(l[1])+ "\nbuying price : "+ str(l[2])+ "\nSelling Price : "+ str(l[3]))
