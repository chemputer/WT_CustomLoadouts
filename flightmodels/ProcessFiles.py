#! /usr/bin/python3
import os

def main():
    with open("CustomLoadouts.txt", "w") as f:
        for filename in os.listdir(os.getcwd()):
            if filename.endswith(".blkx"):
                with open(filename, "r") as file:
                    if 'WeaponSlots' in file.read():
                        f.write("|" + filename[:-5] + "\n")
                        print(filename[:-5] + "\n")

if __name__ == "__main__":
    main()