import random

rand_let = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
rand_s = ['@', '#', '$', '&']
result = []

while len(result) < 8:
    res_num = str(random.randint(1, 9))
    res_let = random.choice(rand_let)
    res_letA = res_let.upper()
    res_s = random.choice(rand_s)

    result.append(res_let)
    result.append(res_num)
    result.append(res_letA)
    result.append(res_s)

random.shuffle(result)

password = ''.join(result[:8])
print(password)
