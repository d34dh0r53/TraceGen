#!/usr/bin/env python

import click
import datetime
import uuid
import sys

@click.command()
@click.option('--file', default='stdout', help='Name of output file for multiline trace output')
@click.option('--count', default=1, help='Number of indented lines')
@click.option('--datestamp', default=datetime.datetime.now().isoformat(' '), help="Datestamp")
@click.option('--pid', default=65535, help='Pid of logging process')
@click.option('--level', default="TRACE", help='Logging level')
@click.option('--logsource', default='tracegen', help='Name of the process doing the logging')
@click.option('--message', default='TESTING TRACE', help='Message to inject on first line of multiline')
def do_logging(file, count, logsource, datestamp, level, message, pid):
    my_tag = str(uuid.uuid4())
    odd_spaces = '  '
    even_spaces = '    '

    print "{} {} {} {} Traceback (most recent call last): {} {}".format(datestamp, pid, level, logsource, message, my_tag)

    for i in xrange(count):
        line_head = "{} {} {} {}".format(datestamp, pid, level, logsource)
        line_message = "Line {} - {}".format(i, my_tag)
        if (i == 0):
            line_message = odd_spaces + line_message
        elif (i % 2 == 0):
            line_message = even_spaces + line_message
        else:
            line_message = odd_spaces + line_message
        print "{} {}".format(line_head, line_message)

    print "{} {} {} {}".format(datestamp, pid, level, logsource, message)
    sys.stderr.write(my_tag + '\n')

if __name__ == '__main__':
    do_logging()
