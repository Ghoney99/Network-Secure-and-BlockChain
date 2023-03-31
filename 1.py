import hashlib
from bitmap import BitMap

class BloomFilter:
    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.n = 0
        self.bf = BitMap(m)

    def getPositions(self, item):
        positions = []
        for i in range(1, self.k+1):
            h = hashlib.sha256((item + str(i)).encode()).hexdigest()
            pos = int(h, 16) % self.m
            positions.append(pos)
        return positions

    def add(self, item):
        positions = self.getPositions(item)
        for pos in positions:
            self.bf.set(pos)
        self.n += 1

    def contains(self, item):
        positions = self.getPositions(item)
        for pos in positions:
            if not self.bf[pos]:
                return False
        return True

    def reset(self):
        self.bf.reset()
        self.n = 0

    def __repr__(self):
        num_set_bits = self.bf.count()
        return f"M = {self.m}, F = {self.k}\n" \
               f"BitMap = {self.bf}\n" \
               f"항목의 수 = {self.n}, 1인 비트수 = {num_set_bits}"

if __name__ == "__main__":
    bf = BloomFilter(53, 3)
    for ch in "AEIOU":
        bf.add(ch)
    print(bf)
    for ch in "ABCDEFGHIJ":
        print(ch, bf.contains(ch))
