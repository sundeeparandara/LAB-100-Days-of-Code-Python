import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,direction):
  
  output_text = ""
  if direction == "encode":
    for character in text:
      if character in alphabet:
        input_text_loc = alphabet.index(character)
        output_text_loc = (input_text_loc + shift) % len(alphabet)
        output_text += alphabet[output_text_loc]
      else:
        output_text += character
    print(f"The encoded text is: {output_text}")
  elif direction =="decode":
    for character in text:
      if character in alphabet:
        input_text_loc = alphabet.index(character)
        output_text_loc = (input_text_loc - shift)
        output_text += alphabet[output_text_loc]
      else:
        output_text += character
    print(f"The decoded text is: {output_text}")
  else:
    print("invalid direction")

print(art.logo)

launch_state = 'yes'

while launch_state == 'yes':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text=text,shift=shift,direction=direction)
  launch_state = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()