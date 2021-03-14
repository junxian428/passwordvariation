import itertools
numbers = "0179"
code = itertools.permutations(numbers, 4)
count = 0
for eachpermutation in code:
    print(*eachpermutation)
    count += 1
print(f"[+] Number of variations: {count}")
