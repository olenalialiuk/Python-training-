string=input("Write a string? ")
if int(len(string))%2==0:
    print("The string is even.")
else:
    print("The string is odd.")

  
food=input("What is your favourite food? ")
if food == "mushrooms":
    print("Wow, that’s my favorite too!")
else:
    print("\n")
liked_food_in_common=[]
liked_food_in_common.append(food)


temperature=int(input("What is temperature now? "))
forecast=input("What is forecast for today? ")
if temperature < 72 and forecast != "showers" and forecast != "rain" and forecast != "snow":
    print("Jacket should be worn.")
elif temperature >= 72 and forecast == "showers" and forecast == "rain" and forecast == "snow":
    print("Umbrella should be brought.")
elif temperature < 72 and forecast == "showers" or forecast == "rain" or forecast == "snow":
    print("Based on the weather forecast, you should bring a jacket and an umbrella")
elif temperature >= 72 and forecast != "showers" or forecast != "rain" or forecast != "snow":
    print("Based on the weather forecast, you should bring an umbrella")
else:
  print("The weather is great! Have a nice day!")
print("\n")

string_1 = len(input("Write the first string? "))
string_2 = len(input("Write the second string? "))
if string_1 == string_2:
    print ("both strings have the same lenth")
else:
    print("The string 1 and string 2 are different.")

fun_list=["Half-Life 2", "Grand Theft Auto V", "The Orange Box"]
challeng_list=["Half-Life", "BioShock", "Grand Theft Auto V"]
game=input("What is your favourite game? ")
if game == fun_list and game == challeng_list:
    print ("I think that one is fun and challenging!")
elif game == fun_list and game != challeng_list:
    print ("I think that one is fun!")
elif game != fun_list and game == challeng_list:
    print ("I think that one is challenging!")
else:
    print ("I don’t think that one is fun or challenging.")