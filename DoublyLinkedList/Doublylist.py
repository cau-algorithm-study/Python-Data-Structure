# -*- coding:utf-8 -*-
'''
이중연결리스트(Doubly Linked List) 는 각 노드가 두 개의 레퍼런스를 가지고 각각 이전 노드와 다음 노드를 가리키는 연결리스트이다.

*단순연결리스트는 다음 노드의 레퍼런스만으로 노드들이 연결되어, 삽입이나 삭제할 때 반드시 이전 노드를 가리키는 레퍼런스를 추가로 알아야 하고,
역방향으로 노드들을 탐색할 수 없다. 이중연결리스트는 단순연결리스트의 이러한 단점을 보완했으나, 각 노드마다 1개의 레퍼런스를 추가로 
저장해야 한다는 단점을 가진다.

1. 삽입/삭제 연산은 단순연결리스트의 삭제/삽입보다 복잡하나 각각 O(1) 개의 reference 만을 갱신하므로 O(1) 시간에 수행됨.
2. 탐색 연산은 단순연결리스트의 탐색과 같이 Head 또는 Tail 로 부터 노드들을 순차적으로 탐색해야 하므로 O(N) 시간이 소요됨.

'''

class DList:

    # 노드 생성자 항목과 앞뒤 레퍼런스
    class Node:

        def __init__(self, item, prev, link):
            self.item = item
            self.prev = prev
            self.next = link 

    # 이중연결리스트 생성자 head와 tail, 항목 수로 구성.
    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    def getSize(self): return self.size
    def is_empty(self): return self.size == 0

    def insert_before(self, p, item):
        t = p.prev
        n = self.Node(item, t, p) # 새 노드 생성하여 n 이 참조
        p.prev = n # 새노드와 앞뒤 노드 연결
        t.next = n # 새노드와 앞뒤 노드 연결
        self.size += 1

    def insert_after(self, p, item):
        t = p.next
        n = self.Node(item, p, t) # 새 노드 생성하여 n 이 참조
        t.prev = n # 새노드와 앞뒤 노드 연결
        p.next = n # 새노드와 앞뒤 노드 연결
        self.size += 1

    def delete(self, x):
        f = x.prev
        r = x.next
        f.next = r # x를 건너 뛰고, x의 앞뒤 노드를 직접 연결
        r.prev = f
        self.size -= 1
        return x.item

    def print_list(self):
        if self.is_empty():
            print("list is empty")
        else:
            p = self.head.next
            while p != self.tail:
                if p.next != self.tail:
                    print(p.item, ' <=> ', end='')
                else:
                    print(p.item)
                
                p = p.next # 노드를 차례로 방문하기 위해

class EmptyError(Exception):
    pass
    
           