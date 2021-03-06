import minheap as mheap


def generateData(x):
    data = []
    for i in x:
        head = None
        for j in reversed(len(i)):
            item = ListNode(x[i][j])
            item.next = head
            head = item
        data.append(head)
    return data


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for i in list:
            heap.append((i.val, i))
        mheap.heapify(heap)
        res = None
        head = ListNode(0)
        head.next = res
        while heap:
            val, temp = mheap.pop(heap)
            res = temp
            res = res.next
            temp = temp.next
            if temp is not None:
                mheap.push(heap,(temp.val,temp)
        return head.next
    
    def mergeLists(self,lists):
        if len(lists) == 0:
            return lists
        heap = []
        head = None
        tail = None
        for i in lists:
            if i != None:
                heap.append((i.val,i))
        minheap.heapify(heap)
        v,t = minheap.pop(heap)
        head = t
        tail = head
        t = t.next
        minheap.push(heap,(t.val,t))
        while heap:
            v1,t1 = minheap.pop(heap)
            tail.next = t1
            tail = tail.next
            t1 = t1.next
            if t1:
                minheap.push(heap,(t1.val,t1))
        return head     




so = Solution()
data = generateData([[7],[49],[73],[58],[30],[72],[44],[78],[23],[9],[40]
,[65],[92],[42],[87],[3],[27],[29],[40],[12],[3]])
res = so.mergeKLists(data)
while res != None:
    print(res.val)
    print("\n")
    res = res.next
