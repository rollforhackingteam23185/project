user = input('equation:')

indexnum = 0
tokens = []

user = user.replace(" ", "")
print(user)

for i in range(len(user)):
    if user[i].isdigit():
        continue
    else:
        tokens.append(user[indexnum:i])
        tokens.append(user[i])
        indexnum = i+1
        print(user[i])
        print(indexnum)
        print(tokens)
tokens.append(user[indexnum:])

print(tokens)
