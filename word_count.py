*** Count the frequency of each word in a given string."""

def word_count(string):
    d=dict()
    l=string.split()
    for i in l:
        if i in d.keys():
            d[i]=d[i]+1
        else:
            d[i]=1
    return d
    
if __name__=="__main__":
    s="Any string with some values . values can be anything"
    print(word_count(s))
