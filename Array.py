#lifo
# 참조 지역성: 한번 참조된 곳은 다시 참조될 확률이 높다.
# 데이터 탐색이 어렵다
# 콜스택, 문자열 역순 출력, 연산자 후위표기법. 뒤로가기

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return -1
        else:
            self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0