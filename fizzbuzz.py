def fizzbuzz(n):
    result = []
    
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(i)
    
    return result

def print_fizzbuzz(n=100):
    result = fizzbuzz(n)
    for item in result:
        print(item)

if __name__ == "__main__":
    print_fizzbuzz()