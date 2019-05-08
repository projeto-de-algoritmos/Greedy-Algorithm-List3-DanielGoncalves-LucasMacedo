import heapq

class Node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.right = None
        self.left = None
    # para a heap não dar erro no heappush quando há frequencias iguais
    def __lt__(self, other):
        return self.frequency < other.frequency


class Huffman:
    def __init__(self, text):
        self.text = text
        self.characters_frequency = {}
        self.characters_codes = {}
        self.heap = []
        self.compressed_text = ''

        for character in self.text:
            if not character in self.characters_codes:
                self.characters_codes[character] = ''

        self.compress_text()

    def get_character_frequency(self):

        for character in self.text:
            if not character in self.characters_frequency:
                self.characters_frequency[character] = 0
            self.characters_frequency[character] += 1

    def fill_heap(self):

        for key in self.characters_frequency:
            heapq.heappush(self.heap, Node(key, self.characters_frequency[key]))

    def join_nodes(self):
        # juntar os nos da heap ate que tenha so um no com os filhos
        # ele pega as duas menores frequencias da heap e junta ate que tenha so 1
        while(len(self.heap) > 1):
            node_one = heapq.heappop(self.heap)
            node_two = heapq.heappop(self.heap)
            print("ESTE EH O 1: " + str(node_one.character) + " " + str(node_one.frequency))
            print("ESTE EH O 2: " + str(node_two.character) + " " + str(node_two.frequency))
            join_node = Node(None, node_one.frequency + node_two.frequency)
            join_node.left = node_one
            join_node.right = node_two

            heapq.heappush(self.heap, join_node)


def main():

    text = str(input())
    
    print('[' + text + ']')

    print('text in ASCII [' + str(len(text) * 8) + ' BITS]')

    huffman = Huffman(text)

    print(huffman.characters_frequency)

    for element in huffman.heap:
        print(str(element.character) + ' : ' + str(element.frequency))

    print(huffman.characters_codes)


if __name__ == '__main__':

    try:
        main()

    except KeyboardInterrupt:
        print('Interruption')
