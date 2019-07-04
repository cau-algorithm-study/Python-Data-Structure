# -*- coding:utf-8 -*-
'''
남태평양에 있는 어느 나라에 11개의 섬이 다음과 같이 다리로 연결되어 있다. 
이 나라의 관광청에서는 관광객들이 11개의 섬들을 모두 방문할 수 있는, 순서가 다른 3개의 관광코스를 만들었다.
각 코스의 관광은 섬 H에서 시작한다. 관광청에서는 각 관광 코스의 방문 순서를 다음과 같은 규칙에 따라 만들었다.

                        H
                    /       \   
                    F       S
                  /   \    /  \
                 U     E   Z   K
                /     /         \
                N     A          Y
                       \
                        T
'''
# A 코스 : 섬에 도착하면 항상 도착한 섬을 먼저 관광하고, 그 다음엔 왼쪽 섬으로 관광을 진행한다.
#           왼쪽 방향의 모든 섬들을 방문한 후에는 오른쪽 섬으로 관광을 진행한다.


def A_course(n):  # A 코스
    if n != None:
        print(n.name, '->', end=' ')  # 섬 N 방문
        A_course(n.left)
        A_course(n.right)

# B 코스 : 섬에 도착하면 도착한 섬의 관광을 미루고, 먼저 왼쪽 섬으로 관광을 진행하고 왼쪽 방향의 모든
#           섬들을 방문한 후에 돌아와서 섬을 관광한다. 그 다음엔 오른쪽 섬으로 관광한다.


def B_course(n):
    if n != None:
        B_course(n.left)
        print(n.name, '->', end=' ')
        B_course(n.right)

# C 코스 : 섬에 도착하면 도착한 섬의 관광을 미루고, 먼저 왼쪽 섬으로 관광을 진행하고 왼쪽 방향의 모든 섬들을
#           관광한 후에 돌아와서 오른쪽 섬으로 관광을 진행한다. 오른쪽 방향의 모든 섬들을 관광한 후에 돌아와서,
#           관광을 미루었던 섬을 관광한다.


def C_course(n):
    if n != None:
        C_course(n.left)
        C_course(n.right)
        print(n.name, '->', end=' ')


class Node:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right

def map():
    n1 = Node('H')
    n2 = Node('F')
    n3 = Node('S')
    n4 = Node('U')
    n5 = Node('E')
    n6 = Node('Z')
    n7 = Node('K')
    n8 = Node('N')
    n9 = Node('A')
    n10 = Node('Y')
    n11 = Node('T')

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    n5.left = n9
    n7.right = n10
    n9.right = n11

    return n1 # 시작섬 리턴

start = map()
print('A-코스:\t')
A_course(start)
print("")
print('B-코스:\t')
B_course(start)
print("")
print('C-코스:\t')
C_course(start)