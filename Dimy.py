import sys
import os
import time
from pyshamir import split

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
  # task1: k >= 3 and n >= 5 and k < 
  if not (k >= 3 and n >= 5 and k < n):
    print("Constraints: k >= 3, n >= 5, and k < n")
    sys.exit(1)

  return t, k, n

#task1: generate a 32-byte EphID
def generate_ephid():
  return os.urandom(32)

#task2: Shamir Secret Sharing mechanism
def sss_ephid(ephid, k, n):
    shares = split(ephid, n, k)
    return shares

def main():
  t, k, n = parseArguments()
  print(f"t: {t}, k: {k}, n: {n}")

  try:
      while True:
          ephid = generate_ephid()
          shares = sss_ephid(ephid, k, n)

          print(f"----New EphID: {ephid.hex()}")
          print("----Generated Shares:")
          for i, share in enumerate(shares, 1):
              print(f"    Share {i}: {share}")

          time.sleep(t)

  except KeyboardInterrupt:
      print("\n Client stop")


if __name__ == "__main__":
  main()