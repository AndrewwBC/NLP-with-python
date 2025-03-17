from nltk.corpus import webtext, nps_chat

for fileid in webtext.fileids():
    print(fileid, webtext.raw(fileid)[:65])
    
print(nps_chat.posts('10-19-20s_706posts.xml')[123])