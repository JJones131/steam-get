import json
import urllib2



def app_find(appid):
    print "Loading data..."
    data = json.load(urllib2.urlopen('http://api.steampowered.com/ISteamApps/GetAppList/v0001'))

    results = data['applist']['apps']['app']

    #loop through all apps in data
    for r in results:
        #if the appid matches the user's entered id
        if user_enter == str(r['appid']).strip():
            return r['name']

    return

user_enter = raw_input('Please enter ID of App: ').strip()

try:
    #try to convert user_enter to an integer
    #if it succeeds, app continues as normal
    #else ValueError is raised and jumps to except ValueError:
    isValid = int(user_enter)

    if not user_enter:
        print "You haven't entered anything dingus"
    else:
        appName = app_find(user_enter)

        if not appName:
            print "App not found!"
        else:
            print appName

except ValueError:
    print "App IDs are in numbers, please reenter"








