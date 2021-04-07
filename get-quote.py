import random

def primary():
#  print("Keep it logically awesome.")
  f = open("python-lab\python-random-quote\quotes.txt")
  quotes = f.readlines()
  f.close()
  f = open("python-lab\python-random-quote\quotes.txt", "a")
  f.write("Now the file has more content!")
  f.close()
  last = len(quotes) - 1
  rnd = random.randint(0, last)
  print(quotes[rnd],quotes[rnd-1],end='')

if __name__== "__main__":
  primary()
