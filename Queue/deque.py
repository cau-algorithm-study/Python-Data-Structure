from collections import deque
dq = deque('data') # 새 데크 객체를 생성

for elem in dq:
    print(elem.upper(), end='')
print()

# 맨 뒤와 맨 앞에 항목 삽입
dq.append('r')
dq.appendleft('k')
print(dq)

#맨 뒤와 맨 앞에 항목 삭제
dq.pop()
dq.popleft()
print(dq[-1]) # 맨 뒤 항목 출력

print('x' in dq)
dq.extend('structure')
dq.extendleft(reversed('python'))

print(dq)