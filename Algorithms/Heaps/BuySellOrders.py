import heapq
"""
Given a list of orders (price, quantity, type), the algorithm matches buy orders to sell order
and vice-versa to get the best price. A match is defined as:
    - buy order: if there exists a sell order price that is <= than buy order price
    - sell order: if there exists a buy order price that is >= than sell order price
The algorithm returns the number of unmatched orders at the end.

Time: O(nlogn)
Space: O(n)
"""
def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
    buy_heap, sell_heap = [], [] #max heap for buy order, min heap for sell orders
    
    for p, a, t in orders:
        #sell order
        if t:
            #while the quantity of the sell order is not satisfied and there is a match
            while a and buy_heap and -buy_heap[0][0] >= p:
                #quantity of the best buy order avialable
                buy_amount = buy_heap[0][1]
                #if there is enough buy_amount, we can execute this sell order and exit the loop
                if buy_amount > a:
                    #assign new amount after sell order
                    buy_heap[0][1] -= a
                    a = 0
                #there is not enough of the best buy order to execute the sell order
                else:
                    #remove the current buy order (alredy used) and work with the next best buy order
                    heapq.heappop(buy_heap)
                    #update the remaining sell order
                    a -= buy_amount
            #if the sell order is not fulfilled, add it to the sell backlog (sell heap)
            if a > 0:
                heapq.heappush(sell_heap, [p, a])
        #buy order    
        else:
            #same idea for buy order
            while a and sell_heap and sell_heap[0][0] <= p:
                sell_amount = sell_heap[0][1]
                if(sell_amount > a):
                    sell_heap[0][1] -= a
                    a = 0
                else:
                    heapq.heappop(sell_heap)
                    a-=sell_amount
            if(a > 0):
                heapq.heappush(buy_heap, [-p, a])
    
    #return the remaining orders in the backlog
    return sum(a for _, a in buy_heap+sell_heap) % (10**9 + 7)