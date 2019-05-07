def character_frequency(phrase):

    frequency = { }

    for i in range(0, len(phrase)):
        frequency[phrase[i]] = 0
    for i in range(0, len(phrase)):
        frequency[phrase[i]] += 1

    return frequency


def main():

    phrase = str(input())
    
    print('[' + phrase + ']')

    frequency = character_frequency(phrase)

    print(frequency)


if __name__ == '__main__':

    try:
        main()

    except KeyboardInterrupt:
        print('Interruption')
