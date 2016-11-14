def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

import argparse, json, datetime

parser = argparse.ArgumentParser(description='Sort list of integers using Bubblesort')
parser.add_argument('--verbose', help='verbosity', action='store_true')
parser.add_argument('data', metavar='d', type=str,
                    help='path to datafile')

args = parser.parse_args()

with open(args.data, 'r') as file:
  lst = json.loads(file.read())
  if args.verbose:
    print(lst)
  sts = datetime.datetime.now()
  bubbleSort(lst)
  ets = datetime.datetime.now()
  if args.verbose:
    print(lst)

  print(ets-sts)

