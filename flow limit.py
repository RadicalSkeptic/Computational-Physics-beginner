import os
def clear(): return os.system('cls')


under = 1
over = 1
count = 1
while(count <= 10000):
    under = under/2
    over = over*2
    print("Count:", count, "     Under:", under, "     Over:", over,)
    count += 1
    # clear()
