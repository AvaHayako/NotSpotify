

# making a class
# call main, 
# for whatever type, gonna make another instance of the class
# using whatever subid input it recieves.


from datetime import date

# Artist object
class Artist:
    def __init__(self, aID, mycursor, mydb):
        self.aID = aID
        self.mc = mycursor    
        self.mydb = mydb
    
    # return artist name, song count, likes count, follower count
    def info(self):
        # list of command tuples = (<result identifier>, <SQL command>)
        SQLcommands = [("Name:","Select aName from Artist where aID = %d;"),
                      ("Song count:","Select count(*) from Song where aID = %d;"),
                     ("Like count:","Select sum(like_count) from Song where aID = %d;"),
                     ("Follow count:","Select count(*) from Follow where aID = %d;")]
        
        print('\n=== Your Artist Info ===')
        for c in SQLcommands:
            # execute SQL commands sequentially
            self.mc.execute(c[1]% (self.aID))
            for r in self.mc:
                # print result identifier and result(s) 
                print(c[0], r[0])      
        
    # returns list of all song names
    def songs(self):
        self.mc.execute("Select sName from Song where aID = %d;"% (self.aID))  
        
        print('\n=== Your Songs ===')
        for c in self.mc:
            # list result(s) with comma separators
            print(f"{c[0]},",end=" ")  
        print("\n")
    
    
    # return song title, date published, likes and playlists
    def song_info(self, sID):
        print(sID)
        print(type(sID))
        # list of command tuples = (<result identifier>, <SQL command>)
        SQLcommands = [('Title:', "Select sName From song Where sID = '%s';"),
                    ('Publish date:', "Select publish_date From song Where sID = '%s';"),
                    ('Likes:', "Select like_count From song Where sID = '%s';"),
                    ('Playlists with your song:', """Select P.pName From Playlist as P, Is_On as IO 
                            Where IO.sID = '%s' and IO.pID = P.pID;""")]
                    
        print('\n=== Your Song Info ===')
        for c in SQLcommands: 
            # execute SQL commands sequentially
            self.mc.execute(c[1]% (sID))
            result = self.mc.fetchall()
            # if there's > 1 query result (rows)
            if len(result) > 1:
                print(c[0])
                for r in result:
                    print((r[0]+","),end=" ")
            else:
                print(c[0],end=" ")
                for r in result:
                    print(r[0])
        print("\n")
        
            
    # adds new song to database            
    def add(self, sName, p_date = str(date.today())):
        # derive song name from sID
        sID = str(self.aID) + sName.strip()
        self.mc.execute("insert into Not_Spotify.Song values('%s', %d, '%s', '%s', 0);"% (sID, self.aID, sName, p_date))
        print('\nSong "%s" added!'% (sName))
        self.mydb.commit()

    
    # removes song from database
    def remove(self, sID):
        # derive song name from sID
        sName = sID.replace(str(self.aID),"")
        self.mc.execute("delete from Not_Spotify.Song where Song.sID = '%s';"% (sID))
        print('\nSong "%s" removed!'% (sName))
        self.mydb.commit()
    
    
        




         
# =====TESTING=====

# =============================================================================
# 
# mydb = mysql.connector.connect(
#    host="localhost",
#    user="root",
#    passwd=".ec33x!FQ?6nM-8",
#    use_pure = True
#  )
#  
# mycursor = mydb.cursor()
# #print(mydb)
# mycursor.execute("USE NOT_SPOTIFY;")
# =============================================================================
#=============================================================================         
#a1 = Artist(102, mycursor)
#a1.info()
#a1.songs()
# a1.song_info('"Stronger"')
#a1.add("Poop")
# =============================================================================

                              
