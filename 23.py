# Reverse String

def reverse_string(s):
    return ''.join([s[i] for i in range(len(s)-1, -1, -1)])

input_string = "hello"
reversed_string = reverse_string(input_string)
print(reversed_string)
