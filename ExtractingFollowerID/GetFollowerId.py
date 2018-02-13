
'''
Created on 17 Nov 2017

@author: Ruwan Perera
'''
import twitter
import re
api = twitter.Api(consumer_key='6DQAErJBT7i9NOysBwQIjSPTH',
                      consumer_secret='B6yMjlOJSE6OBlm9JLQC1w4q7G18bpvn94y4e076ZiDUDSXc6r',
                      access_token_key='849391373958688768-7xMmUPRhlwM20BZ7sAo69MslHFMzNWc',
                      access_token_secret='RrMulWbyPa5yc5OH3uEkrRk10QCHgXnXDNIkVP6k2E1GQ')
import sys
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)
TimesOfAppearenceIND = 0
TimesOfAppearenceUK = 0
TimesOfAppearenceUSA = 0
TimesOfAppearenceCHINA = 0
TimesOfAppearenceJP = 0

India = []
UK =[]
China =[]
USA = []
Japan = []
#print(api.VerifyCredentials())
#user_profile = api.VerifyCredentials()
#print(user_profile)

# Get your own friend list authenticated above
#users = api.GetFriends()
#print([u.name for u in users])

#user = api.GetUser(screen_name = 'ruwanperera1222')
#print(user)
#print(user.id)
#print(user.name)
#user = api.GetUser(screen_name = 'saimadhup')
#print(user.id)
#user = api.GetFollowers(screen_name = 'saimadhup')
user = api.GetFriends(screen_name = 'saimadhup')
friend_count = len(user)
for w in user:
    if w.name == "":
        uprint("finish")
    else:
        #uprint(w.name, w.id, w.lang, w.screen_name, w.location, w.created_at, w.geo_enabled)
        uprint(w.name,w.screen_name, w.lang, w.location)
        list_of_words = w.location.split()
#    if w.location == "India":
        for word in list_of_words:
            if 'india' in word.lower():
                India.append(w.screen_name)
                TimesOfAppearenceIND +=1
#                uprint('TimesOfAppearenceIND',TimesOfAppearenceIND)
            else :
                if 'uk' in word.lower():
                    UK.append(w.screen_name)
                    TimesOfAppearenceUK +=1
#                   uprint('TimesOfAppearenceUK',TimesOfAppearenceUK)
                else :
                    if 'china' in word.lower():
                        China.append(w.screen_name)
                        TimesOfAppearenceCHINA +=1
#                        uprint('TimesOfAppearenceCHINA',TimesOfAppearenceCHINA)
                    else :
                        if 'jp' in word.lower():
                            Japan.append(w.screen_name)
                            TimesOfAppearenceJP +=1
#                            uprint('TimesOfAppearenceJP',TimesOfAppearenceJP)
                        else :
                            if 'usa' in word.lower():
                                USA.append(w.screen_name)
                                TimesOfAppearenceUSA +=1
#                                uprint('TimesOfAppearenceUSA',TimesOfAppearenceUSA)


uprint(friend_count)
uprint('TimesOfAppearenceIND',TimesOfAppearenceIND)
uprint('TimesOfAppearenceUK',TimesOfAppearenceUK)
uprint('TimesOfAppearenceCHINA',TimesOfAppearenceCHINA)
uprint('TimesOfAppearenceUSA',TimesOfAppearenceUSA)
uprint('TimesOfAppearenceJP',TimesOfAppearenceJP)
uprint(India)#user = api.GetUser(user_id = 937364378055196672)
#uprint(China)
#uprint(Japan)
#uprint(UK)
#uprint(USA)
#uprint(India)
uprint(TimesOfAppearenceIND)

for k in range(len(India)):
    TimesOfAppearenceIND = 0
    user = api.GetFriends(screen_name = India[k])
    uprint('name',India[k])
    friend_count = len(user)
    uprint('friend count',friend_count)
    for w in user:
        if w.name == "":
            uprint("finish")
        else:
        #uprint(w.name, w.id, w.lang, w.screen_name, w.location, w.created_at, w.geo_enabled)
#           uprint(w.name,w.screen_name, w.lang, w.location)
            list_of_words = w.location.split()
#    if w.location == "India":
            for word in list_of_words:
                if 'india' in word.lower():
                    India.append(w.screen_name)
                    TimesOfAppearenceIND +=1
#                   uprint('TimesOfAppearenceIND',TimesOfAppearenceIND)
                else :
                    if 'uk' in word.lower():
                        UK.append(w.screen_name)
                        TimesOfAppearenceUK +=1
#                       uprint('TimesOfAppearenceUK',TimesOfAppearenceUK)
                    else :
                        if 'china' in word.lower():
                            China.append(w.screen_name)
                            TimesOfAppearenceCHINA +=1
#                           uprint('TimesOfAppearenceCHINA',TimesOfAppearenceCHINA)
                        else :
                            if 'jp' in word.lower():
                                Japan.append(w.screen_name)
                                TimesOfAppearenceJP +=1
#                                uprint('TimesOfAppearenceJP',TimesOfAppearenceJP)
                            else :
                                if 'usa' in word.lower():
                                    USA.append(w.screen_name)
                                    TimesOfAppearenceUSA +=1
#                                   uprint('TimesOfAppearenceUSA',TimesOfAppearenceUSA)

    uprint('TimesOfAppearenceIND',TimesOfAppearenceIND)
uprint('TimesOfAppearenceUK',TimesOfAppearenceUK)
uprint('TimesOfAppearenceCHINA',TimesOfAppearenceCHINA)
uprint('TimesOfAppearenceUSA',TimesOfAppearenceUSA)
uprint('TimesOfAppearenceJP',TimesOfAppearenceJP)
#uprint(India)#user = api.GetUser(user_id = 937364378055196672)
#uprint(China)
#uprint(Japan)
#uprint(UK)
#uprint(USA)
uprint(TimesOfAppearenceIND)
uprint(India)
#print(user.name)
#print(user.lang)
#print(user.default_profile_image)









# Get a anonymous users friend list
#username = "Andypiper"
#queryone = api.GetFriends(screen_name=username)
#print(len(queryone["ids"]))
#querytwo = api.GetFollowers(screen_name = username, cursor=-1, count=5)

#querytwo = api.GetFollowers(user_id, screen_name, cursor, count, total_count, skip_status, include_user_entities)
#print user_profile['created_at']
#for line in user_profile:
#GET https://api.twitter.com/1.1/followers/ids.json?cursor=-1&screen_name=andypiper&count=5000

#test changes at origin and pulling at desk top

