import json
import urllib
import urllib2
import datetime
from datetime import timedelta

key = 'ENTER KEY HERE'

def get_user_name(steamid):
    linkArgs = {'key': key, 'steamids': steamid}
    encodedArgs = urllib.urlencode(linkArgs)

    link = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?' + encodedArgs

    data = json.load(urllib2.urlopen(link))

    result = data['response']['players'][0]['personaname']
    return result

def get_user_logoff(mysteamid):
    linkArgs = {'key': key, 'steamids': mysteamid}
    encodedArgs = urllib.urlencode(linkArgs)

    link = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?' + encodedArgs
    data = json.load(urllib2.urlopen(link))

    result = data['response']['players'][0]['lastlogoff']

    return (datetime.datetime.fromtimestamp(int(result)))#.strftime('%d/%m/%Y  %H:%M:%S'))

dict = { 'username': get_user_name(76561198015367230), 'logoff': get_user_logoff(76561198015367230)}

print dict['username']
print dict['logoff']