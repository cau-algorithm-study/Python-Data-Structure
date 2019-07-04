def add(item):
    q.append(item)


def remove():
    if len(q) != 0:
        item = q.pop(0)
        return item


def print_q():
    print('front -> ', end='')
    for i in range(len(q)):
        print('{!s:<8}'.format(q[i]), end='')
    print(' <- rear')


q = []

add('apple')
add('orange')
add('cherry')
add('pear')
print_q()
remove()
print_q()
remove()
print_q()
