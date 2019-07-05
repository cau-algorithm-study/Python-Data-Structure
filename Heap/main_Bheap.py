from binary_heap import BHeap
if __name__ == "__main__":
    a = [None] * 1
    a.append([90, 'watermelon'])
    a.append([80, 'pear'])
    a.append([70, 'melon'])
    a.append([50, 'lime'])
    a.append([60, 'mango'])
    a.append([20, 'cherry'])
    a.append([30, 'grape'])
    a.append([35, 'orange'])
    a.append([10, 'apricot'])
    a.append([15, 'banana'])
    a.append([45, 'lemon'])
    a.append([40, 'kiwi'])
    b = BHeap(a)

    print('Before heap construction :')
    b.print_heap()
    b.create_heap()

    print('Minimum Heap : ')
    b.print_heap()

    print('After deleting minimum value ')
    print(b.delete_min())
    b.print_heap()
    b.insert([5, 'apple'])
    print('Inserting 5')
    b.print_heap()
