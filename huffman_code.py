import heapq

class Node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.right = None
        self.left = None

    def __lt__(self, other):
        return self.frequency < other.frequency


class Huffman:
    def __init__(self, text):
        self.text = text
        self.characters_frequency = {}
        self.characters_codes = {}
        self.heap = []

        self.get_character_frequency()
        self.fill_heap()

    def get_character_frequency(self):

        for character in self.text:
            if not character in self.characters_frequency:
                self.characters_frequency[character] = 0
            self.characters_frequency[character] += 1

    def fill_heap(self):

        for key in self.characters_frequency:
            heapq.heappush(self.heap, Node(key, self.characters_frequency[key]))


def main():

    text = str(input())
    
    print('[' + text + ']')

    print('text in ASCII [' + str(len(text) * 8) + ' BITS]')

    huffman = Huffman(text)

    print(huffman.characters_frequency)

    for element in huffman.heap:
        print(str(element.character) + ' : ' + str(element.frequency))


if __name__ == '__main__':

    try:
        main()

    except KeyboardInterrupt:
        print('Interruption')
