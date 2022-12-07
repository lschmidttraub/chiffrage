def chiffrer(message, clef, n):
    res = ""
    for char in message:
        res+=str((ord(char)**clef)%n)+" "
    return (res)

def dechiffrer(message, clef, n):
    res = ""
    for nb in message.split(" "):
        if nb!="":
            res=res+chr((int(nb)**clef)%n)
    return res