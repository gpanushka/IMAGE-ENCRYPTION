from PIL import Image

def encrypt_decrypt(image_path, key, mode):
  """Encrypts or decrypts an image using XOR operation with a key."""
  image = Image.open(image_path)
  pixels = image.load()
  width, height = image.size

  for y in range(height):
    for x in range(width):
      pixel = pixels[x, y]
      new_pixel = tuple(map(lambda a, b: a ^ b, pixel, key))  # XOR each channel with key
      pixels[x, y] = new_pixel

  new_name = f"{mode}_{image_path}"  # Add prefix based on mode
  image.save(new_name)
  #print(f"Image {mode}d successfully!")
  if mode == 'e':
    print("Image is encrypted successfully.")
  elif mode == 'd':
    print("Image is decrypted successfully.")

def main():
  while True:
    mode = input("Enter 'e' to encrypt or 'd' to decrypt: ")
    if mode.lower() in ('e', 'd'):
      break
    else:
      print("Invalid input. Please enter 'e' or 'd'.")

  image_path = input("Enter the image path: ")
  key = int(input("Enter the key (integer between 0-255): "))
  key = bytes([key] * 3)  # Repeat key for all channels

  encrypt_decrypt(image_path, key, mode.lower())

if __name__ == "__main__":
  main()
