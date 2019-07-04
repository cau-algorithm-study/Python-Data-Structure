from Circularlist import CList

if __name__ == "__main__":
    s = CList()
    s.insert('pear')
    s.insert('cherry')
    s.insert('orange')
    s.insert('apple')
    s.print_list()

    print('s의 길이 =', s.no_items())
    print('s의 첫 항목 : ', s.first())

    s.delete()
    print('첫 노드 삭제 후 : ', end='')
    s.print_list()

    print('s의 길이 =', s.no_items())
    print('s의 첫 항목 : ', s.first())

    s.delete()
    print('첫 노드 삭제 후 : ', end='')
    s.print_list()

    s.delete()
    print('첫 노드 삭제 후 : ', end='')
    s.print_list()

    s.delete()
    print('첫 노드 삭제 후 : ', end='')
    s.print_list()
