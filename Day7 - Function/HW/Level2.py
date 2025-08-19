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
        return "Tep rong"
    else:
        return "Tep nay ko rong"
print(is_empty("Me thang huy beo"))

#3 Write different functions which take lists. They should calculate_mean, calculate_median,
#  calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(list):
    return sum(list) / len(list)

def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]
    
def calculate_mode(lst):
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    max_freq = max(frequency.values())
    modes = [key for key, val in frequency.items() if val == max_freq]
    if len(modes) == len(set(lst)):
        return "No mode"
    return modes


def calculate_range(lst):
    return max(lst) - min(lst)


def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    import math
    return math.sqrt(calculate_variance(lst))
numbers = [1, 2, 2, 3, 4, 5, 5, 5]

print("Mean:", calculate_mean(numbers))
print("Median:", calculate_median(numbers))
print("Mode:", calculate_mode(numbers))
print("Range:", calculate_range(numbers))
print("Variance:", calculate_variance(numbers))
print("Standard Deviation:", calculate_std(numbers))

