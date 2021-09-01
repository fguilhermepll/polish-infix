class Stack:
    items = None
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def precedence(c):
    if(c == '+' or c == '-'):
        return 1
    elif (c == '*' or c == '/'):
        return 2
    elif (c == '^'):
        return 3
    else:
        return 0
def split(word):
    return [char for char in word]
    
def infixToPost(exp):
    stack = Stack()
    stack.push('#')
    output = []

    splitExp = split(exp)
    #print(splitExp)
    
    for c in splitExp:
        if(c == ' '):
            pass
        elif (c.isnumeric() or c.isalpha()):
            output.append(c)
        elif (c == '('):
            stack.push(c)
        elif (c == ')'):
            while (not stack.isEmpty() and stack.peek() != '('):
                item = stack.pop()
                output.append(item)
            stack.pop()
        else:
            while (not stack.isEmpty() and precedence(c) <= precedence(stack.peek())):
                output.append(stack.pop())

            stack.push(c)
    while (stack.peek() != '#'):
        output.append(stack.peek())
        stack.pop()
    outputJoin = ''.join(output)
    return outputJoin
    
print(infixToPost('3+1'))
print(infixToPost('x^y/(5*z)+10'))
