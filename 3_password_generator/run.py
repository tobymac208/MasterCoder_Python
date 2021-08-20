import random

def main():
    # let's get:
    #   - lowercase (3)
    lowercase = ''
    LOWERCASE_VALUES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z']
    #   - uppercase (3)
    uppercase = ''
    UPPERCASE_VALUES = [x.upper() for x in LOWERCASE_VALUES]
    #   - numbers (3)
    numbers = ''
    NUMBER_RANGE = 10
    #   - puncutation
    punctuation = ''
    PUNCTUATION_VALUES = "!#$%&'()*+,-./:;<=>?@[\]^_{|}~"

    # generate three numbers. we'll concatenate these later
    # generate three random upper letters
    # generate three random lower letters
    for _ in range(3):
        # generate a new random lowercase value
        numbers += str(random.randint(0, NUMBER_RANGE-1))
        lowercase += LOWERCASE_VALUES[random.randint(0, 25)]
        uppercase += UPPERCASE_VALUES[random.randint(0, 25)]
        punctuation += PUNCTUATION_VALUES[random.randint(0, len(PUNCTUATION_VALUES)-1)]
    
    print('Your new password: ')
    print(punctuation + uppercase + lowercase + numbers)


if __name__ == '__main__':
    main()
