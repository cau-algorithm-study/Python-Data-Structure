# -*- coding:utf-8 -*-
'''
단순연결리스트 (Singly Linked List)는 동적 메모리 할당을 이용해 노드들을 한 방향으로 연결하여 리스트를 구현하는 자료구조이다.
1. 삽입/삭제 시 항목들의 이동이 필요없다 (O(1))
2. 항목 탐색 시 항상 첫 노드부터 원하는 노드를 찾을 때 까지 차례로 방문한다 (순차탐색(Sequential Search))
'''


class SList:
    
    # 노드 생성자
    class Node:
        def __init__(self, item, link):
            self.item = item 
            self.next = link # 다음 레퍼런스

    # 단순연결리스트 생성자
    def __init__(self):
        self.head = None
        self.size = 0 # 항목 수 

    def getSize(self): return self.size
    def is_empty(self): return self.size == 0

    # 단순연결리스트의 맨 앞에 새 노드를 삽입함.
    def insert_front(self, item):
        # 리스트가 empty 일 때
        if self.is_empty():
            self.head = self.Node(item, None)
        else:
            self.head = self.Node(item, self.head)
        self.size += 1

    # p가 가리키는 노드의 다음 노드를 새 노드가 가리킴.
    def insert_after(self, item, p):
        p.next = SList.Node(item, p.next)
        self.size += 1
    
    # 단순연결리스트의 첫 노드를 삭제하는 경우
    def delte_front(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        else:
            self.head = self.head.next
            self.size -= 1

    # p가 가리키는 노드의 다음 노드를 삭제하는 경우
    def delete_after(self, p):
        if self.is_empty():
            raise EmptyError('Underflow')
        t = p.next
        p.next = t.next
        self.size -= 1

    def search(self, target):
        p = self.head
        for k in range(self.size):
            if target == p.item : return k
            p = p.next
        return None

    def print_list(self):
        p = self.head
        while p :
            if p.next != None:
                print(p.item, ' -> ', end='')
            else:
                print(p.item)
            p = p.next

class EmptyError(Exception):
    pass
