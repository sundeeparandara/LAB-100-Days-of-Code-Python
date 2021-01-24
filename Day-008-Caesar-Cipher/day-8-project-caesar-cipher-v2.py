alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,direction):
  output_text = ""
  if direction == "encode":
    for character in text:
      input_text_loc = alphabet.index(character)
      output_text_loc = (input_text_loc + shift) % len(alphabet)
      output_text += alphabet[output_text_loc]
    print(f"The encoded text is {output_text}")
  elif direction =="decode":
    for character in text:
      input_text_loc = alphabet.index(character)
      output_text_loc = (input_text_loc - shift)
      output_text += alphabet[output_text_loc]
    print(f"The decoded text is {output_text}")
  else:
    print("invalid direction")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
caesar(text=text,shift=shift,direction=direction)