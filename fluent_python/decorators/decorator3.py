from dis import dis

b =6
def f1(a):
    print(a)
    print(b)

f1(3)
dis(f1)