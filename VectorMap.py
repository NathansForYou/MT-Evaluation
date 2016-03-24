#!/usr/bin/env python

class VectorMap:
    def __init__(self):
        self.vectors = {}
        self.dim = 0

    def load_from_file(self, file_name):
        f = open(file_name)
        for line in f:
            arr = line.split()
            word = arr.pop(0)
            vec = [float(x) for x in arr]
            self.vectors[word] = vec
            if self.dim == 0:
                self.dim = len(vec)

    def get_vector(self, word):
        if word in self.vectors:
            return self.vectors[word]
        else:
            return [0.0] * self.dim
