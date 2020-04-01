name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    if not line.startswith('From '): continue
    words = line.split()
    address = words[1]
    counts[address] = counts.get(address, 0) + 1

maxaddress = None
maxcount = None

for adr,ccc in counts.items():
    if maxcount == None or maxcount < ccc:
        maxaddress = adr
        maxcount = ccc

print(maxaddress, maxcount)
