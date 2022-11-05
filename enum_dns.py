#!/usr/bin/env python3
import os
import sys
import logging
try:
    import threading
except:
    sys.exit("Install missing library: pip install threaded")
try:
    import socket
except:
    sys.exit("Install missing library: pip install sockets")
try:
    import requests
except:
    sys.exit("Install missing library: pip install requests")

if len(sys.argv) !=4:
    print("follow the example: ")
    print("")
    print("%s google.com /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt /home/user/Documents/enum_dns.txt"%(sys.argv[0]))
    sys.exit()

LOG = sys.argv[3]
logging.basicConfig(level=logging.INFO, filename=LOG, format="%(message)s")

def dns(domain, wordlist):
    for nm in names:
        dns = nm.strip("\n") + "." + domain
        try:
            logging.info(dns + ": " + socket.gethostbyname(dns))
            print(dns + ": " + socket.gethostbyname(dns))
        except Exception as error:
            pass
        except KeyboardInterrupt:
            sys.exit()
        except socket.gaierror:
            pass

    try:
        while True:
            if _ in range(4):
                threading.Thread(target=dns).join.start()
            else:
                print("threading error")
                pass
        else:
            print("error")
    except KeyboardInterrupt:
        sys.exit()
    except Exception as error:
        pass

try:
    if __name__ == "__main__":
        domain = sys.argv[1]
        wordlist = sys.argv[2]
        with open(wordlist, "r") as archive:
            names = archive.readlines()
            dns(domain, wordlist)
except KeyboardInterrupt:
    sys.exit()
except Exception as error:
    pass

