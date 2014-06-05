extras = "a an the of is or it to because some another as has have had are and off on from"
extras=extras.split(" ")
def remv_extra(s):
    b=" "
    s = s.split(" ")
    for letter in s:
        if letter not in extras:
            b+=" "+letter
    return b
    #print len(b)

#remv_extra("Counter-Strike is itself a mod, it has developed its own community of script writers and mod creators. Some mods add bots, while others remove features of the game, and others create different modes of play. Some of the mods give server administrators more flexible and efficient control over his or her server. Admin plugins, as they are mostly referred to as, have become very popular")

punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
#extras = "a an the of is or to because some another as has have had are and off on from"
#extras=extras.split(" ")
def remove_punctuation(s):
    b= " "
    for letter in s:
        if letter not in punctuation:
            b += letter
    return b
