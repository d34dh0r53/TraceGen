TraceGen
========

Generate Openstackish Logs

This generates multiline python like traceback messages ala OpenStack services.  A UUID is generated for easy searching in the logs and this UUID is printed to STDERR for reference.

````bash
tracegen.py --help
Usage: tracegen.py [OPTIONS]

Options:
  --outfile TEXT    Name of output file for multiline trace output
  --count INTEGER   Number of indented lines
  --datestamp TEXT  Datestamp
  --pid INTEGER     Pid of logging process
  --level TEXT      Logging level
  --logsource TEXT  Name of the process doing the logging
  --message TEXT    Message to inject on first line of multiline
  --help            Show this message and exit.
  ````

## Example Output

````bash
tracegen.py
2014-08-13 15:49:48.923810 65535 TRACE tracegen Traceback (most recent call last): TESTING TRACE 840ee47f-8ed6-469c-b0ad-634a561e1a3c
2014-08-13 15:49:48.923810 65535 TRACE tracegen   Line 0 - 840ee47f-8ed6-469c-b0ad-634a561e1a3c
2014-08-13 15:49:48.923810 65535 TRACE tracegen
840ee47f-8ed6-469c-b0ad-634a561e1a3c
````
