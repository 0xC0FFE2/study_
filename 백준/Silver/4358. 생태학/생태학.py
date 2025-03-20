from collections import Counter
import sys

trees = Counter()
total = 0

for line in sys.stdin:
    tree = line.strip()
    total += 1
    trees[tree] += 1

for x in sorted(trees.keys()):
    pst = (trees[x]/total)*100
    print(f'{x} {pst:.4f}')