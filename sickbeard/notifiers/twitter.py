"""Shamelessly ripped from a comment by dbr:
http://commandline.org.uk/python/scripting-twitter-with-python/#c606"""

import urllib

def truncate(string,target):
    if len(string) > target:
        return string[:(target-3)] + "..."
    else:
        return string

def squawk(username,password,message):
    """Simple post-to-twitter function"""
    message = truncate(message,140) # trim message
    data = urllib.urlencode({"status" : message})
    res = urllib.urlopen("http://%s:%s@twitter.com/statuses/update.xml" % \
                         (username,password), data)

def sendTwitter(options, message = None):
    """ Posts message to twitter.  Username/password in options.
        options is a dict with the following keys:
            options['username']:  Surprisingly contains the twitter username
            options['password']:  Yeah this is the twitter password
    """
    if message != None:
        squawk(options['username'], options['password'], message)

if __name__ == "__main__":
    username = raw_input("Enter twitter username: ")
    password = raw_input("Enter twitter password: ")
    message = raw_input("Enter twitter update message: ")
    sendTwitter({'username': username, 'password': password}, message)