#!/usr/local/bin/python3

import json

lst2 = [] # early declare for loop addition later on
lst4 = [] # early declare for loop addition later on
lst_following = [] # final list for the usernames of people I follow
lst_followers = [] # final list for the usernames of people that follow me
lst_not_following = []  # the list for usernames of people that don't follow me back

# this opens the json file following and stores into the first list
with open("following.json", 'r') as fh:
        s = fh.read()
        lst = json.loads(s)
lst = lst["relationships_following"]

# second list to break into "string_list_data"
for i in lst:
        lst2 += i ['string_list_data']

# final list to store the username
for i in range (0,len(lst2)):
        lst_following += [lst2[i]['value']]

# now time to parse followers file

with open("followers_1.json", 'r') as fh:
        s = fh.read()
        lst3 = json.loads(s)

for i in lst3:
        lst4 += i["string_list_data"]

for i in range (0, len(lst4)):
        lst_followers += [lst4[i]['value']]


# Now time to find out who's following and who's not!

# Since these lists are not sorted and using merge sort would still be an extra looped operation, it would just be better to use linear search
# algo will be O(n^2) since there will be double loops

isFollowing = False

for i in lst_following:
        for j in lst_followers:
                if i == j:
                        isFollowing = True
        
        if (isFollowing == False):
                lst_not_following += [i]
        else:
                isFollowing = False


# now this gets exported to a txt file for better access and storage for the user

with open('NotFollowingBack.txt', 'w') as file:
    # Write each item in the list to a new line in the file
    for item in lst_not_following:
        file.write(item + '\n')
