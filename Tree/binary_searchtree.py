class Node:
    # 노드생성자:: 키, 항목, 왼쪽과 오른쪽 자식 레퍼런스
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BST:
    # 트리 생성자
    def __init__(self):
        self.root = None

    # 탐색 연산
    def get(self, key):
        pass
    
    # 삽입 연산
    def put(self, key, value):
        pass
    
    # 최솟값 가진 노드 찾기
    def min(self):
        pass

    # 최솟값 삭제
    def delete_min(self):
        pass
    
    # 삭제 연산
    def delete(self, key):
        pass