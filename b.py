import time
from datetime import datetime as dt
  
# change hosts path according to your OS
# this file is used to resolve a name into an address (that is, to translate a host name into its Internet address).
hosts_path = "/etc/hosts"
# localhost's IP
redirect = "127.0.0.1"
  
# websites That you want to block
website_list = ["www.facebook.com","facebook.com",
      "dub119.mail.live.com","www.dub119.mail.live.com",
      "www.gmail.com","gmail.com"]

  
while True:
  
    # time of your work
    #Compares the time. If the time is in between 8AM and 4PM, then it prints working hours otherwise it prints fun hours
    stop = ('do you want to stop:')
    if stop.lower() == 'yes':
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    # mapping hostnames to your localhost IP address
                    file.write(redirect + " " + website + "\n")

    elif stop.lower() == 'no':
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
  
            # removing hostnmes from host file
            file.truncate()
  
        print("Fun hours...")
    time.sleep(5)
    # break




        
    # else:
    #     with open(hosts_path, 'r+') as file:
    #         content=file.readlines()
    #         file.seek(0)
    #         for line in content:
    #             if not any(website in line for website in website_list):
    #                 file.write(line)
  
    #         # removing hostnmes from host file
    #         file.truncate()
  
    #     print("Fun hours...")
    # time.sleep(5)