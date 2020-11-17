def isPrime(num):
    for n in range(2,num):
        if num % n == 0:
            print('Number is not Prime')
            break
        else:
            print('Number is Prime')
            break
isPrime(72)
