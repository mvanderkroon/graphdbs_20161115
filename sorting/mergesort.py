def mergeSort(alist):

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

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
  mergeSort(lst)
  ets = datetime.datetime.now()
  if args.verbose:
    print(lst)
  print(ets-sts)
