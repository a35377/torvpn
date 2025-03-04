# -*- coding: utf-8 -*-
import time
import os
import subprocess

try:
    import requests
except Exception:
    print('[+] python3 requests is not installed')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 requests is installed')

try:
    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:
    print('[+] Tor is not installed!')
    subprocess.check_output('sudo apt update', shell=True)
    subprocess.check_output('sudo apt install tor -y', shell=True)
    print('[!] Tor is installed successfully')

# Ensure Tor uses only US exit nodes and binds to different ports with isolated circuits
torrc_config = '/etc/tor/torrc'
with open(torrc_config, 'a') as torrc:
    for port in range(9041, 9051):
        torrc.write(f'\nSocksPort 127.0.0.1:{port} IsolateClientAddr IsolateSocksAuth\nExitNodes {{us}}\nStrictNodes 1\n')

# Restart the Tor service to apply changes
os.system('service tor restart')
time.sleep(5)

# Function to renew the Tor circuit
def renew_tor_circuit():
    os.system('kill -HUP $(pidof tor)')
    time.sleep(5)

# Notify the user to change their SOCKS proxy settings
print("\033[1;32;40m Change your SOCKS to ports from 127.0.0.1:9041 to 127.0.0.1:9050 \n")

# Retrieve and display the current IP assigned by Tor (only US IPs on different ports)
def ma_ip(port):
    url = 'http://checkip.amazonaws.com'
    try:
        get_ip = requests.get(url, proxies=dict(http=f'socks5://127.0.0.1:{port}', https=f'socks5://127.0.0.1:{port}'), timeout=10)
        return get_ip.text.strip()
    except Exception as e:
        return f'Error on port {port}: {e}'

for port in range(9041, 9051):
    renew_tor_circuit()
    current_ip = ma_ip(port)
    print(f'[+] Your US IP on port {port} is: {current_ip}')
# No repeated IP changes; the Tor IP will remain active as long as the service runs.
