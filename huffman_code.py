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

        self.encoded_text = ''
        self.decoded_text = ''

        for character in self.text:
            if not character in self.characters_codes:
                self.characters_codes[character] = ''

        self.encode_text()
        self.decode_text()

    def get_character_frequency(self):

        for character in self.text:
            if not character in self.characters_frequency:
                self.characters_frequency[character] = 0
            self.characters_frequency[character] += 1

    def fill_heap(self):

        for key in self.characters_frequency:
            heapq.heappush(self.heap, Node(
                key, self.characters_frequency[key]))

    def join_nodes(self):
        # juntar os nos da heap ate que tenha so um no com os filhos
        # ele pega as duas menores frequencias da heap e junta ate que tenha so 1
        while(len(self.heap) > 1):
            node_one = heapq.heappop(self.heap)
            node_two = heapq.heappop(self.heap)

            # print("Primeiro node do join: " + str(node_one.character) + " " + str(node_one.frequency))
            # print("Segundo node do join: " + str(node_two.character) + " " + str(node_two.frequency))

            join_node = Node(None, node_one.frequency + node_two.frequency)
            join_node.left = node_one
            join_node.right = node_two

            heapq.heappush(self.heap, join_node)

    def print_huffman_tree(self, node):

        if(node == None):
            return

        print(str(node.character) + ' : ' + str(node.frequency))

        self.print_huffman_tree(node.left)
        self.print_huffman_tree(node.right)

    def get_characters_codes(self, node, code):
        if len(self.characters_frequency) == 1:
            self.characters_codes[node.character] = '0'
        else:
            if(node == None):
                return

            if(node.character != None and self.characters_codes[node.character] == ''):
                self.characters_codes[node.character] = code

            self.get_characters_codes(node.left, code + '0')
            self.get_characters_codes(node.right, code + '1')

    def build_encoded_text(self):

        for character in self.text:
            self.encoded_text += self.characters_codes[character]

    def encode_text(self):

        self.get_character_frequency()
        self.fill_heap()
        self.join_nodes()
        # self.print_huffman_tree(self.heap[0])
        self.get_characters_codes(self.heap[0], '')
        self.build_encoded_text()

    def decode_text(self):

        node = self.heap[0]
        if len(self.characters_frequency) == 1:
            for bit in self.encoded_text:
                self.decoded_text += node.character
        else:
            for bit in self.encoded_text:
                if bit == '0':
                    node = node.left
                else:
                    node = node.right
                if node.left == None and node.right == None:
                    self.decoded_text += node.character
                    node = self.heap[0]


def main():

    text = str(input())

    huffman = Huffman(text)

    print('[' + huffman.text + ']')

    print('Text in ASCII [' + str(len(huffman.text) * 8) + ' BITS]')

    print(huffman.characters_frequency)

    # for element in huffman.heap:
    #     print(str(element.character) + ' : ' + str(element.frequency))

    print(huffman.characters_codes)

    print('Text encoded [' + huffman.encoded_text + ']')

    print('Text encoded [' + str(len(huffman.encoded_text)) + ' BITS]')

    print('Bits saved [' + str(len(huffman.text) *
                               8 - len(huffman.encoded_text)) + ' BITS]')

    print('Text decoded [' + huffman.decoded_text + ']')


# if __name__ == '__main__':

#     try:
#         main()

#     except KeyboardInterrupt:
#         print('Interruption')
