import sys

if len(sys.argv) != 3:
    print("error")
else:
    for i in range(int(sys.argv[2])):
        print(sys.argv[1])
    