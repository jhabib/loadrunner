import socket
import time
import threading
import numpy
import random
from optparse import OptionParser


class TcpClient(threading.Thread):
    daemon = True

    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port

    def get_socket(self):
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conn(self, sock):
        sock.connect((self.host, self.port))

    def reconn(self, sock):
        sock.close()
        sock = self.get_socket()
        self.conn(sock)
        return sock

    def run(self):
        sock = self.get_socket()
        self.conn(sock)
        while True:
            m = str(numpy.random.rand(1024))
            time.sleep(random.randint(1, 3))
            try:
                sock.sendall(m)
                recv = sock.recv(1024)
                print '%s' % recv
                if not recv:
                    print 'reconnecting ... '
                    sock = self.reconn(sock)
                    time.sleep(5)
            except Exception as ex:
                print 'reconnecting ... '
                sock = self.reconn(sock)
                print str(ex)

if __name__ == '__main__':

    p = OptionParser(usage="usage: %prog [options] -c connections -r remote_host -p remote_port", version="%prog 1.0")

    p.add_option('-c', '--connections',
                 dest='conns',
                 default=300,
                 type='int')

    p.add_option('-r', '--remote_host',
                 dest='remote_host',
                 default='127.0.0.1')

    p.add_option('-p', '--port',
                 dest='remote_port',
                 default=2727,
                 type='int')

    opts, rem = p.parse_args()

    for i in xrange(opts.conns):
        tc = TcpClient(opts.remote_host, opts.remote_port)
        try:
            tc.start()
            time.sleep(0.1)
        except Exception as e:
            pass
    tc.join()
