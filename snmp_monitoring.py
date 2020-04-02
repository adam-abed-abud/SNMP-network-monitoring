# Python SNMP monitoring code for ISOTDAQ Networking Lab
# USAGE:  python snmp_monitoring.py
#
# Author: Adam Abed Abud
# Mail: adam.abed.abud@cern.ch
# Last update: May 14, 2019


#!/usr/bin/env python


import os
import time
import argparse
import netsnmp #snmp module for Python
import sqlite3
from datetime import datetime

timestamp = 'time' #name of time column
IN_1 = 'IN_port_1' # name of the column
OUT_1 = 'OUT_port_1' # name of the column
IN_3 = 'IN_port_3' # name of the column
OUT_3 = 'OUT_port_3' # name of the column
IN_13 = 'IN_port_13' # name of the column
OUT_13 = 'OUT_port_13' # name of the column
IN_15 = 'IN_port_15' # name of the column
OUT_15 = 'OUT_port_15' # name of the column

sqlite_file = 'database/switch_monitoringDB.sqlite'  # name of the sqlite database file
table_name = 'switch_monitor'  # name of the table to be created
field_type = 'INTEGER'  # results (in bytes) are integer values 


def parse_args():
    parser = argparse.ArgumentParser(description='Python script for network monitoring with snmp')

    parser.add_argument('--server_address', default='192.168.0.10') #10.193.254.2

    return parser.parse_args()


def difference(A,B):
   return int(A)-int(B)


def database_setup():
   '''
   This function creates the sqlite3 table with the timestamp column 
   and the columns for IN/OUT  from the four ports
   '''
   global IN_1  # name of the column
   global OUT_1 # name of the column
   global IN_3
   global OUT_3
   global IN_13
   global OUT_13
   global IN_15
   global OUT_15
   global sqlite_file 
   global table_name
   global timestamp
   global field_type

   # Connecting to the database file
   conn = sqlite3.connect(sqlite_file)
   c = conn.cursor()


   # Creating a new SQLite table with 1 column
   try:
      c.execute('CREATE TABLE IF NOT EXISTS {tn} ({time_column} {ft}, {nf} {ft}, {nf2} {ft}, {nf3} {ft}, {nf4} {ft}, {nf5} {ft}, {nf6} {ft}, {nf7} {ft}, {nf8} {ft})'\
        .format(tn=table_name, nf=IN_1, nf2=OUT_1, nf3=IN_3, nf4=OUT_3, nf5=IN_13, nf6=OUT_13, nf7=IN_15, nf8=OUT_15, time_column=timestamp, ft=field_type))
 
      # Committing changes and closing the connection to the database file
      conn.commit()
      conn.close()

   except sqlite3.OperationalError: 
      raise Exception("sqlite3 OperationalError. Check table creation syntax.")



def monitoring(server_address):
   '''
   Monitoring function on ports 01, 03, 13 and 15. The results are converted
   in rates (B/s) and stored in the sqlite3 table. 
   '''

   global IN_1 
   global OUT_1 
   global IN_3
   global OUT_3
   global IN_13
   global OUT_13
   global IN_15
   global OUT_15
   global sqlite_file 
   global table_name
   global timestamp
   global field_type

   serv = server_address

   system_description = netsnmp.Varbind('sysDescr.0')
   sysDescr = netsnmp.snmpget(system_description, Version = 1,  DestHost = serv,  Community='public') 

   print "=======================" 
   print "System description: \t", sysDescr[0]
   print "======================="

   # Incoming packets on ports 1, 3, 13, 15
   IfIn01 = netsnmp.Varbind('ifInOctets.1')
   IfIn03 = netsnmp.Varbind('ifInOctets.3')
   IfIn13 = netsnmp.Varbind('ifInOctets.13')
   IfIn15 = netsnmp.Varbind('ifInOctets.15')

   # Outgoing packets on ports 1, 3, 13, 15
   IfOut01 = netsnmp.Varbind('ifOutOctets.1')
   IfOut03 = netsnmp.Varbind('ifOutOctets.3')
   IfOut13 = netsnmp.Varbind('ifOutOctets.13')
   IfOut15 = netsnmp.Varbind('ifOutOctets.15')

 
   flag = 0
   while True:
       if flag == 0: #This condition makes sure that the first entry is zero. 
          IN_port_1_memory = netsnmp.snmpget(IfIn01, Version = 2,  DestHost = serv,  Community='public') 
          OUT_port_1_memory = netsnmp.snmpget(IfOut01, Version = 2,  DestHost = serv,  Community='public') 
          IN_port_3_memory = netsnmp.snmpget(IfIn03, Version = 2,  DestHost = serv,  Community='public') 
          OUT_port_3_memory = netsnmp.snmpget(IfOut03, Version = 2,  DestHost = serv,  Community='public') 
          IN_port_13_memory = netsnmp.snmpget(IfIn13, Version = 2,  DestHost = serv,  Community='public') 
          OUT_port_13_memory = netsnmp.snmpget(IfOut13, Version = 2,  DestHost = serv,  Community='public') 
          IN_port_15_memory = netsnmp.snmpget(IfIn15, Version = 2,  DestHost = serv,  Community='public') 
          OUT_port_15_memory = netsnmp.snmpget(IfOut15, Version = 2,  DestHost = serv,  Community='public') 

          conn = sqlite3.connect(sqlite_file)
          c = conn.cursor()
          c.execute("INSERT INTO {tn} ({time_column},{nf},{nf2},{nf3},{nf4},{nf5},{nf6},{nf7},{nf8}) VALUES(TIME('NOW'),{value},{value},{value},{value},{value},{value},{value},{value})"\
             .format(tn=table_name, nf=IN_1, nf2=OUT_1,  nf3=IN_3, nf4=OUT_3, nf5=IN_13, nf6=OUT_13, nf7=IN_15, nf8=OUT_15, time_column="time", value=0))

          conn.commit()
          flag = 1


       else:
          IN_port_1 = netsnmp.snmpget(IfIn01, Version = 2,  DestHost = serv,  Community='public') 
          OUT_port_1 = netsnmp.snmpget(IfOut01, Version = 2,  DestHost = serv,  Community='public') 
          IN_port_3 = netsnmp.snmpget(IfIn03, Version = 2,  DestHost = serv,  Community='public') 
          OUT_port_3 = netsnmp.snmpget(IfOut03, Version = 2,  DestHost = serv,  Community='public') 
          IN_port_13 = netsnmp.snmpget(IfIn13, Version = 2,  DestHost = serv,  Community='public') 
          OUT_port_13 = netsnmp.snmpget(IfOut13, Version = 2,  DestHost = serv,  Community='public') 
          IN_port_15 = netsnmp.snmpget(IfIn15, Version = 2,  DestHost = serv,  Community='public') 
          OUT_port_15 = netsnmp.snmpget(IfOut15, Version = 2,  DestHost = serv,  Community='public') 


          difference_IN_1 = difference(IN_port_1[0], IN_port_1_memory[0])
          difference_OUT_1 = difference(OUT_port_1[0], OUT_port_1_memory[0])
          difference_IN_3 = difference(IN_port_3[0], IN_port_3_memory[0])
          difference_OUT_3 = difference(OUT_port_3[0], OUT_port_3_memory[0])
          difference_IN_13 = difference(IN_port_13[0], IN_port_13_memory[0])
          difference_OUT_13 = difference(OUT_port_13[0], OUT_port_13_memory[0])
          difference_IN_15 = difference(IN_port_15[0], IN_port_15_memory[0])
          difference_OUT_15 = difference(OUT_port_15[0], OUT_port_15_memory[0])


          conn = sqlite3.connect(sqlite_file)
          c = conn.cursor()
          c.execute("INSERT INTO {tn} ({time_column},{nf},{nf2},{nf3},{nf4},{nf5},{nf6},{nf7},{nf8}) VALUES(TIME('NOW'), {IF01}, {OUT01}, {IF03}, {OUT03},{IF13}, {OUT13},{IF15}, {OUT15})"\
             .format(tn="switch_monitor", nf=IN_1, nf2=OUT_1, nf3=IN_3, nf4=OUT_3,nf5=IN_13, nf6=OUT_13, nf7=IN_15, nf8=OUT_15, time_column="time", IF01 = difference_IN_1 , OUT01 = difference_OUT_1, IF03 = difference_IN_3 , OUT03 = difference_OUT_3, IF13 = difference_IN_13 , OUT13 = difference_OUT_13, IF15 = difference_IN_15 , OUT15 = difference_OUT_15))

          conn.commit()

          IN_port_1_memory = IN_port_1
          OUT_port_1_memory = OUT_port_1
          IN_port_3_memory = IN_port_3
          OUT_port_3_memory = OUT_port_3
          IN_port_13_memory = IN_port_13
          OUT_port_13_memory = OUT_port_13
          IN_port_15_memory = IN_port_15
          OUT_port_15_memory = OUT_port_15
          print "Reading ports 1, 3, 13, 15 ----> OK \n", 

          time.sleep(1) #Get the rate in B/s

         


def main():
    args=parse_args()
    server_address = args.server_address #default server address 192.168.0.10
    database_setup()
    monitoring(server_address)



if __name__ == "__main__":
    main()













