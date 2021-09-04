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

def parseToBar(exp):
    outputList = []
    for c in exp:
        if(c.isnumeric() or c.isalpha()):
            outputList.append('|')
            outputList.append(c)
            outputList.append('|')
        else:
            outputList.append(c)
    outputList = "".join(outputList)
    return outputList

def runWhile(exp, x):
    outputList = []
    outputList.append('|')

    for c in exp:
        if(c.isnumeric() or c.isalpha()):
            outputList.append(c)
            
        else:
            break
        outputList.append('|')
    return outputList


def infixToPostWithWhile(exp):
    stack = Stack()
    stack.push('#')

    output = []

    splitExp = split(exp)
    length = len(splitExp)
    op = 0
    
    while op < len(exp):
        if(splitExp[op] == ' '):
            op += 1
        elif(splitExp[op].isnumeric() or splitExp[op].isalpha()):
            strp = ''
            while(splitExp[op].isnumeric() or splitExp[op].isalpha()):
                strp += splitExp[op]
                op+=1
                if(op == len(exp)):
                    break

            output.append('|')
            output.append(strp)
            output.append('|')
            
        elif (splitExp[op] == '('):
            stack.push(splitExp[op])
            op += 1
        elif (splitExp[op] == ')'):
            while (not stack.isEmpty() and stack.peek() != '('):
                item = stack.pop()
                output.append(item)
            stack.pop()
            op += 1
        else:
            while (not stack.isEmpty() and precedence(splitExp[op]) <= precedence(stack.peek())):
                output.append(stack.pop())
            stack.push(splitExp[op])
            op += 1
    while (stack.peek() != '#'):
           output.append(stack.peek())
           stack.pop()
    outputJoin = ''.join(output)

    return outputJoin


def infixToPost(exp):
    stack = Stack()
    stack.push('#')
    output = []
    outputWithBars = []

    splitExp = split(exp)
  
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
    outputWithBars = parseToBar(outputJoin)

    return outputWithBars


print('WITH CORRECT BARS: ')
print(infixToPostWithWhile('30+12'))
print(infixToPostWithWhile('30+1'))
print(infixToPostWithWhile('32 + 3351- 93'))
print(infixToPostWithWhile('333+1 + 1x0'))
print(infixToPostWithWhile('AZ+B/C3*(D2-A)^F^H'))
print(infixToPostWithWhile('1x ^ y / (5 * z) + 1033'))
print('')
print(infixToPost('32+1'))
print(infixToPost('A+B'))
print(infixToPost('A+B/C*(D-A)^F^H'))
print(infixToPost('A+B/C*(D-A)^F^H'))
