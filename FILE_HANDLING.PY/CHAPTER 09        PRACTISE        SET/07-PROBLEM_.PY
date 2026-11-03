with open("log.txt") as f:
    lines=f.readlines()

lineno1=1

for line in lines :
    if ("python in line"):
        print(f"yes python is present in . line no :{lineno1}")
        break
    lineno1=+1

else:
    print("no python is present")















