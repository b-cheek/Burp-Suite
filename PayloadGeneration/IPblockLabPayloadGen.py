# fUsernms = open("./burpUser.txt", "r")
fPasswds = open("./burpPass.txt", "r")
fPayload = open("./burpPayload.txt", "a")
fPayload.truncate(0)

# burpUsernms = fUsernms.read().split("\n")
burpPasswds = fPasswds.read().split("\n")


for i in range(0,100):
    fPayload.write("wiener" + "\n" +  "carlos" + "\n")

# for i in burpPasswds:
#     fPayload.write("peter" + "\n" + i + "\n")

# fUsernms.close()
fPasswds.close()
fPayload.close()