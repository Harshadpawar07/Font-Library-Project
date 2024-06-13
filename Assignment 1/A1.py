

num = 1

if num<=1:
    print("The number is not prime")
    
else:
    n = 2
    is_prime = True
    while n*n<=num:
        if  num%n==0:
            is_prime = False
            break
        n+=1
    if is_prime:
        print("Prime Number")

    else:
        print("Not Prime")
    
