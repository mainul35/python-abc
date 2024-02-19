def reverse_a_string_sol1(input):
    length = len(input)
    output = ''
    for i in range(length - 1, -1, -1):
        output += input[i]
    return output

def reverse_a_string_sol2(input):
    return input[::-1]

input = input()
print(reverse_a_string_sol1(input))
# print(reverse_a_string_sol2(input))
