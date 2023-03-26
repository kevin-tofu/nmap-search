import nmap
import time
import requests

nm = nmap.PortScanner()
nm.scan('100.64.1.1/24', arguments='-sn')

for host in nm.all_hosts():
    res = requests.get('http://{host}')
    print(host, host.text)
    time.sleep(1)
