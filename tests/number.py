import random

str="123456789abcdefghijklmnopqrstuvwxyz"
for i in range(20):
    res = random.sample(str,8)
    if not res[0].isdigit():
        print(''.join(res)+"@163.com")
    else:
        res[0] = random.choice("abcdefghijklmnopqrstuvwuxyz")
        print(''.join(res)+"@163.com")
