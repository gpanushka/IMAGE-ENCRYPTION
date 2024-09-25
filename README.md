I developed a simple image encryption and decryption tool using pixel manipulation.

I have used resources like Visual Studio Code as the text editor and used internet resources for debugging.
This task is executed using the following steps:

**1. Libraries:** <br/> We only import PIL for image processing. <br/> Pillow is a friendly fork of PIL, the Python Imaging Library, that adds image processing capabilities to your Python interpreter. It supports many file formats, efficient data representation, and powerful image operations. 
![image](https://github.com/gpanushka/PRODIGY_CS_02/assets/167328539/8f0957f6-238c-46e0-be00-79db8f8fd8ff)


**2. Encryption/Decryption Function:** <br/> The code simplifies things by combining encryption and decryption. It takes the image path, a key (integer), and a mode ('e' or 'd'). It opens the image and loops through each pixel. A clever trick with *map* lets it perform XOR encryption/decryption on all color channels (red, green, blue) at once. The modified pixel values are used to update the image data. A new filename is created with a prefix based on the mode (encrypted or decrypted). Finally, the image is saved and a success message is printed, all within a single function.
![image](https://github.com/gpanushka/PRODIGY_CS_02/assets/167328539/edebccd7-1e9a-4bc4-949f-ce4d73165e2c)


**3. Main Function:** <br/> The funcyion starts by prompting the user to choose between encryption ('e') or decryption ('d'). It then asks for the image path. If encrypting, a random key is generated and printed for safekeeping during decryption. This key is then used by the _encrypt_image_ function to modify the image data. For decryption, the user is prompted to enter the key again, but this time in hexadecimal format (the format the key was printed in during encryption). This key is then passed to the _decrypt_image_ function to reverse the encryption and restore the original image.
![image](https://github.com/gpanushka/PRODIGY_CS_02/assets/167328539/debd56e6-aafd-44d5-8d2d-211de551bb03)


<h3>OUTPUT:</h3>

**Input from user:**

![image](https://github.com/gpanushka/PRODIGY_CS_02/assets/167328539/7ccad18a-9d6f-4640-8f53-42c447049110)


**Input image:**

![input2](https://github.com/gpanushka/PRODIGY_CS_02/assets/167328539/cef819aa-95c6-4cf2-b241-0d6292150f92)


**Image after encryption:**

![e_input2](https://github.com/gpanushka/PRODIGY_CS_02/assets/167328539/c88bf9ac-b2ea-4969-a616-5366ddd7e2c3)


Same image after decryption would give such image as output:

![d_input2](https://github.com/gpanushka/PRODIGY_CS_02/assets/167328539/110988e3-b7f4-42f5-8343-eb172e3188b1)

Let's take another image as an example to observe the working of this code:

![image](https://github.com/gpanushka/PRODIGY_CS_02/assets/167328539/aa6b3e64-6386-43b3-9c11-00982dfa0bb4)

The original image looks like this:

![fruits](https://github.com/gpanushka/PRODIGY_CS_02/assets/167328539/5d96f277-93f5-4131-9bee-fd3c2c7e6430)

After encryption, the image would look like this:

![e_fruits](https://github.com/gpanushka/PRODIGY_CS_02/assets/167328539/f52f687f-a04c-4635-9f34-68b7004e500e)


After decryption, the image would look like this:

![d_fruits](https://github.com/gpanushka/PRODIGY_CS_02/assets/167328539/34e0bfd9-40cc-4686-a39b-c39506c51729)



