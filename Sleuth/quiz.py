# ask the candidate a question
activity = input( "How would you like to spend your evening?\n(A)Reading a book\n(B)Attending a party\n ")
print( f"You chose {activity}.")
if activity == "A":
    print( "Nice choise!")
elif activity == "B":
    print( "Sounds fun!" )
else:
    print( "You must type A or B, let's just say you like to read")
    
# ask the candidate a second question
job = input( "What is your dream job?\n(A) Curator at the Smithsonian\n(B)Running a businnes\n ")
print( f"You chose {job}.")
if job == "A":
    print( "Curator, Nice choise!")
elif job == "B":
    print( "Running a business, Sounds fun!" )
else:
    print( "You must type A or B, let's just say you like to read")

    # ask the candidate a third question
value = input( "Whay is more important?\n(A) Money\n(B)Love\n ")
print( f"You chose {value}.")
if value == "A":
    print( "Money, Nice choise!")
elif value == "B":
    print( "Love, Sounds fun!" )
else:
    print( "You must type A or B, let's just say you like to read")

    # ask the candidate a fourth question
decade = input( "What is your favorite decade?\n(A) 1910s\n(B)2010s\n ")
print( f"You chose {decade}.")
if decade == "A":
    print( "1910s, Nice choise!")
elif decade == "B":
    print( "2010s, Sounds fun!" )
else:
    print( "You must type A or B, let's just say you like to read")

    # ask the candidate a fifth question
travel = input( "What is your favorite way to travel?\n(A) Driving\n(B)Flying a party\n ")
print( f"You chose {travel}.")
if travel == "A":
    print( "Driving, Nice choise!")
elif travel == "B":
    print( "Flying, Sounds fun!" )
else:
    print( "You must type A or B, let's just say you like to read")

# print out their choise
print( f"You chose {activity}, then {job}, then {value}, then {decade}, then {travel}.")

sam_like = 0
cam_like = 0
kai_like = 0
indy_like = 0

#Actividad
if activity == "A":
    sam_like = sam_like + 2
    indy_like = indy_like + 2
    kai_like = kai_like + 2
else:
    cam_like = cam_like + 1
    indy_like = indy_like + 1

#Job
if job == "A":
    sam_like = sam_like + 2
    indy_like = indy_like + 2
    cam_like = cam_like + 2
else:
    sam_like = sam_like - 1
    kai_like = kai_like + 2
    indy_like = indy_like +1

#Value
if value == "A":
    sam_like = sam_like -1
    kai_like = kai_like +1
else:
    sam_like = sam_like + 2
    cam_like = cam_like + 2
    indy_like = indy_like + 1

#Decade
if decade == "A":
    cam_like = cam_like + 2
    sam_like = sam_like + 2
else:
    kai_like = kai_like + 1
    indy_like = indy_like + 2

#travel
if travel == "A":
    sam_like = sam_like - 2
    kai_like = kai_like + 1
    indy_like = indy_like -1
else:
    sam_like = sam_like + 1
    cam_like = cam_like + 1
    kai_like = kai_like - 1

#Print the results depending on the score
if sam_like >= 3:
    print( "You are most like Sharp-eyed Sam!" )
elif cam_like >= 3:
    print( "You're most like Curius cam" )
elif kai_like >= 3:
    print( "You're most like Keen Kai!" )
else:
    print( "You're most like Inquisitive Indy!" )
    



