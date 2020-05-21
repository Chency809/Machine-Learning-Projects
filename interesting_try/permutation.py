# string = "abc"
# n = len(string)
#
# def permutate(string, s, n, new_string):
#     if (s == n):
#         print(new_string)
#     else:
#         for i in range(s, n):
#             new_string += string[i]
#             s = s+1
#             permutate(string, s, n, "")
#
# permutate(string, 0, n, "")

ini_str = "abc"

# Printing initial string
print("Initial string", ini_str)

# Finding all permuatation
result = []


def permute(data, i, length):
    if i == length:
        result.append(''.join(data))
    else:
        for j in range(i, length):
            # swap
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i]


permute(list(ini_str), 0, len(ini_str))

# Printing result
print("Resultant permutations", str(result))

"""
from itertools import combinations

n, m = input().split()
n = int(n)
m = int(m)
num_list = input().split()
num_list = list(map(int, num_list))

print(num_list)
print(n)
print(m)

confirm_ai = False
for i in num_list:
    if i > 10 ** 9 or i < 1:
        confirm_ai = True
        break

for i in range(0, n):
    num_list[i] = num_list[i] % m

if (n > 35 or n < 1) or (m > 10 ** 9 or m < 1) or (confirm_ai):
    print(" Input Error! ")
else:
    answer = 0
    for i in range(0, n):
        result_list = list(combinations(num_list, i+1))
        for i in result_list:
            if sum(i) % m > answer:
                answer = sum(i) % m
    print(answer)
"""