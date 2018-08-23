# CDR-parser
Python script to collect AVAYA call log into a MS-SQL database

You can start it via python shell or convert it to a windows service.
In this version you'll need to add the listening port number and database parameters (username, password, database name, etc.) manually in the appropriate "constants" section of the script.
The AVAYA call manager needs also tuning. It should send CDR-s at the listened port.

In future I'll make something more comfortable.

Requirements
------------
collector:
MS machine
python 3 (tested on 3.6.5) on it
modules socket and pymssql

database:
any MS SQL database server with the right to write data
