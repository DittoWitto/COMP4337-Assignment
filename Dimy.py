import sys
import os
import socket
import time
import random
from secretsharing import SecretSharer

broadcast_IP = '255.255.255.255'
broadcast_port = 12345

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
  # task1: k >= 3 and n >= 5 and k < n
  if not (k >= 3 and n >= 5 and k < n):
    print("Constraints: k >= 3, n >= 5, and k < n")
    sys.exit(1)

  return t, k, n

#task1: generate a 32-byte EphID
def generate_ephid():
  return os.urandom(32)

#task2: Shamir Secret Sharing mechanism
def share_ephid(ephid, k, n):
  ephid_hex = ephid.hex()
  shares = SecretSharer.split_secret(ephid_hex, k, n)
  return shares

#task3: broadcast the shares
def broadcast_shares(shares, broadcast_IP, broadcast_port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

  for i, share in enumerate(shares, start=1):
    #task3a: message drop mechanism
    drop = random.random() < 0.5
    if drop:
      print(f"share {i} drop")

    else:
      share_bytes = share.encode()
      sock.sendto(share_bytes, (broadcast_IP, broadcast_port))
      print(f"broadcasted share {i}: {share}")
    time.sleep(3)
  sock.close()
    

def main():
  t, k, n = parseArguments()
  print(f"t: {t}, k: {k}, n: {n}")

  try:
    while True:
      ephid = generate_ephid()
      print(f"******EphID: {ephid.hex()}")

      shares = share_ephid(ephid, k, n)
      print("******generated shares:")

      for i, share in enumerate(shares, 1):
        print(f"share {i}: {share}")

      broadcast_shares(shares, broadcast_IP, broadcast_port)

      time.sleep(t)
  
  except KeyboardInterrupt:
    print("\n client stop")


if __name__ == "__main__":
  main()