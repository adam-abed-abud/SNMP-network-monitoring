## SNMP Network monitoring

### Real time SNMP monitoring application. This project was first introduced at the International School of Trigger and Data Acquisition (ISOTDAQ).

 - Author: **Adam Abed Abud**
 - Last update: May, 2019

Adapted from: https://github.com/tdiethe/flask-live-charts

**Backend:** Python & flask
**Frontend:** Javascript Highcharts 


# Usage
Before starting the web application you will need netsnmp and flask installed on your machine.

```sh
cd SNMP_network_monitoring
python snmp_monitoring.py
```
This will start the server. It will keep quering the SNMP server for the number of bytes going IN/OUT of the switch. By default the server address is 192.168.0.10. To change the IP of the switch:


```sh
python  snmp_monitoring.py --server_address SWITCH_IP_ADDRESS
```

Start the web application. 

```sh
python app.py
```

Start firefox with the following address:
```sh
firefox 127.0.0.1:5000
```

Enjoy!

License
----

For the benefit of everyone.


**Free Software!**

