import sys

# Defining the main function
def main():
    '''This is the main function'''
    range_ = input('Enter the range: ')
    result = prime_composite(range_)
    print(result)

def prime_composite(range_):
    '''This function gets the prime or composite numbers'''
    range_ = range_.split(',')
    first_number = int(range_[0])
    second_number = int(range_[1])
    for number in range(first_number, second_number + 1):
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    result = 'Composite'
                    break
            else:
                result = 'Prime'
        else:
            result = 'Composite'
        print(number, 'is', result)
    return result

if __name__ == '__main__':
    main()