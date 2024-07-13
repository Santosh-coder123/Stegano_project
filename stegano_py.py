import cv2
import string
import os

d = {}
c = {}

# Initialize the dictionaries for character to ASCII and vice versa
for i in range(256):
    d[chr(i)] = i
    c[i] = chr(i)

# Read the image
x = cv2.imread(r"C:\Users\santosh\OneDrive\Desktop\New folder\Originalgroot_img.jpg")

# Get the shape of the image
i = x.shape[0]
j = x.shape[1]
print(i, j)

# Input the key and text
key = input("Enter your password/pin(security key): ")
text = input("Enter text to hide: ")

kl = 0
tln = len(text)
z = 0  # decides plane
n = 0  # number of row
m = 0  # number of column

l = len(text)

for i in range(l):
    x[n, m, z] = d[text[i]] ^ d[key[kl]]
    m = (m + 1) % j  # move to the next column
    if m == 0:  # if we have moved past the last column, move to the next row
        n = (n + 1) % i
    z = (z + 1) % 3  # cycle through color planes
    kl = (kl + 1) % len(key)

# Save the encrypted image
cv2.imwrite("encryptedgroot_img.jpg", x)
os.startfile("encryptedgroot_img.jpg")
print("Your data is hiding process is completed successfully.")


#For decrypting the hidden data/text use below process
# Decryption process
ch = int(input("\nEnter 100 to extract data from Image: "))

if ch == 100 :
    key1 = input("\n\nRe-enter key to extract text: ")
    decrypt = ""

    if key == key1:
        n = 0  # reset row
        m = 0  # reset column
        z = 0  # reset plane
        kl = 0  # reset key index

        for i in range(l):
            decrypt += c[x[n, m, z] ^ d[key[kl]]]
            m = (m + 1) % j
            if m == 0:
                n = (n + 1) % i
            z = (z + 1) % 3
            kl = (kl + 1) % len(key)
        print("Encrypted text/data was: ", decrypt)
        print("Thank you for using stegano")
        print(" EXITING ")
    else:
        print("Key doesn't match. plz enter the correct key")
    
