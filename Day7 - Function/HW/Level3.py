#1
def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True
print(is_prime(7))

#2
a="a"
b="b" 
c='c'
list = [1,2,3,a,b,c,c]
def unique(list):
    for i in list:
            if list.count(i) > 1:
                 return False 
    return True
print(unique(list))

#3
