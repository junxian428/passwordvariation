import itertools

numbers = input("[+] Choose numbers 0,9: ")
length_of_code = input("[+] Length of expected code: ")
code = itertools.permutations(numbers, int(length_of_code))
count = 0
for eachpermutation in code:
    print(*eachpermutation)
    count += 1
print(f"[+] Number of variations: {count}")
