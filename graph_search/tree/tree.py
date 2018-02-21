# Simple OOP Binary Tree
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self, root):
        self.root = root

    def insert_left(self, child):
        if self.root.left is None:
            self.root.left = child
        else: # push existing child down 1 level in tree
            child.left = self.root.left
            self.root.left = child

    def insert_right(self, child):
        if self.root.right is None:
            self.root.right = child
        else: # push existing child down 1 level in tree
            child.right = self.root.right
            self.root.right = child

# Thinking of tree as Maps
{
    'val': 'A',
    'children': [
        {
            'val': 'B',
            'children': [
                {'val': 'D'},
                {'val': 'E'},
            ]
        },
        {
            'val': 'C',
            'children': [
                {'val': 'F'},
                {'val': 'G'},
                {'val': 'H'}
            ]
        }
    ]
}

from collections import defaultdict
from itertools import product
import os


# O(num_words * length of each word + num_words * num_neighors of each word)
# O(N...?)
def build_graph(words):
    buckets = defaultdict(list)
    graph = defaultdict(set)

    # create a vertex for every word in graph
    for word in words:
        for i in range(len(word)):
            # Create buckets for each word by removing 1 char
            bucket = '{}_{}'.format(word[:i], word[i + 1:])
            buckets[bucket].append(word)

    # add vertices and edges for words in the same bucket
    for bucket, mutual_neighbors in buckets.items():
        for word1, word2 in product(mutual_neighbors, repeat=2):
            if word1 != word2:
                graph[word1].add(word2)
                graph[word2].add(word1)

    return graph


def get_words(vocabulary_file):
    for line in open(vocabulary_file, 'r'):
        yield line[:-1]  # remove newline character


vocabulary_file = os.path.join(os.path.dirname(__file__), 'words.txt')
word_graph = build_graph(get_words(vocabulary_file))

# set(['POOL', 'WOOL', 'FOWL', 'FOAL', 'FOUL', ... ])

from collections import deque


def traverse(graph, starting_vertex):
    visited = set()
    queue = deque([[starting_vertex]])
    # O(V) to for each vertex
    while queue:
        path = queue.popleft()
        vertex = path[-1]
        yield vertex, path
        # O(E) for each edge
        for neighbor in graph[vertex] - visited:
            visited.add(neighbor)
            queue.append(path + [neighbor])

if __name__ == '__main__':
    for vertex, path in traverse(word_graph, 'FOOL'):
        if vertex == 'SAGE':
            print ' -> '.join(path)
            # FOOL -> FOOD -> FOLD -> SOLD -> SOLE -> SALE -> SAGE
