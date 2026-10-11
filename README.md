# Python Port Scanner

A simple TCP port scanner built with Python's standard `socket` module. It scans ports 1-999 on a target host and prints the ones that are open.

## Features
- Scans ports 1-999 (the common "well-known" range)
- Uses `connect_ex()` with a short timeout (0.02 s) for fast scanning
- Prints each open port as it is found
- No external libraries required

## How it works
For each port, the script creates a TCP socket (`AF_INET`, `SOCK_STREAM`) and tries to connect to the target. If `connect_ex()` returns `0`, the connection succeeded and the port is reported as **OPEN**. Any other result means the port is closed or filtered, and nothing is printed. Each socket is closed after its check.

## Requirements
- Python 3.x

## Usage
1. Clone the repository:

       git clone https://github.com/<your-username>/<repo-name>.git
       cd <repo-name>

2. Run the scanner:

       python port_scanner.py

By default it scans `127.0.0.1` (your own machine). To scan another host, change this line in the script:

    target = '127.0.0.1'

## Example output

    scanning 127.0.0.1
    port 135:OPEN
    port 445:OPEN
    scan complete

## Common ports you may see
| Port | Service |
|------|---------|
| 22 | SSH |
| 80 | HTTP |
| 135 | MS RPC |
| 443 | HTTPS |
| 445 | SMB |

## Limitations
- The target is hardcoded in the script
- Ports are scanned one at a time (no multithreading)
- The 0.02 s timeout is tuned for localhost; slower or remote hosts may need a higher value
- TCP only (no UDP scanning)

## Future improvements
- Accept target IP and port range from user input
- Add multithreading for faster scans
- Detect service names and grab banners
- Save results to a file

## Disclaimer
This project is for **educational purposes only**. Only scan systems you own or have explicit permission to test. Unauthorized port scanning may be illegal.

## Author
Jeeva | B.Tech CSE (Cyber Security) | CompTIA Security+
