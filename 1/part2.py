import sys

if len(sys.argv) != 2:
  print(f'Usage: python3 {sys.argv[0]} <input filename>')
  exit(1)

listA = []
listB = []

with open(sys.argv[1]) as f:
  for line in f:
    a,b = line.strip().split('   ')
    listA.append(int(a))
    listB.append(int(b))

counts = {}

for target in listA:
  if target in counts.keys():
    counts.update({target: counts[target] * 2})
  else:
    counts[target] = listB.count(target)

result = 0

for k in counts:
  result += k * counts[k]

print(f'Result: {result}')

