#from bs4 import BeautifulSoup
import sys, urllib, urllib2
from StringIO import StringIO
import html2text
import string
#from Lev import *
#from diff import *
#from lcs import *
from compare import *
from extras import *
def query_google(query, start):

    import urllib2, urllib

        # urlencode the query
    query = urllib.quote(query)
    uip='106.51.114.3'

    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=' + query + '&start=' + str(start) + '&rsz=large'

    try:
        req = urllib2.Request(url)
        opener = urllib2.build_opener()
        data_string = opener.open(req).read()

    except urllib2.URLError:
        print "------ Error opening " + url + "..... Timed out?"
        return None

    # Should use json to parse the results, but instead we're converting the string to dictionary. Duct tape.

    # replace the "null" with "None" for Python
    data_string = data_string.replace(": null,", ": None,")

    # convert the string to a dictionary
    exec("data = " + data_string)

    # simplify the results a bit
    results = data["responseData"]["results"]
    #print results

    # build list of urls
    urls = []

    for i in results:
        url = i["url"]
        url = url.split("%")[0] # get rid of some garbage from the url. Probably avoidable by using Json.
        urls.append(url)

    return urls

########################################################

def get_page(url):
    try:
        import urllib2
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        return opener.open(url)
    except:
        return ""

########################################################

def html_to_text(data):
    import re
    
    # remove the newlines
    data = data.replace("\n"," ")
    data = data.replace("\r"," ")
   
    # replace consecutive spaces into a single one
    data = " ".join(data.split())   
   
    # get only the body content
    bodyPat = re.compile(r'<body[^<>]*?>(.*?)</body>',re.I)
    ace = re.findall(bodyPat, data)
    try:
        data = ace[0]
    except:
        pass
   
    # now remove the java script
    p = re.compile(r'<script[^<>]*?>.*?</script>')
    data = p.sub('', data)
   
    # remove the css styles
    p = re.compile(r'<style[^<>]*?>.*?</style>')
    data = p.sub('', data)
   
    # remove html comments
    p = re.compile(r'')
    data = p.sub('',data)
   
    # remove all the tags
    p = re.compile(r'<[^<]*?>')
    data = p.sub('', data)
   
    return data

##########################################################

def chunks(s,n):
    a=[]
    j=0
    c=0
    b=n
    for i in range(0,len(s)-1,b):
        if s[i]==' ':
            a.append(s[c:i+1])
            c=i
        else:
            while s[i]!=' ':
                i=i+1
            
            a.append(s[c:i+1])
            c=i

    a.append(s[c:]) 
        
    for k in range(0,len(a)-1,1):
        if a[k] == ' ':
            del(a[k])
            
    return a
####################################################################

##getting page
def fill_file(result):
    url = result
    #print url
    f = get_page(url)
    #print f
    if f == "":
        return "a"
    f = f.read()
    ##removes tags
    f = html_to_text(f)
    ##decoding to ASCII
    encoding = 'utf-8'
    try:
        ustr = f.decode(encoding)
    except:
        pass
        return f
    b = StringIO()
    old = sys.stdout
    try:
        sys.stdout = b
        html2text.wrapwrite(html2text.html2text(ustr, url))
    finally: sys.stdout = old
    text = b.getvalue()
    b.close()
    return text

#####################################################################
punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
#extras = "a an the of is or to because some another as has have had are and off on from"
#extras=extras.split(" ")
def remove_punctuation(s):
    b= " "
    for letter in s:
        if letter not in punctuation:
            b += letter
    return b

def begin(chunked_query):
    ##get results
    results = []
    site_list = []
    
    
    for b in chunked_query:
        results+= query_google(b,0)
        
        #print results

    ##store in list
        
    for var in results:
        c = fill_file(var)
        if c == "a":
            results.remove(var)
        else:
            site_list.append(c)
           # site_list.append("\n#####################\n")
    return results,site_list

def detect(a):
    #a = "Counter-Strike is a first-person shooter in which players join either the terrorist team, the counter-terrorist team, or become spectators. Each team attempts to complete their mission objective and/or eliminate the opposing team. Each round starts with the two teams spawning simultaneously.A player can choose to play as one of eight different default character models (four for each side, although Counter-Strike: Condition Zero added two extra models, bringing the total to ten). Players are generally given a few seconds before the round begins (known as freeze time) to prepare and buy equipment, during which they cannot attack or move (one notable exception is that a player may receive damage during freeze time. This happens when a map is changed to spawn players at a certain height above the ground, thus causing fall damage to the player"
    #comp = "Counter-Strike is a first-person shooter in which players join either the terrorist team, the counter-terrorist team, or become spectators. Each team attempts to complete their mission objective and/or eliminate the opposing team. Each round starts with the two teams spawning simultaneously.A player can choose to play as one of eight different default character models (four for each side, although Counter-Strike: Condition Zero added two extra models, bringing the total to ten). Players are generally given a few seconds before the round begins (known as freeze time) to prepare and buy equipment, during which they cannot attack or move (one notable exception is that a player may receive damage during freeze time. This happens when a map is changed to spawn players at a certain height above the ground, thus causing fall damage to the player."
    a = remove_punctuation(a)
    comp = a
    a = chunks(a,250)
    #comp = remove_punctuation(comp)
    comp= remv_extra(comp)
    #print a
    #print comp
    #print len(comp)
    sites,site_list = begin(a)
    lev_list = []
    i=0

    #print len(sites)
    #print len(site_list)
    for item in site_list:
        item = remove_punctuation(item)
        item = remv_extra(item)
        #print item
        lev = compare(item, comp)
        lev_list.append(lev)
        #print sites[i]
        #print lev_list[i]
        print sites[i], lev_list[i]
        i = i+1
    return sites,lev_list

#detect('A mushroom (or toadstool) is the fleshy, spore-bearing fruiting body of a fungus, typically produced above ground on soil or on its food source. The standard for the name mushroom is the cultivated white button mushroom, Agaricus bisporus; hence the word mushroom"is most often applied to those fungi (Basidiomycota, Agaricomycetes) that have a stem (stipe), a cap (pileus), and gills (lamellae, sing. lamella) or pores on the underside of the cap.Mushroom describes a variety of gilled fungi, with or without stems, and the term is used even more generally, to describe both the fleshy fruiting bodies of some Ascomycota and the woody or leathery fruiting bodies of some Basidiomycota, depending upon the context of the word.Forms deviating from the standard morphology usually have more specific names, such as "puffball", "stinkhorn", and "morel", and gilled mushrooms themselves are often called "agarics" in reference to their similarity to Agaricus or their place Agaricales. By extension, the term mushroom can also designate the entire fungus when in culture; the thallus (called a mycelium) of species forming the fruiting bodies called mushrooms; or the species itself.')
