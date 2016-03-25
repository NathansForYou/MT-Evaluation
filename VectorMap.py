#!/usr/bin/env python

class VectorMap:
    def __init__(self):
        self.vectors = {}
        self.dim = 0
        self.stopwords = self.load_stopwords()

    def load_stopwords(self):
        stopwords = set()
        f = open("stopwords")
        for line in f:
            for word in line.split("\'"):
                word = word.strip()
                stopwords.add(word)
        return stopwords

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
            return self.vectors["OOL"]

    def sentence_to_vector(self, line):
        words = line.split()
        sen_vec = [0.0] * self.dim

        for word in words:
            if word not in self.stopwords:
                sen_vec = [sum(z) for z in zip(sen_vec, self.get_vector(word))]

        return sen_vec
