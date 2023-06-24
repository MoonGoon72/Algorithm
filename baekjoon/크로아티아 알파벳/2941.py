cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

result = len(word)

for alpha in cro_alpha:
    result -= word.count(alpha)

print(result)