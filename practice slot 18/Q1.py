def check(seq):
    for i in seq:
        if i <= 0:
            print('False sequence')
            return False
    return seq
    
    

def check_prime(n):
    if n < 1:
        return False
    
    else:
        for i in range (2, n):
            if n % i == 0:
                return False
        return True
  
  
sequence = [3, 1, 8, 7, 9, 11]
checked_seq = check(sequence)
prime_seq = []
while True:
    if checked_seq == False:
        print('enter new sequence')
        break
    
    else:
        for i in checked_seq:
            if check_prime(i) == True:
                prime_seq.append(i)
        m = max(prime_seq)
        total = sum(prime_seq)
        print('The prime numbers')
        print('=================')
        print(f'The sequence numbers: {checked_seq}')
        print(f'The prime numbers: {prime_seq}')
        print(f'The largest number: {m}')
        print(f'You got the total number of the prime number: {total}')
        break