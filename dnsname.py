##
## A simple method to return DNS from IP address
##
import socket

def dnsName(ipaddress):
    addresslist=socket.gethostbyaddr(ipaddress)
    return addresslist[0]

print("DNS Name: ", dnsName('8.8.8.8'))
print("DNS Name: ", dnsName('212.77.98.9'))



