def num():
    M = eval(input("请输入第一个整数M(1<=M<N<=20000)："))
    N = eval(input("请输入第二个整数N(1<=M<N<=20000):"))
    flag = 1
    for i in range(M,N+1):
        for j in range(i+1,N+1):
            if main(i)==j and main(j)==i:
                print(i,j)
                flag = 0
    if flag:
        print('NONE')
def main(n):
    b=0
    for i in range(1,n):
        if n % i==0:
            b += i
    return b

num()