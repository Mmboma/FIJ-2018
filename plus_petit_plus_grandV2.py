import random 

nombre_a_trouver = random.randrange(100)

continuer = True 

while  continuer == True:

  entree = int ( input("taper un nombre"))

  if nombre_a_trouver > entree :
    print ("le nombr est plus grand")
  elif  nombre_a_trouver < entree :
    print("le nombre est plus petit")
  else:
    print ("Bravoooooo!!!!!")  
    continuer = False 
