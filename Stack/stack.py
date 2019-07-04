def push(item):
    stack.append(item)


def peek():
    if len(stack) != 0:
        return stack[-1]


def pop():
    if len(stack) != 0:
        item = stack.pop(-1)
        return item


stack = []

push('appled')
push('orange')
push('cherry')
print(stack, '\t<- top')
print('top : ', end='')
print(peek())

push('pear')
print(stack, '\t<- top')
print('top : ', end='')
print(peek())

pop()
print(stack, '\t<- top')
print('top : ', end='')
print(peek())