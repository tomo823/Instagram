import requests
import socket


def get_local_addr():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def get_gip_addr():
    res = requests.get('http://checkip.dyndns.com/')
    return res.text

if __name__ == '__main__':
    #print('your globalip: ' + get_gip_addr())
    print('your localip: ' + get_local_addr())