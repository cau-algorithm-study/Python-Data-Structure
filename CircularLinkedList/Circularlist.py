# -*- coding:utf-8 -*-
'''
원형연결리스트(Circular Linked List)는 마지막 노드가 첫 노드와 연결된 단순연결리스트이다.

*마지막 노드와 첫 노드를 O(1)시간에 방문할 수 있는 장점을 가진다. 또한 리스트가 empty가 아니면,
어떤 노드도 None을 가지고 있지 않으므로 프로그램에서 None 조건을 검사하지 않아도 된다는 장점을 가진다.

*반대 방향으로 노드들을 방문하기가 쉽지 않으며, 무한 루프가 발생할 수 있음에 유의할 필요가 있다.
'''

class CList:

    # 노드 생성자 항목과 다음 노드 레퍼런스
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link
    
    # 원형연결리스트 생성자, last와 항목 수로 구성.
    def __init__(self):
        self.last = None
        self.size = 0

    def no_items(self): return self.size
    def is_empty(self): return self.size == 0

    def insert(self, item):
        # 새 항목을 저장할 노드를 생성한 후, 연결리스트가 empty인 경우와 그렇지 않은 경우로 나눔.
        n = self.Node(item, None) 

        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
        
        self.size += 1

    def first(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        f = self.last.next
        return f.item

    # 리스트의 첫 노드를 삭제함. 
    # 노드가 1개 인 경우, last를 None으로 만든다.
    # 노드가 2개 이상인 경우, x가 가리키는 노드를 연결리스트에서 분리한다.
    def delete(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        x = self.last.next
        
        if self.size == 1:
            self.last = None
        else:
            self.last.next = x.next
        self.size -= 1

        return x.item

    def print_list(self):
        if self.is_empty():
            print('list is empty')
        else:
            f = self.last.next
            p = f
            while p.next != f:
                print(p.item, ' -> ', end='')
                p = p.next
            print(p.item)

class EmptyError(Exception):
    pass