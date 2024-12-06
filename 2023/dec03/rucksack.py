with open('input.txt') as file:

    df = file.read()

d = {} #empty dictionary
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(1,53):
    d[alpha[i - 1]] = i
print(d)
temp = []for line in df:

    for letter in line:
        temp.append(letter)
print(temp)
