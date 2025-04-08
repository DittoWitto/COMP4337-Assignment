import sys

def parseArguments():
  if len(sys.argv) != 4:
    print("Usage: python3 Dimy.py <t> <k> <n>")
    sys.exit(1)
  t = int(sys.argv[1])
  k = int(sys.argv[2])
  n = int(sys.argv[3])
  # t ∈ {15,18,21,24,27,30}
  if t not in [15, 18, 21, 24, 27, 30]:
    print("t must be one of {15,18,21,24,27,30}")
    sys.exit(1)
  return t, k, n

def main():
  t, k, n = parseArguments()
  print(f"t: {t}, k: {k}, n: {n}")