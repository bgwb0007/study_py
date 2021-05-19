## https://programmers.co.kr/learn/courses/4008/lessons/72547

def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer