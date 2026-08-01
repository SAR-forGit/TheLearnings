# Verify your Username:
givenName = input("Enter your name: ")

recommendedUsername = "@" + givenName.lower() + str(len(givenName));

while(1):
    userName = input(f"we recommend you username {recommendedUsername}. Do you wnat to use it?")
    userAnswer = userName
    
    if(userAnswer == "yes" or userAnswer == "YES" or userAnswer == "Y" or userAnswer == "y"):
        userName = recommendedUsername
        break
    elif(userAnswer == "No" or userAnswer == "no" or userAnswer == "NO" or userAnswer == "n" or userAnswer == "N"):
        userName = input("Enter your desired username: ")
        userAnswer = input(f"are you sure for the username {"@"+userName}")
        while(1 or userAnswer == "No" or userAnswer == "no" or userAnswer == "NO" or userAnswer == "n" or userAnswer == "N"):
            userName = input("Enter your desired username: ");
            userAnswer = input(f"are you sure for the username ${"@"+userName}")
            if(userAnswer == "yes" or userAnswer == "YES" or userAnswer == "Y" or userAnswer == "y"): break
            else: continue
        break
    else:
        userName = input("Wrong Answer! Try Again.")
        continue
print(f"Hey ${givenName}, your username is set to {userName}")

#Replace
nigg = "Hi, NIGG how are you?"
nigg = nigg.replace("NIGG", "Slave", 1)
print(nigg)

#Replace All
nigg = "Hello Nigg, How are you Nigg?"
nigg = nigg.replace("NIGG", "Slave")
print(nigg)
