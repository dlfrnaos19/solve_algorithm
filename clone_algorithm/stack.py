class Stack():
    def __init__(self):
        self.items = []    
    # 빈 리스트일 경우 False, 값이 있으면 True를 반환하므로, not으로 전환
    def isEmpty(self):
        return not bool(self.items)

    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("stack is empty")
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("stack is empty")
    
    def __repr__(self):
        return repr(self.items)

if __name__ == "__main__":
    stack = Stack()
    print("check stack empty", stack.isEmpty())
    for i in range(10):
        stack.push(i)
    print("stack size", stack.size())
    print("stack peek", stack.peek())
    print('pop', stack.pop())
    print("stack peek", stack.peek())
    print('isempty', stack.isEmpty())
    print(stack)
    
    
    
    