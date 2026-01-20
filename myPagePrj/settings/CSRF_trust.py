import socket

def get_ipaddress():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    rtn = "http://" + ip_address
    return rtn