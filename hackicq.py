import os, sys
print("""
                  _     _____  ___   ____
  /\  /\__ _  ___| | __ \_   \/ __\ /___ \
 / /_/ / _` |/ __| |/ /  / /\/ /   //  / /
/ __  / (_| | (__|   </\/ /_/ /___/ \_/ /
\/ /_/ \__,_|\___|_|\_\____/\____/\___,_\
                                          
Termux-Lab              vk.com/termux_lab
""")

print("Starting...")
ports = input("[PORT]: ")
if ports == "":
    ports=8080
os.system("php -S localhost:"+str(ports))
