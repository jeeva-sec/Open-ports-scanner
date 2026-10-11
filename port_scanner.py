import socket

target = '127.0.0.1'

print(f"scanning {target}")

for ports in range(1,1000):

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.02)

    try :

        scan = s.connect_ex((target,ports))

        if scan == 0:

            print(f"port {ports}:OPEN")

    except OSError as erorr:

        print(f"port {ports}:CLOSED")

    finally :
              s.close()

print("scan complete")
