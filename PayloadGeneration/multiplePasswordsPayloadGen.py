fPasswds = open("./burpPass.txt", "r")
fPayload = open("./burpPayload.txt", "a")
fPayload.truncate(0)

burpPasswds = fPasswds.read().split("\n")

for i in burpPasswds:
    print('"' + i + '",')

fPasswds.close()
fPayload.close()