import pickle
fp=open("pickle.txt","wb")
cn=["dhoni","virat","sachin"]
pickle.dump(cn,fp)
fp.close()
