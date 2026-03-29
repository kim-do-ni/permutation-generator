import itertools
import os
import time

# Clear screen
os.system("clear")

# Banner
os.system("figlet PERMUTATION GENERATOR | lolcat")

print(">> Advanced Permutation Tool")
print(">> Developed by Just Doni")
print(">> Powered by ChatGPT\n")

# Input
data = input("[+] Enter numbers or text: ")
limit_input = input("[+] Limit (0 = all): ")

# Handle limit
if limit_input.lower() in ["0", "all"]:
    limit = 0
else:
    try:
        limit = int(limit_input)
    except:
        limit = 0

print("\n[!] Generating permutations...\n")
time.sleep(1)

results = itertools.permutations(data)

count = 0

for p in results:
    combination = ''.join(p)
    print(combination)
    
    count += 1
    time.sleep(0.01)
    
    if limit != 0 and count >= limit:
        print(f"\n[!] Stopped at {count}")
        break

print(f"\n[✓] Total generated: {count}")
print("[✓] Process completed.\n")
