Str = "The quick Brow Fox"
lower = 0
upper = 0
for i in Str:
    if i.islower():
        lower += 1
    elif i.isupper():
        upper += 1
print("No. of Upper case characters:", upper)
print("No. of Lower case characters:", lower)