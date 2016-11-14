import random
import argparse

def main():
  print([random.choice([i for i in range(1000)]) for r in range(args.integers)])

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Generate list of N random integers')
  parser.add_argument('integers', metavar='-n', type=int,
                      help='number of random integers to generate')

  args = parser.parse_args()
  main()
