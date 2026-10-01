# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temporary_list=ListNode(0) #nenu oka temparary node tisukunna ra
        temp=temporary_list #tarvatha nenu temp ani oka variable ni kuda point chestunna andhuko tharvatha cheptha wait
        remainder=0 # endhuku ante suppose nenu 4+6 add cheddam anukunna 10 vasthadi , manam normal ga yala add chestham 1 emo paiki veltundi kada
        while l1 is not None or l2 is not None or remainder >0: # pra node ni and remain ni kuda cheack chestunna ra
            if l1 is not None: # ikkada nenu l1 linked empty aa ani chustunna , oka vela empty kaka pothey nenu x loki aa current node value ni add chestunna
                x=l1.val
                l1=l1.next
            else:
                x=0
            if l2 is not None: # edi kuda same ok vela unte add chestunna lekapothey y=0 antyyyyyyyyyyyyyyyyyyy
                y=l2.val
                l2=l2.next
            else:
                y=0

            total=x+y+remainder #edhi sum calculation ni ku yala ga vachhu ga
            remainder=total//10 # edhi remainber
            sum_digit=total%10 # edhi digit kosam

            temp.next=ListNode(sum_digit) # ante manam starting lo oka temporary_list anedi head anuko or starting point of node edi temp.next ante enko dahi oka next ki point chestundi ra ante suppose nuvuu oka lst create chesav ra nuvuu user deggara nunchi input tesukoni loop ni run chestha elments ni list loki add chesthav list index based chesukoni , kani ikkada nuvuu loop rancheyya daniki emm undavuu kada andhukey next petta
            temp=temp.next # edhi emo 

        return temporary_list.next # ikkada manam first 0 ni intaial ga tesukunnam ra indhulo yala ga unthundi ante 0 8 0 7 thundi kada and dhukey nenu aa tharvatha node nundi return chestunna
        
            

        