string=input("Write a string? ")
if int(len(string))%2==0:
    print("The string is even.")
else:
    print("The string is odd.")

  
food=input("What is your favourite food? ")
if food == "mushrooms":
    print("Wow, that’s my favorite too!")
else:
    print("n/")
liked_food_in_common=[]
liked_food_in_common.append(food)


temperature=int(input("What is temperature now? "))
if temperature < 72:
    print("jacket should be worn.")
forecast=input("What is forecast for today? ")
if forecast == "showers" or "rain" or "snow":
    print("umbrella should be brought.")
elif temperature < 72 and forecast == "showers" or "rain" or "snow":
    print("Based on the weather forecast, you should bring a jacket and an umbrella")
elif temperature >= 72 and forecast == "showers" or "rain" or "snow":
    print("Based on the weather forecast, you should bring an umbrella")
elif temperature < 72:
  print("Based on the weather forecast, you should bring a jacket. The weather is great! Have a nice day!")