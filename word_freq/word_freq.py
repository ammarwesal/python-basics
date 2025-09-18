def word_freq():
  f=open("words.txt","rt")
  c={}
  for line in f:
   words=line.split()
   for word in words:
     if word in c:
      c[word]+=1
     else:
      c[word]=1
  
  f.close()
  return c

word_count=word_freq()
for word , count in word_count.items():
    print(f"'{word}':{count}")
  

