import string


class stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


def in_to_post_converter(input):
    precedence = {
        "*": 2,
        "/": 2,
        "+": 1,
        "-": 1
    }

    operator_stack = stack()
    postfix_list = []
    token_list = list(input)  # input.split('')

    if token_list[0] in '+-' and token_list[-1] not in '/*' or token_list[0] == '':
        for token in token_list:
            if token in string.ascii_lowercase or token in string.ascii_uppercase or token in string.digits:
                postfix_list.append(token)

            else:
                while (not operator_stack.is_empty()) and (precedence[operator_stack.peek()] >= precedence[token]):
                    postfix_list.append(operator_stack.pop())
                operator_stack.push(token)

        while not operator_stack.is_empty():
            postfix_list.append(operator_stack.pop())
        print(' '.join(postfix_list))
    else:
        print('There is a syntax error')


d = str(input())

in_to_post_converter(d)

# elif token == '(':
#     opStack.push(token)
# elif token == ')':
#     topToken = opStack.pop()
#     while topToken != '(':
#         postfixList.append(topToken)
#         topToken = opStack.pop()
# this is for bracket validator
