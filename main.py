import sys

def main() -> int:
  count = 0
  dict = {}
  with open("books/frakenstein.txt") as f:
    for line in f:
      for word in line.split():
        count = count + 1
        for char in word:
          key = char.lower()
          if key.isalpha():
            if key in dict:
              dict[key] = dict[key] + 1
            else:
              dict[key] = 1
    
    print(f'{count} words found in document')
    for key in dict:
      print(f'The \'{key}\' character was found {dict[key]} times')

main()