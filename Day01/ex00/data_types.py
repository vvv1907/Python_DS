#!/usr/local/bin/python3

def data_types():

    a = 1
    b = 'a'
    c = 1.2
    d = True
    e = [1, 2]
    f = {'one': 1, 'two': 2}
    g = (1, 'a', True)
    h = {1, 2, 3}

    print('[%s, %s, %s, %s, %s, %s, %s, %s]'
          % (
              type(a).__name__,
              type(b).__name__,
              type(c).__name__,
              type(d).__name__,
              type(e).__name__,
              type(f).__name__,
              type(g).__name__,
              type(h).__name__
            )
          )

if __name__ == '__main__':
    data_types()
