#!/usr/bin/env python3
import os
import sys
import logging
try:
    import socket
except:
    sys.exit("Install missing library: pip install sockets")
try:
    import requests
except:
    sys.exit("Install missing library: pip install requests")

def helplk():
    print("follow the examples: ")
    print("")
    print("%s -h"%(sys.argv[0]))
    print("%s --help"%(sys.argv[0]))
    print("%s -u google.com -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt --save /home/user/Documents/enum_dns.txt"%(sys.argv[0]))
    sys.exit()

if len(sys.argv) <=1:
    helplk()
    sys.exit()
elif len(sys.argv) ==2:
    choice = str(sys.argv[1])
    if choice == "-u":
        print("insert valid url")
        sys.exit()
    elif choice == "--url":
        print("insert valid url")
        sys.exit()
    elif choice == "-h":
        helplk()
        sys.exit()
    elif choice == "--help":
        helplk()
        sys.exit()
    else:
        print("invalid option")
        print()
        helplk()
        sys.exit()
elif len(sys.argv) ==3:
    print("insert valid wordlist")
    print()
    helplk()
    sys.exit()
elif len(sys.argv) ==4:
    choice = str(sys.argv[3])
    if choice == "-w":
        print("insert valid wordlist")
        print()
        helplk()
        sys.exit()
    else:
        print("invalid option")
        print()
        helplk()
        sys.exit()
elif len(sys.argv) ==5:
    print("insert save-file")
    print()
    helplk()
    sys.exit()
elif len(sys.argv) ==6:
    choice = str(sys.argv[5])
    if choice == "--save":
        print("insert save-file")
        print()
        helplk()
        sys.exit()
    else:
        print("invalid option")
        print()
        helplk()
        sys.exit()
elif len(sys.argv) >=8:
    print("arguments error")
    print()
    helplk()
    sys.exit()
else:
    pass

LOG = sys.argv[6]
logging.basicConfig(level=logging.INFO, filename=LOG, format="%(message)s")

def dns(domain, wordlist):
    for nm in names:
        dns = nm.strip("\n") + "." + domain
        try:
            logging.info(dns + ": " + socket.gethostbyname(dns))
            print(dns + ": " + socket.gethostbyname(dns))
        except socket.gaierror:
            pass
        except Exception as error:
            pass
        except KeyboardInterrupt:
            sys.exit()

try:
    if __name__ == "__main__":
        domain = sys.argv[2]
        wordlist = sys.argv[4]
        with open(wordlist, "r") as archive:
            names = archive.readlines()
            dns(domain, wordlist)
except KeyboardInterrupt:
    sys.exit()
except Exception as error:
    pass
