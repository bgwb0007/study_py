## https://programmers.co.kr/learn/courses/4008/lessons/66570
## http://pyengine.blogspot.com/2019/12/for-else.html
import math

if __name__ == '__main__':
    numbers = [int(input()) for _ in range(5)]
    multiplied = 1
    for number in numbers:
        multiplied *= number
        if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
            print('found')
            break
    else:
        print('not found')