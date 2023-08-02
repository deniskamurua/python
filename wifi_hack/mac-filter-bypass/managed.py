import subprocess
import time

new_mac = input("Enter mac addr:")

subprocess.run(['ifconfig', 'wlan0', 'down'])

subprocess.run(['macchanger', '-m', new_mac, 'wlan0' ])

subprocess.run(['ifconfig', 'wlan0', 'up'])
