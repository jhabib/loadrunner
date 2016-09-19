import psutil
import logging
import logging.handlers
import time
import datetime
from optparse import OptionParser


def create_log_files(output_file, size, count, interval):
    logger = logging.getLogger('LoadLogger')
    logger.setLevel(logging.INFO)

    handler = logging.handlers.RotatingFileHandler(
        output_file, maxBytes=size, backupCount=count)

    logger.addHandler(handler)

    while True:
        log_string = "\n".join(['\n\n'+str(datetime.datetime.utcnow()),
                                 'cpu: '+str(psutil.cpu_percent(interval=1, percpu=True)),
                                 'mem: '+str(psutil.virtual_memory()),
                                 'disk: '+str(psutil.disk_io_counters(perdisk=True)),
                                 'net: '+str(psutil.net_io_counters())])
        logger.info(log_string)
        print log_string
        time.sleep(interval)

if __name__ == '__main__':

    p = OptionParser(usage="usage: %prog [options] file_path file_size file_count", version="%prog 1.0")
    p.add_option('-o', '--output',
                 dest='output_filepath',
                 default='load_log.txt')

    p.add_option('-s', '--size',
                 dest='size',
                 default=8192,
                 type='int')

    p.add_option('-c', '--count',
                 dest='count',
                 default=100,
                 type='int')

    p.add_option('-i', '--interval',
                 dest='interval',
                 default=0.5,
                 type='float')

    opts, rem = p.parse_args()

    create_log_files(opts.output_filepath, opts.size, opts.count, opts.interval)

