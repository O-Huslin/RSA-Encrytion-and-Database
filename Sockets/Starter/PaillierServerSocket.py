# Server to implement simplified 'secure' electronic voting algorithm
# and tally votes from a client.

# Author: 
# Last modified: 2020-10-07
# Version: 0.1.1
#!/usr/bin/python3

import socket
import random
import math
import sys

class NumTheory:
    @staticmethod
    def expMod(b,n,m):
        """Computes the modular exponent of a number"""
        """returns (b^n mod m)"""
        if n==0:
            return 1
        elif n%2==0:
            return NumTheory.expMod((b*b)%m, n/2, m)
        else:
            return(b*NumTheory.expMod(b,n-1,m))%m
    
    @staticmethod
    def gcd_iter(u, v):
        """Iterative Euclidean algorithm to find the greatest common divisor of
           integers u and v"""
        while v:
            u, v = v, u % v
        return abs(u)
    
    @staticmethod
    def lcm(u, v):
        """Returns the lowest common multiple of two integers, u and v"""
        return int((u*v)/NumTheory.gcd_iter(u, v))
    
    @staticmethod
    def ext_Euclid(m,n):
        """Extended Euclidean algorithm. It returns the multiplicative
            inverse of n mod m"""
        a = (1,0,m)
        b = (0,1,n)
        while True:
            if b[2] == 0: return a[2]
            if b[2] == 1: return int(b[1] + (m if b[1] < 0 else 0))
            q = math.floor(a[2]/float(b[2]))
            t = (a[0] - (q * b[0]), a[1] - (q*b[1]), a[2] - (q*b[2]))
            a = b
            b = t
    
    @staticmethod
    def L(x, n):
        """Function needed for unscrambling data """
        return math.floor((x-1)/n)


class PaillierServerSocket:
    
    def __init__(self, host, port):
        
        self.host = host
        self.port = port
        
        servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr = (host, port)
        print(addr)     #test address
        
        servSock.bind(('',port))
        hostname = socket.gethostname()
        print('Server is listening on IP:', hostname, 'on Port:', port)
        
        servSock.listen(1)
        candidates = []
        
        while True:
            conSock, address = servSock.accept()
            print("Connection has been established" + "\n")
            msg = conSock.recv(1024).decode() #receives the connection confirmation message
            
            if msg == "100 Hello":
                print(len(msg))
                print("Connection message has been confirmed" + "\n")
                key1, key2 = str(n), str(gen)
                keys = "105 Key n: " + key1 + ", " + "g: " + key2
                conSock.send(keys.encode()) #sends the key message
                
                cans = str(input("Please type the first names of the candidates separated by commas: "))
                cans = cans.upper()
                print(cans)

                #test the mysend method
                conSock.send(cans.encode()) #sends the names of the candidates 
                names = cans.strip()
                print(names)
                
                c1 = {"ID: 256", "Candidate: " + names[0]}
                c2 = {"ID: 65536", "Candidate: " + names[1]}
                candidates += c1, c2
                #msg3 = {c1[0] + "Candidate: " + c1[0] + "}"{c2[0] + "Candidate: " + c2[1]
                print(candidates)
                
                msg3 = "106 [" + str(candidates[0]) + ", " + str(candidates[1]) + "]"
                conSock.send(msg3.encode())
                print(msg3)
                
                #msg4 = "107 Polls Open"
                #conSock.send(msg4.encode())
                #print("Polls message sent")

                #win = conSock.recv(1024).decode()
                #print(win)
                
            else:
                print("Incorrect connection message has been entered. \nConnection has been terminated.")
            conSock.close
      
        
    def ProcessMsgs(self):
        """Main event processing method"""
        
        pass

    def connect(self, host, port):
        # Add code to connect to a host and port
        self.connect(host, port)

    def mysend(self, msg):
        """Add code here to send message into the socket"""
        self.msg = msg
        msgSent = 0
        while msgSent < len(msg):
            sendRem = self.socket.send(msg[msgSent:])
            msgSent += sendRem

            
    def myreceive(self):
        """Add code here to read data from the socket"""
        print("The server is ready to receive")
        return serSock.recv(1024)
        
'''
This will be run if you run this script from the command line. You should not
change any of this; the grader may rely on the behavior here to test your
submission.
'''
if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print ("Please supply a server port.")
#        sys.exit()
    HOST = ''                # Symbolic name meaning all available interfaces
    PORT = int(args[1])     # The port on which the server is listening
    if PORT < 1023 or PORT > 65535:
        print("Invalid port specified.")
        sys.exit()
        
    p = int(input('Enter P : '))
    q = int(input('Enter Q: '))
    n = p*q
    euler = (p-1)*(q-1)
    lAmbda = NumTheory.lcm(p-1, q-1)
    if NumTheory.gcd_iter(n, euler) != 1:
        print(str(n) + " is not relatively prime to " + str(euler))
        sys.exit()
    gen = random.randint(1,n**2)
    L_fn_input = NumTheory.expMod(gen, lAmbda, n**2)
    mu = NumTheory.ext_Euclid(n,NumTheory.L(L_fn_input,n))
    print("Public key: (" + str(n) + "," + str(gen) +")")
    print("Private key: " + str(lAmbda))
    print("mu: " + str(mu))
    
    print("Server of Orley M. Huslin")
    s = PaillierServerSocket(HOST,PORT)
    s.close()
