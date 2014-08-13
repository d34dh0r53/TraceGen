TraceGen
========

Generate Openstackish Logs

This generates multiline python like traceback messages ala OpenStack services.

````
./tracegen.py --help
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
