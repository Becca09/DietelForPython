def bracket_pair_checker(brackets: str) -> bool:
    stack = []
    for bracket in brackets:
        if bracket in "{([":
            stack.append(bracket)
        if bracket in '}])':
            peek = stack[-1]
            if bracket == ')' and peek == '(':
                stack.pop()
            elif bracket == ']' and peek == '[':
                stack.pop()
            elif bracket == '}' and peek == '{':
                stack.pop()
            else:
                return False
    return len(stack) == 0


print(bracket_pair_checker('{{([][])}()}'))
print(bracket_pair_checker('((()]))'))
print(bracket_pair_checker('({[]})'))
print(bracket_pair_checker('({[){{]})'))


# num = 1
# def func():
#     global num
#     num+= 1
#     print(num)
# print(num)

# def func1():
#     num = 1
#     def func2():
#         num = 1
#         print(num)

