#1  #Declare a function named evens_and_odds .
#  It takes a positive integer as parameter and it counts number of evens and odds in the number.
    #print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
def evens_and_odds(pi):
    a=0
    b=0
    for i in range(pi+1):
        if i%2 == 0:
            a+=i
        else:
            b+=i
    return a,b
print("So so chan va so le lan luot la",evens_and_odds(100))


#1.5 Call your function factorial,
#  it takes a whole number as a parameter and it return a factorial of the number
def factorial(wn):
    giaithua = 1
    for i in range (1,wn+1):
        giaithua*=i 
    return giaithua
print("Giai thua so da cho la",factorial(5))

#2 Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(a):
    if not a:
        return True
    else:
        return "Me huy beo that"
print(is_empty("Me thang huy beo"))