import os
import time

option =  input ('What would you like to do:\n1) List directory \n2) Print curr>

#Lists the currect directory
if option == '1':
        print ('Option one selected')
        time.sleep(1)
        os.system('ls')

#Prints the working directory
if option == '2':
        print ('Option two selected')
        time.sleep(1)
        os.system('pwd')

#Creates a new directory with a name of your choice
if option == '3':
        print ('Option three selected')
        time.sleep(1)
        name1 = input('Please enter the name of the directory you would like to create:')
        os.system('mkdir ' + name1)

#Creates a new file with an extension of your choice
if option == '4':
        print ('Option four selected')
        time.sleep(1)
        filea = input('Please enter the name of the file you would like to create: ')

        fileb = input('File type: ')
        os.system('touch ' + filea + '.' + fileb)

#Displays the systems uptime
if option == '5':
        time.sleep(1)
        os.system('uptime')

#Exits script
if option == '6':
        print ('Exiting script')
        time.sleep(1)
        exit()

if option == '7':
#       os.system('sudo apt-get install sl')
        os.system('sl')

else:
        print ('Invalid option!')
        time.sleep(1)
        exit()


