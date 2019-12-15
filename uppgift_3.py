

def divisible_by_five(x):
    if x % 5 == 0:
        return True
    else:
        return False

number = input("type a number ")        

print(divisible_by_five(int(number)))