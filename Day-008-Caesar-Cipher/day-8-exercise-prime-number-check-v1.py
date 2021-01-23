#Write your code below this line 👇

def prime_checker(number):

  i = 2
  prime_check = True

  if (number % 1 != 0) | (number == 1):
    prime_check = False
    #print('*')
  else:
    while i < number:
      if number%i == 0:
        prime_check = False
        #print("**")
        break
      i += 1

  if prime_check == True:
    print("It's a prime number")
  else:
    print("It's not a prime number")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



