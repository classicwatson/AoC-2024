import sys

if len(sys.argv) != 2:
  print(f'Usage: python3 {sys.argv[0]} <input filename>')
  exit(1)

listA = []
listB = []

with open(sys.argv[1]) as f:
  for line in f:
    a,b = line.strip().split('   ')
    listA.append(a)
    listB.append(b)


combined = zip(sorted(listA), sorted(listB))
result = 0

for a,b in combined:
  result += abs(int(a)-int(b))

print(f'Result: {result}')

