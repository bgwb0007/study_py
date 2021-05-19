## https://programmers.co.kr/learn/courses/4008/lessons/13323

## a를 b로 나눈 몫과 나머지를 출력. *-> unpacking
a, b = map(int, input().strip().split(' '))
print(*divmod(a,b))