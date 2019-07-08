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
    '''
    get()의 탐색 과정과 같이 삭제할 노드를 찾은 후, 이진 탐색트리 조건을 만족하도록
    삭제된 노드의 부모노드와 자식노드들을 연결해 주어야 한다.

    삭제되는 노드 N
    case 0 : 자식이 없는 경우   => N의 부모노드가 N을 가리키던 레퍼런스를 None으로 만든다 
    case 1 : 자식이 하나인 경우 => N의 부모노드와 N의 자식노드를 직접 연결한다
    case 2 : 자식이 둘인 경우   => N의 자리에 이진탐색트리를 중위순회하면서 N을 방문한 직후에
                                방문되는 노드를 N의 자리로 옮긴다.
    '''

    def delete(self, key):
        # 루트와 del_node()가 리턴하는 노드를 재연결
        self.root = self.del_node(self.root, k)

    def del_node(self, n, k):
        if n == None:
            return None

        if n.key > k:
            # n의 왼쪽자식과 del_node()가 리턴하는 노드를 재연결
            n.left = self.del_node(n.left, k)

        elif n.key < k:
            # n의 오른쪽 자식과 del_node()가 리턴하는 노드를 재연결
            n.right = self.del_node(n.right, k)

        else:
            if n.right == None:  # case 0 , case 1 (오른쪽자식이 None인 경우)
                return n.left
            if n.left == None:  # case 1 (왼쪽자식이 None인 경우)
                return n.right

            # case 2
            # 삭제될 노드
            target = n

            # target의 중위후속자를 찾아 n이 참조하게 함
            n = self.minimum(target.right)

            # n의 오른쪽자식과 target의 오른쪽자식 연결
            n.right = self.del_min(target.right)
            # n의 왼쪽자식과 target의 왼쪽자식 연결
            n.left = target.left

        return n
