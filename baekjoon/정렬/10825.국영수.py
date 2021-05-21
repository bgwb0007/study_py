## https://www.acmicpc.net/problem/10825

N = int(input())

students = []
for _ in range(N):
    temp = input().split()
    students.append((temp[0], int(temp[1]), int(temp[2]), int(temp[3])))

def setting(data):
    return (-data[1], data[2], -data[3], data[0])

answer = sorted(students, key=setting)
for student in answer:
    print(student[0])