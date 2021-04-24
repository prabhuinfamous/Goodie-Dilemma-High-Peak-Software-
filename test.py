import sys
#output file
opfile = open("output.txt","w")
#input file
ipfile = open("given_input.txt","r")
content = ipfile.readlines()
a = {}
b = {}
employees = int(content[0].split(": ")[1])
goodies = content[4:]
prices = []
for item in goodies:
    if item[-2:] == "\n":
        item = item.split(": ")
        name,price = item[0],int(item[1][:-1])
    else:
        item = item.split(": ")
        name,price = item[0],int(item[1])
    prices.append(price)
    a[name] = price
sprices = sorted(prices)
diff = []
for i in range(len(prices)-employees):
    diff.append(sprices[i+employees-1] - sprices[i])
for i in a:
    b[a[i]] = i
ind = diff.index(min(diff))
out = ["The goodies are selected for distribution are:\n","\n"]
for i in sprices[ind:ind+employees]:
    out.append(b[i] + ": " + str(i) + "\n")
out.append("\n")
out.append("And the difference between the chosen goodie with highest price and the lowest price is " + str(min(diff)))
opfile.writelines(out)
opfile.close()
