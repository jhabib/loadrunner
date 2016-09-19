import numpy
import psutil
from optparse import OptionParser


def eat_memory(chunk_size=256):
    result = []
    while psutil.virtual_memory().free > 1024*1024*chunk_size:
        try:
            result = result + [numpy.random.bytes(1024*1024) for x in xrange(chunk_size)]
        except MemoryError as me:
            pass
        print 'mem used: ' + str(psutil.virtual_memory().used)
        print 'mem_available: ' + str(psutil.virtual_memory().available)

if __name__ == '__main__':

    p = OptionParser(usage="usage: %prog [options] chunk_size", version="%prog 1.0")
    p.add_option('-c', '--chunk',
                 dest='chunk',
                 default=256,
                 type='int')

    opts, rem = p.parse_args()

    while True:
        eat_memory(opts.chunk)
