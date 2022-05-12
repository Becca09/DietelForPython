from functools import reduce

users = [
    {"userName": "@Onike_of lagos", "age": 24,
     "tweets": ["i love being a product designer", "out with my girls today @steffi @rosie",
                "thanks to my man @vick for the beautiful gift",
                "did a good prank on my sisters today @summy @becks lmao",
                "literally obsessed with my monazeni collection", "promoted to a senior designer!!"], "verified": True},

    {"userName": "@aunty_bob", "age": 27,
     "tweets": ["guyssss started my journey at semicolon africa today",
                "lmaooo, got a new name in class today AUNTY BOB",
                "omo guys java dey stress me but i LOVEET!!!",
                "i have stockholm syndrome, my java teacher is my abuser lmaooooo",
                "love my baby joel so much"], "verified": True},

    {"userName": "@iyawo anobi", "age": 25,
     "tweets": [" peep my girls @aunty_bob, @AsherFlo WOMEN IN TECH", "this life ehn, i like enjoyment die",
                "anobi and i are going to dubia for the weekend", "i live a soft life"], "verified": "yes"},

    {"userName": "@AdvancedWorm", "age": 20,
     "tweets": [" i will die for python", "java is overrated abeg"], "verified": False},

    {"userName": "@priest", "age": 22,
     "tweets": ["offendee", "tall java lord", "love to look for @aunty_bob trouble",
                "let's chat about OOP in java, see you in the comment section"], "verified": True},

    {"userName": "@BigHeadedLawyer", "age": 42,
     "tweets": ["moving to tech, head is big enough to carry stuff"], "verified": False},

    {"userName": "@annoyingLadi", "age": 50,
     "tweets": [], "verified": False},

    {"userName": "@crazyTolani", "age": 26,
     "tweets": ["i want to retire when i am thirty and enjoy big booties till i die",
                "i am literally a very intelligent stupid person",
                "@iyawo anobi, abeg help me buy abaya 40k for one my sidechicks when coming from dubia"],
     "verified": True},

    {"userName": "@ShomoluTechBro", "age": 28,
     "tweets": ["i am a trenchies TechBro" "chasing the better life", "@crazyTolani you be werey lamoooo"],
     "verified": False},

    {"userName": "@SilentSeun", "age": 25,
     "tweets": ["silence everyWhere"],
     "verified": False}
]
verifiedUsers = [user['userName'] for user in users if user['verified']]
# verifiedUsers = map(lambda y: y['userName'], filter(lambda x: x['verified'], users))
# verifiedUsers = filter(lambda x: x, map(lambda x: x ['userName'] if x['verified'] else False, users))
print(verifiedUsers)

print()
print()

ActiveUsers = [user['userName'] for user in users if len(user['tweets']) > 0]
print(ActiveUsers)

print()
print()

usersBelow25 = [user['userName'] for user in users if (user['age']) <= 25 and user['verified']]
print(usersBelow25)

print()
print()

MaxAgeOfTwitterUser = max(user['age'] for user in users)
print("The oldest twitter user is ", MaxAgeOfTwitterUser)

print()
print()

avg = sum(user['age'] for user in users) / len(users)
print("average age is ", avg)

print()
print()

minAge = min(user['age'] for user in users)
print("The youngest twitter user is ", minAge)

print()
print()

userWithMostTweet = max(users, key=lambda user: len(user['tweets']))
print("the user with the most tweet is ", userWithMostTweet)

print()
print()

AgeAscend = sorted(users, key=lambda user: user['age'])
AgeDescending = sorted(users, key=lambda user: user['age'], reverse=True)
print(AgeAscend)
print(AgeDescending)

print()
print()

nameAscend = sorted(users, key=lambda user: user['userName'])
nameDescending = sorted(users, key=lambda user: user['userName'], reverse=True)
print(nameAscend)
print(nameDescending)

print()
print()

# USER WITH LONGEST NAME
longest_name_ = max(users, key=lambda x: len(x["userName"]))
print("USER WITH LONGEST NAME: ", longest_name_["userName"])

longest_name = reduce(lambda x, y: x if len(x["userName"]) > len(y["userName"]) else y, users)
print("USER WITH LONGEST NAME: ", longest_name["userName"])


print()
print()


# USER WITH THE MOST TWEET
most_tweet_ = max(users, key=lambda x: len(x["tweets"]))
print("USER WITH THE MOST TWEET: ", most_tweet_["userName"])
print(most_tweet_["tweets"])

most_tweet = reduce(lambda x, y: x if len(x["tweets"]) > len(y["tweets"]) else y, users)
print("USER WITH THE MOST TWEET: ", most_tweet["userName"])
print(most_tweet["tweets"])
