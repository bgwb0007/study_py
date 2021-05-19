# https://programmers.co.kr/learn/courses/4008/lessons/13173

import bisect
mylist = [1, 2, 3, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))

# 중복되는거 있으면 오른쪽거 탐색
print(bisect.bisect_right(mylist,3))
# 왼쪽거 탐색
print(bisect.bisect_left(mylist,3))

print(float('inf'))