import cmath
print("二次方程格式为：ax ** 2 + bx + c = 0")
print("请分别输入系数：a, b, c: ")
a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))

d = b ** 2 - 4 * a * c
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('结果为 {0} 和 {1}'.format(sol1, sol2))