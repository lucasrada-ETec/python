for i in range(1,11):
    factorial=1
    if i==8:continue
    for c in range(i,0,-1):
        factorial=factorial*c
    print(factorial,"= {}!".format(i))