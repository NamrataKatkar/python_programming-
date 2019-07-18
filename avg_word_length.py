 def avg_word_len(string):
    l=list(string.split())
    s=0
    for i in range(0,len(l)):
      s+=len(l[i])
    avg=s/len(l)
    return avg
  
 if __name__=='__main__':
    string="Calculate the avg length of words in a sentence"
    print(avg_word_len(string))
