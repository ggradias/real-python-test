#Leonardo de Pisa

import sys

def fib(n):
#return the nth fibonacci number
  n = int(n)
  if n <= 1:
    return 1

  return fib(n-1)+ fib(n-2)



if __name__ == '__main__':
    import pdb; pdb.set_trace()
    print(fib(sys.argv[-1]))

