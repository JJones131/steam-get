import json
import urllib
import urllib2
import datetime
from datetime import timedelta
import SteamObjects

#!/usr/bin/python


key = 'ENTER STEAM API KEY HERE'


def access_friendlist(steamid):
    friendsList = []

    linkArgs = {'key': key, 'steamid': steamid, 'relationship': 'friend'}
    encodedArgs = urllib.urlencode(linkArgs)

    link = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?' + encodedArgs
    data = json.load(urllib2.urlopen(link))

    results = data['friendslist']['friends']

    for r in results:
        friend = SteamObjects.FriendList()

        friend.steamid = r.get('steamid')
        friend.relationship = r.get('relationship')
        friend.friend_since = datetime.datetime.fromtimestamp(int(r.get('friend_since', 0)))
        friend.friend_sinceunix = r.get('friend_since', 0)

        friendsList.append(friend)


    return friendsList


def get_user_name(steamid):
    linkArgs = {'key': key, 'steamids': steamid}
    encodedArgs = urllib.urlencode(linkArgs)

    link = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?' + encodedArgs

    data = json.load(urllib2.urlopen(link))

    result = data['response']['players'][0]['personaname']
    return result


def get_user_names(steamids):
    usernames = []

    #print ",".join(steamids)

    linkArgs = {'key': key, 'steamids': ",".join(steamids)}
    encodedArgs = urllib.urlencode(linkArgs)

    link = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?' + encodedArgs

    data = json.load(urllib2.urlopen(link))

    results = data['response']['players']

    #loop through results and add each personaname to the list
    for u in results:
        usernames.append(u['personaname'].strip())

    return usernames


def get_user_info(steamid):
    user = SteamObjects.PlayerSummary()

    linkArgs = {'key': key, 'steamids': steamid}
    encodedArgs = urllib.urlencode(linkArgs)

    link = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?' + encodedArgs

    data = json.load(urllib2.urlopen(link))

    playerInfo = data['response']['players']

    for p in playerInfo:
        user.steamid = p.get('steamid')
        user.communityvisibilitystate = p.get('communityvisibilitystate', 1)
        user.profilestate = p.get('profilestate', 0)
        user.personaname = p.get('personaname')
        user.lastlogoff = datetime.datetime.fromtimestamp(int(p.get('lastlogoff', 0)))
        user.lastlogoffunix = p.get('lastlogoff', 0)
        user.profileurl = p.get('profileurl')
        user.avatar = p.get('avatar')
        user.avatarmedium = p.get('avatarmedium')
        user.avatarfull = p.get('avatarfull')
        user.personastate = p.get('personastate', 0)
        user.primaryclanid = p.get('primaryclanid')
        user.timecreated = datetime.datetime.fromtimestamp(int(p.get('timecreated', 0)))
        user.timecreatedunix = p.get('timecreated', 0)
        user.personastateflags = p.get('personastateflags')

        state = user.personastate

        if state == 0:
            user.personastatetext = "Offline"
        elif state == 1:
            user.personastatetext = "Online"
        elif state == 2:
            user.personastatetext = "Busy"
        elif state == 3:
            user.personastatetext = "Away"
        elif state == 4:
            user.personastatetext = "Snooze"
        elif state == 5:
            user.personastatetext = "Looking to trade"
        elif state == 6:
            user.personastatetext = "Looking to play"
        else:
            user.personastatetext = ""

    return user

steamid = str(raw_input('Please enter your 64 bit Steam ID here: ')).strip()

if not steamid.isdigit():
    print 'That is not a valid Steam ID'
    exit()

now = datetime.datetime.now()

yesterday = timedelta(hours=24)
diff = now - yesterday

friends = access_friendlist(steamid)

userFilter = raw_input("Please enter first character of username you'd like to filter or leave empty for all results: ").strip()

for friendObj in friends:
    # username = get_user_name(r)
    # logOff = get_user_logoff(r)

    userInfo = get_user_info(friendObj.steamid)

    print userInfo.steamid + ": " + userInfo.personaname
    print "Last logged off: " + str(userInfo.lastlogoff)
    print "Status: " + userInfo.personastatetext
    print "Profile URL: " + userInfo.profileurl
    print "Friend since: " + str(friendObj.friend_since)

    print
    print "---------------------"
    print

    # if userInfo.personaname.startswith(userFilter) and userInfo.lastlogoff > diff:
    #     print userInfo.personaname + " " + "last logged off at " + str(userInfo.lastlogoff) + " with steamid: " + userInfo.steamid


#
