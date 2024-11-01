import heapq

pq=[]

heapq.heappush(pq,(2,'a')) #(priority,element)
#2,a

heapq.heappush(pq,(1,'b'))
#2,a 1,b
#1,b 2,a

heapq.heappush(pq,(4,'c'))
#1,b 2,a 4,c
print(pq)

heapq.heappush(pq,(0,'d'))
#0,d 1,b 4,c 2,a

heapq.heappush(pq,(6,'e'))
print(pq)

heapq.heappush(pq,(5,'f'))
print(pq)

heapq.heappush(pq,(3,'g'))
print(pq)

