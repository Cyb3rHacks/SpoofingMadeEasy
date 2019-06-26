# SpoofingMadeEasy V.1.0

SpoofingMadeEasy is a simple python script that allows begining users to DNS spoof with ease. SpoofingMadeEasy utilizes the DNS module that comes with MITMF (I do NOT take credit for MITMF). This tool is very simple and easy to use as it will ask the user to imput the IP addresses and then conifure the DNS module accordingly. It can store this information for future attacks to make things easier. This script will also carry out the attack for you. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

Follow the simple instrutions below to get everything up and running on your local computer.

1. Downloadning the repository:

```
$ git clone https://github.com/Cyb3rHacks/SpoofingMadeEasy.git
```

2. cd Into the direcotory where you cloned the files. For example:

```
$ cd /root/SpoofingMadeEasy
```

3. Run the script:
```
$ python SpoofingMadeEasy.py
```

You should now be on the homepage for the script:
```
   _______     ______ ____  _____   _    _          _____ _  __ _____   
  / ____\ \   / /  _ \___ \|  __ \ | |  | |   /\   / ____| |/ // ____|  
| |     \ \_/ /| |_) |__) | |__) | | |__| |  /  \ | |    | ' /| (___    
| |      \   / |  _ <|__ <|  _  /  |  __  | / /\ \| |    |  <  \___ \   
| |____   | |  | |_) |__) | | \ \  | |  | |/ ____ \ |____| . \ ____) |  
 \_____|  |_|  |____/____/|_|  \_\ |_|  |_/_/    \_\_____|_|\_\_____/   

#~ Cybersecurity Penetration Testing/Ethical Hacking                    
#~ SpoofingMadeEasy V.1.0
#~ Contact: Please contact me if you find any bugs!
#~ GitHub: https://github.com/Cyb3rHacks

NOTE: I am not taking credit for MITMF - this is NOT my tool. I am only making it easier for people starting with MIMTF.


1 #> Install MITMF                 #Install Man In The Middle Framework
2 #> Change DNS records            #Change websites that the target will be redirected to
3 #> Target Information            #Save/Change Gateway IP and Target IP for future attacks
4 #> Start Spoofing Attack         #Start Spoofing Attack
5 #> Exit                          #Exit script - back to terminal


Please select an option [1-5]:


```

## USAGE

Below are some simple examples of what the script is capable of. Please use them as a guild, however, you will easily be able to successfully launch attacks as it is meant for beginners.

### Downlaoding MITMF module

Before you try and launch an attack, you will need to download the MITMF module so select option 1:

```
1 #> Install MITMF                 #Install Man In The Middle Framework
```

### Changing the DNS records - redirecting domains and IP addresses

This option will allow you to edit the mitmf.conf file and change the IP addresses and domains you wish to DNS spoof:

1. Select Option 2
```
2 #> Change DNS records            #Change websites that the target will be redirected to
```

2. Confirm that you wish to change the file.

3. Next, you will need to scroll down to the section where you are able to add your custom domains. It should look like this:

```

         nameservers = 8.8.8.8

         [[[A]]]     # Queries for IPv4 address records
         *.thesprawl.org= xxx.xxx.x.xxx
         *.live.com= xxx.xxx.x.xxx
         *.*.com= xxx.xxx.x.xxx


```
Change the domains and the IP addresses marked "X".
the * is called a wildcard. This mean that any sub domain that live.com has, it will also be redirected. 

*.*.* will redirect any website the target is travelling to

4. Now press ctrl-s to save and then ctrl-x to close

### Target Information

This option will allow you to add/save a Target for future attacks
```
3 #> Target Information            #Save/Change Gateway IP and Target IP for future attacks
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc




  
