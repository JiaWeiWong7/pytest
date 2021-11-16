num = int(input("请输入一个数字: "))

if num > 1:
    for i in range (2, num):
        if num % i == 0:
            print("不是质数")
            print(i, "*", num // i, "等于", num)
            break
    else:
        print("是质数")
else:
    print("不是质数")