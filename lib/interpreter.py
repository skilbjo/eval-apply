#!/usr/bin/env python3
import argparse
import parse
import eval

def extract(file):
  data = ''
  with open(file,'r') as f:
    for line in f:
      data+=line
  return data

def main(file):
  data = extract(file)
  data = parse.parse(data)
  data = eval.eval(data)
  print(data)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Lisp interpreter')
  parser.add_argument('-f','--file', help='File to interpret')

  args = parser.parse_args()

  main(args.file)
