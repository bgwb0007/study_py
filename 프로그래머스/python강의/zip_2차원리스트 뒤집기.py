## https://programmers.co.kr/learn/courses/4008/lessons/13318

mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_list = list(map(list, zip(*mylist)))
for i in new_list:
    print(i)
print()
print("90도 회전")
## 90도 회전
list2 = list(map(list, zip(*mylist[::-1])))
for i in list2:
    print(i)

print()
print("뒤집기")
list3 =list(map(list, zip(*mylist)))
for i in list3:
    print(i)