# -*- coding:utf-8 -*-
'''
Insert 연산을 위한 upheap은 삽입된 노드로부터 최대 루트까지 올라가며 부모와 자식 노드를 교환한다.
또한, delete_min 연산에서는 힙의 마지막 노드를 루트로 이동한 후, downheap을 최하위층의 노드까지 교환해야 하는 경우가 있다.

따라서, 힙에서 각 연산의 수행시간은 힙의 높이에 비례한다. 
힙은 완전이진트리이므로 힙에 N개의 노드가 있으면, 높이는 [log(N+1)]이다. 따라서 힙 연산의 수행시간은 O(logN)이다.

힙 만들기는 h = 1인 경우부터 시작하여 최상위층의 루트까지 각 노드에 대해 downheap을 수행하므로,
힙 만들기의 수행시간 T(N)은 다음의 계산을 통해 O(N)임을 알 수 있다.
    T(N) = 1*(N/2^2) + 2*(N/2^3) + 3*(N/2^4) + ... + (logN-1)*(N/2^logN)
'''

'''
우선순위큐를 위한 heapq를 라이브러리로 제공한다.
@heapq.heappush(heap, item)     # insert()
@heapq.heappop(heap)            # delete_min()
@heapq.heappushpop(heap, item)  # item을 삽입한 후, delete_min() 수행
@heapq.heapify(x)               # craete_heap()
@heapq.heapreplace(heap, item)  # delete_min()을 먼저 수행 후, item 삽입
'''


class BHeap:
    def __init__(self, a):
        self.a = a
        self.N = len(a) - 1

    # 초기 힙 만들기 (heapq.heapify()와 동일)
    # 초기에 임의의 순서로 키가 저장되어 있는 리스트 a[1] ~ a[N]의 항목들을 최소힙으로 만든다.
    def create_heap(self):
        for i in range(self.N//2, 0, -1):
            self.downheap(i)

    # 삽입 연산 (heapq.push()와 동일)
    def insert(self, key_value):
        self.N += 1

        # 새 항목을 힙 마지막에 추가
        self.a.append(key_value)

        # 힙속성 회복시키기 위해
        self.upheap(self.N)

    # 최솟값 삭제 (heapq.pop()과 동일)
    def delete_min(self):
        if self.N == 0:
            print('힙이 비어 있음')
            return None

        minimum = self.a[1]

        # root값과 맨 마지막값 교환
        self.a[1], self.a[-1] = self.a[-1], self.a[1]
        del self.a[-1]

        self.N -= 1

        # 힙 속성 회복
        self.downheap(1)
        return minimum

    # 힙 내려가며 힙속성 회복 (Bottom-up Heap Construction)
    # 상향식(Bottom-Up) 방식으로 각 노드에 대해 힙속성을 만족하도록 부모와 자식노드를 서로 바꾼다.
    # 힙을 만들기 위해선 a[N//2] 부터 a[1]까지 차례로 downheap을 각각 수행하여 힙속성을 충족시킨다.
    # a[N//2+1] 부터 a[N]에 대하여 downheap을 수행하지 않는 이유는 이 노드들이 이파리(Leaf)이므로
    # 각각의 노드가 힙 크기가 1인 독립적인 최소힙이기 때문이다.
    def downheap(self, i):
        while 2*i <= self.N:
            k = 2 * i

            if k < self.N and self.a[k][0] > self.a[k+1][0]:
                k += 1
            if self.a[i][0] < self.a[k][0]:
                break

            self.a[i], self.a[k] = self.a[k], self.a[i]
            i = k

    # 힙 올라가며 힙속성 회복
    def upheap(self, j):
        while j > 1 and self.a[j//2][0] > self.a[j][0]:
            self.a[j], self.a[j//2] = self.a[j//2], self.a[j]
            j = j//2

    def print_heap(self):
        for i in range(1, self.N+1):
            print('[%2d' % self.a[i][0], self.a[i][1], ']', end='')

        print("\n heap size = ", self.N)
