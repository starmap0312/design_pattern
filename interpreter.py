# Interpreter Pattern (an OK design pattern)
# - should be called Expression Design Pattern (cause it ends with -er)
# - composite and indivisual nodes are treated uniformly
# 

class Expression(object):
    # an interface for all nodes of the syntax tree

    def interpret(self):
        raise NotImplementedError

class Number(Expression):

    def __init__(self, number):
        self.number = number

    def interpret(self, variables):
        return self.number

class Plus(Expression):
    # composite node, having left and right children

    def __init__(self, left, right):
        self.leftOperand = left
        self.rightOperand = right

    def interpret(self, variables):
        return self.leftOperand.interpret(variables) + self.rightOperand.interpret(variables)


class Minus(Expression):
    # composite node, having left and right children

    def __init__(self, left, right):
        self.leftOperand = left
        self.rightOperand = right

    def interpret(self, variables):
        return self.leftOperand.interpret(variables) - self.rightOperand.interpret(variables)

class Variable(Expression):
    # indivisual node

    def __init__(self, name):
        self.name = name

    def interpret(self, variables):
        if self.name not in variables:
            return 0
        return variables[self.name].interpret(variables)

class Parser(Expression):
    # create the syntax tree by parsing the expression string

    def __init__(self, expression):
        expressionStack = []
        for token in expression.split(' '):
            if token == '+':
                subExpression = Plus(expressionStack.pop(), expressionStack.pop())
                expressionStack.append(subExpression)
            elif token == '-':
                right = expressionStack.pop()
                left = expressionStack.pop()
                subExpression = Minus(left, right)
                expressionStack.append(subExpression)
            else:
                expressionStack.append(Variable(token))
        self.syntaxTree = expressionStack.pop()

    def interpret(self, context):
        return self.syntaxTree.interpret(context)

sentence = Parser(expression='w x z - +')
variables = dict() #a shared collection of Number objects
variables['w'] = Number(5)
variables['x'] = Number(10)
variables['z'] = Number(42)
print sentence.interpret(variables)
