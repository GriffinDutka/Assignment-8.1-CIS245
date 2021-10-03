"""
Griffin Dutka
9/29/21
Assignment 8.1
"""
#Use OS Nodule
import os 

#Request filename and directory
def prompt():
    filename = input("Please enter the name of the file to be saved:")
    dir = input("Please enter the directory you would like to save to:")
    #Request information from user
    name = input("Please enter your name:")
    address = input("Please enter your home address:")
    number = input("Please enter your phone number:")

#check to see if the directory already exists
    if os.path.isdir(dir):
        #Write to file 
        writedata = open(os.path.join(dir,filename),"w")
        #Separate collected data by commas
        writedata.write(name +", "+ address +", "+ number +"\n")
        writedata.close()
        #Print file contents for validation
        print("-----------------------------------")
        print("Validation of the file contents:\n")
        filecontent = open(os.path.join(dir,filename),"r")
        for line in filecontent:
            print(line)
        filecontent.close()
    #If directory doesn't exist, print error
    else:
        print("That directory does not exist! Try again!")

prompt()