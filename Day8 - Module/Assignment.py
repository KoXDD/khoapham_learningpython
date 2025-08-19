#1
import random
import string

def random_user_id():
    characters = string.ascii_letters + string.digits  
    user_id = ''.join(random.choice(characters) for _ in range(6))
    return user_id
print(random_user_id())

#2
def user_id_gen_by_user():
    length = int(input("Enter the number of characters per ID: "))
    count = int(input("Enter the number of IDs to generate: "))
    
    chars = string.ascii_letters + string.digits
    ids = [''.join(random.choice(chars) for _ in range(length)) for _ in range(count)]
    
    return ids
#3
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

#4
def list_of_hexa_colors(n=1):
    return ['#' + ''.join(random.choice('0123456789ABCDEF') for _ in range(6)) for _ in range(n)]

#5
def list_of_rgb_colors(n=1):
    return [rgb_color_gen() for _ in range(n)]

#6
def generate_colors(color_type, n=1):
    if color_type.lower() == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Error: choose 'hexa' or 'rgb'"

#7
def shuffle_list(lst):
    random.shuffle(lst)
    return lst

#8
def random_unique_numbers():
    return random.sample(range(10), 7)