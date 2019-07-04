from Singlylist import SList

# 이 파이썬 파일(모듈)이 메인이면
if __name__ == "__main__":
    s = SList()
    s.insert_front('orange')
    s.insert_front('apple')
    s.insert_after('cherry', s.head.next)
    s.insert_front('pear')
    s.print_list()

    print('cherry 는 %d번째 ' % s.search('cherry'))
    print('kiwi는 ', s.search('kiwi'))
    print('pear 다음 노드 삭제 후 : \t\t', end='')

    s.delete_after(s.head)
    s.print_list()

    print('첫 노드 삭제 후 : \t\t', end='')
    s.delte_front()
    s.print_list()

    print('첫 노드로 mango, strawberry 삽입 후 : \t', end='')
    s.insert_front('mango')
    s.insert_front('strawberry')
    s.print_list()
    s.delete_after(s.head.next.next)
    print('orange 다음 노드 삭제 후 : \t', end='')
    s.print_list()