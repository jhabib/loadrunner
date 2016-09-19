import threading
import SocketServer
from optparse import OptionParser


class TcpHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024)
            cur_thread = threading.current_thread()
            response = '{}: {}'.format(cur_thread.name, data)
            self.request.sendall(data)
            print response
            print ''


class ThreadedTcpHandler(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == '__main__':
    p = OptionParser(usage="usage: %prog [options] -l local_host -p local_port", version="%prog 1.0")

    p.add_option('-l', '--local_host',
                 dest='local_host',
                 default='127.0.0.1')

    p.add_option('-p', '--port',
                 dest='local_port',
                 default=2727,
                 type='int')

    opts, rem = p.parse_args()

    server = ThreadedTcpHandler((opts.local_host, opts.local_port), TcpHandler)

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print 'server loop running in thread %s' % server_thread.name
    print 'server ip: %s server port: %s' % (opts.local_host, opts.local_port)
    server_thread.join()

