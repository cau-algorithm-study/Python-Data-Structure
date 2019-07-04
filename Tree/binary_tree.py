# -*- coding:utf-8 -*-
'''
Left Child-Right Sibling Tree Representation
'''


class Node:
    # 노드 생성자 항목과 왼쪽/오른쪽 자식노드 레퍼런스
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BinaryTree:
    # 트리 생성자
    def __init__(self):
        self.root = None  # 트리의 루트

    # 전위순회
    def preorder(self, n):
        if n != None:

            # 먼저 노드 방문
            print(str(n.item), ' ', end='')

            # 왼쪽 서브트리 방문 후, 오른쪽 서브트리 방문
            if n.left:
                self.preorder(n.left)

            if n.right:
                self.preorder(n.right)

    # 중위순회
    def inorder(self, n):
        if n != None:

            # 왼쪽 서브트리 방문 후 노드 방문
            if n.left:
                self.inorder(n.left)

            print(str(n.item), ' ', end='')

            if n.right:
                self.inorder(n.right)

    # 후위순회
    def postorder(self, n):
        if n != None:

            # 왼쪽과 오른쪽 서브트리 모두 방문 후 노드 방문
            if n.left:
                self.postorder(n.left)

            if n.right:
                self.postorder(n.right)

            print(str(n.item), ' ', end='')

    # 레벨순회
    def levelorder(self, root):
        q = []
        q.append(root)

        while(len(q) != 0):

            # 큐에서 첫 항목 삭제
            t = q.pop(0)

            print(str(t.item), ' ', end='')

            if t.left != None:
                q.append(t.left)

            if t.right != None:
                q.append(t.right)

    # 트리 높이 계산
    def height(self, root):

        if root == None:
            return 0

        return max(self.height(root.left), self.height(root.right)) + 1
