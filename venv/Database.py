import datetime

class DBHelper: 
    
    ##def __init__(self,files):
       ## self.files = []
        ##self.db = environment.PouchDB('corpus')
    


    def pushAll():
        for file in files:
            db.put({"_id":datetime.datetime.now().isoformat(),"title":file.getTitle(),"content":file.getContent()})

    def push(file,content):
        db.put({"_id":datetime.datetime.now().isoformat()},"title":file,"content":content})

        



    

        