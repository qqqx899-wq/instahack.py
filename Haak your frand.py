#!/usr/bin/env python3
import time
import random
import sys
import string
import os

# إعداد ألوان الطرفية
G = '\033[92m'  # أخضر
R = '\033[91m'  # أحمر
W = '\033[0m'   # أبيض
Y = '\033[93m'  # أصفر
C = '\033[96m'  # سماوي للعلامة المائية

def print_slow(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# شعار الأداة الوهمية مع العلامة المائية Q4RStudio
banner = f"""{G}
  ___ _   _ ____ _____  _       _   _    _    ____ _  __
 |_ _| \ | / ___|_   _|/ \     | | | |  / \  / ___| |/ /
  | ||  \| \___ \ | | / _ \    | |_| | / _ \| |   | ' / 
  | || |\  |___) || |/ ___ \ _ |  _  |/ ___ \ |___| . \ 
 |___|_| \_|____/ |_/_/   \_(_)|_| |_/_/   \_\____|_|\_\
                                                            
      [ v3.2.0 ] - Professional Brute-Force Tool
{C}         >>> Developed & Powered by Q4RStudio <<<{W}
"""

print(banner)

print_slow(G + "[*] Initializing Q4RStudio system components..." + W, 0.02)
time.sleep(0.3)
print_slow(G + "[*] Establishing secure Tor connection..." + W, 0.02)
time.sleep(0.5)

target = input(G + "Enter Target Username: " + W)
try:
    threads = int(input(G + "Enter Number of Threads (e.g. 50, 100): " + W))
except ValueError:
    threads = 100

wordlist_path = input(G + "Enter Wordlist Path (Leave empty for default/random): " + W)

use_random = True
custom_passwords = []

if wordlist_path.strip() != "":
    try:
        with open(wordlist_path.strip(), 'r', encoding='utf-8') as f:
            custom_passwords = [line.strip() for line in f if line.strip()]
        
        if custom_passwords:
            use_random = False
            print_slow(G + f"[*] Custom wordlist loaded successfully! ({len(custom_passwords)} passwords found)" + W)
        else:
            print_slow(Y + "[!] Wordlist is empty. Falling back to default random generation." + W)
    except FileNotFoundError:
        print_slow(R + f"[!] Error: File '{wordlist_path}' not found. Falling back to default random generation." + W)
else:
    print_slow(Y + "[*] No wordlist provided. Using default random generation algorithm." + W)

sys.stdout.write(G + "\n[*] Loading Attack Module: [")
for i in range(25):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.05)
print("] 100% Loaded" + W)
print("-" * 50)

print_slow(R + f"\n[!] WARNING: Starting Hydra Brute-force Attack on '{target}' using {threads} threads..." + W, 0.04)
time.sleep(1)
print_slow(G + "[*] Attack starting in 3... 2... 1...\n" + W, 0.1)

count = 1
pass_index = 0

try:
    while True:
        if use_random:
            current_pass = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(6, 12)))
        else:
            current_pass = custom_passwords[pass_index % len(custom_passwords)]
            pass_index += 1

        thread_id = random.randint(1, threads)
        
        print(f"{G}[Thread-{thread_id}] {W}Attacking: {G}{target}{W} | Attempt: {R}{count}{W} | Pass: {current_pass} {W}--> {R}FAILED{W}")
        
        time.sleep(0.03) 
        count += 1
        
except KeyboardInterrupt:
    print_slow(R + "\n\n[!] Attack Aborted by User. Connection Closed." + W)