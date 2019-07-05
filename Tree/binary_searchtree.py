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
        return self.get_item(self.root, k)

    def get_item(self, n, k):
        if n == None:  # 탐색 실패
            return None

        if n.key > k:
            # k가 노드의 key보다 작으면 왼쪽 서브트리 탐색
            return self.get_item(n.left, k)

        elif n.key < k:
            # k가 노드의 key보다 크면 오른쪽 서브트리 검색
            return self.get_item(n.right, k)

        else:
            # 탐색 성공
            return n.value

    # 삽입 연산
    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)

    def put_item(self, n, key, value):
        if n == None:
            # 새 노드 생성 (insert되는 시점)
            return Node(key, value)

        if n.key > key:
            # n의 왼쪽자식과 put_item()이 리턴하는 노드를 재연결
            n.left = self.put_item(n.left, key, value)

        elif n.key < key:
            # n의 오른쪽자식과 put_item()이 리턴하는 노드를 재연결
            n.right = self.put_item(n.right, key, value)

        else:
            # key가 이미 있으므로 value만 갱신
            n.value = value

        # 부모노드와 연결하기 위해 노드 n을 리턴
        return n

    # 최솟값 가진 노드 찾기
    # 루트로부터 왼쪽자식을 따라 내려가며, None을 만났을 때 None의 부모노드가 가진 key가 최솟값이다!

    def min(self):
        if self.root == None:
            return None
        return self.minimum(self.root)

    def minimum(self, n):
        if n.left == None:
            return n
        return self.minimum(n.left)

    # 최솟값 삭제
    def delete_min(self):
        if self.root == None:
            print('tree is empty')

        # 루트와 del_min()이 리턴하는 노드를 재연결
        self.root = self.del_min(self.root)

    def del_min(self, n):

        if n.left == None:
            # 최솟값 가진 노드의 오른쪽 자식을 리턴
            return n.right

        # n의 왼쪽자식과 del_min()이 리턴하는 노드를 재연결
        n.left = self.del_min(n.left)

        return n

    # 삭제 연산
    def delete(self, key):
        pass
