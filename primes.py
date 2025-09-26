def is_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    for i in range(3, number):
        if number % i == 0:
            return False
        else:
            return True

