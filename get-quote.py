import sys

def primary():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  for quote in quotes:
  	sys.stdout.write(quote)
  sys.stdout.flush()

if __name__== "__main__":
  primary()
