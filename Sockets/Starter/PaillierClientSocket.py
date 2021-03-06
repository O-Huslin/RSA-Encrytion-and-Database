# Client to implement simplified 'secure' electronic voting algorithm
# and send votes to a server

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
                    return expMod((b*b)%m, n/2, m)
                else:
                    return(b*expMod(b,n-1,m))%m
	
class PaillierClientSocket:

        

        
        
        def __init__(self, host, port):
                '''Initialise the host name and port to be used'''
                
                self.host = host
                self.port = port
                print(host, port, "\n")

                votes = [0,0]
                
                clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                clientSocket.connect((host, port))

                msg1 = "100 Hello"
                clientSocket.send(msg1.encode())
                msg2 = clientSocket.recv(1024) #receives the key message 
                print(msg2)
                m = clientSocket.recv(1024).decode() #recieves the candidate names
                msg =  "The candidates voting information are: " + m
                m = m.split()
                print(msg)
                clientSocket.send(msg.encode())
                newMsg = clientSocket.recv(1024) #receives the list of candidates  
                print('The candidates are: ', newMsg.decode())
                mg = clientSocket.recv(1024) # receives the 106 message of candidates 
                print(mg.decode())
                #pmsg = clientSocket.recv(1024).decode() #receives polls open message
                #print(psmg)
                
                sen = str(input("Please type the name of the candidate you wish to vote for: "))
                print(sen)
                print(self.vote(sen, m, votes))
                sen = sen.upper()
                sen = str(sen)
                print(sen + " 2")
                if self.vote(sen, m, votes) == "Incorrect candidate name entered.":
                        print(self.vote(sen, m, votes))
                        print('Please try again')
                        sen_2 = input("Please type the name of the candidate you wish to vote for: ")
                        print(self.vote(sen_2, m, votes))
                else:
                        print("Please restart and try again.")
                print(votes)
                        
                clientSocket.close()

     
        def ProcessMsgs(self):
                """Main event processing method"""
                pass


        def mysend(self, msg):
                """Accepts message into the socket"""
                clientSocket.send(msg)
                
    
        def myreceive(self):
                """Add code here to read data from the socket"""
                newSen = clientSocket.recv(1024)

        def vote(self, w, l_names, v_lst):
                self.w = w
                self.l_names = l_names
                self.v_lst = v_lst

                l_names += [1]
                
                if w == l_names[0]:
                        v_lst[0] += 1
                        agn = input('Type Y is you would like to vote again or N if not.')
                        if agn == 'Y' or 'y':
                                v_again = input('Please type the name of the candidate:')
                                vote(v_again, l_names, v_lst)
                        else:
                                return 'Thank you for voting'
                elif w == l_names[1]:
                        v_lst[1] += 1
                        agn_2 = input('Type Y is you would like to vote again or N if not.')
                        if agn_2 == 'Y' or 'y':
                                v_again2 = input('Please type the name of the candidate:')
                                vote(v_again2, l_names, v_lst)
                        else:
                                return 'Thank you for voting'
                elif w != l_names[0] or l_names[1]:
                        return "Incorrect candidate name entered."
                
                        

'''
This will be run if you run this script from the command line. You should not
change any of this; the grader may rely on the behavior here to test your
submission.
'''
if __name__ == "__main__":
        args = sys.argv
        if len(args) != 3:
                print ("Please supply a server address and port.")
 #               sys.exit()
        serverHost = str(args[1])       # The remote host
        serverPort = int(args[2])       # The same port as used by the server
        print(serverHost, serverPort)
    
        print("Client of Orley M. Huslin")
        c = PaillierClientSocket( serverHost, serverPort)
        c.close()
