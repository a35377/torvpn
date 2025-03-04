
# Auto TOR IP Changer

This script automates the process of setting up and using Tor to anonymize your traffic. The assigned IP from Tor will remain unchanged, providing consistent anonymity.

## Features
- Automatically installs required dependencies like `requests` and Tor.
- Starts the Tor service and uses the Tor SOCKS5 proxy.
- Displays the assigned IP address (remains unchanged unless you manually reload or restart the Tor service).

## How to Use

### 1. Switch to Superuser (sudo)
```bash
sudo su
```
### 2. Clone the Repository

```bash
git clone https://github.com/3222h/vpn.git
```
### 3. Change Directory to the Cloned Repository
```bash
cd vpn
```
### 4. Give permission
```bash
chmod +x install.py
```
### 5. Install the Script
```bash
python3 install.py
  ```
### 6. Run the Script
```bash
aut
```
### 7. Ip
```bash
127.0.0.1
```
### 8. Port
```bash
9050
```
### 9. Launch chrome
```bash
google-chrome --proxy-server="socks5://127.0.0.1:9050"
```
### 10. Remove repo
```bash
rm -rf vpn
```
