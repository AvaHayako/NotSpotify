

# making a class
# call main, 
# for whatever type, gonna make another instance of the class
# using whatever subid input it recieves.

import dns
import mysql.connector
#import date


class Subscriber:
    def __init__(self, sub_ID):
        self.sub_ID = sub_ID
    # songs in playlist
    
class Artist:
    def __init__(self, a_ID, mycursor):
        self.a_ID = a_ID
        self.mc = mycursor
    
    # return artist name, song count, likes count, follower count
    def info(self):
        SQLcommands = [("Name:","Select aName from Artist where aID = %d;"),
                      ("Song count:","Select count(*) from Song where aID = %d;"),
                     ("Like count:","Select sum(like_count) from Song where aID = %d;"),
                     ("Follower count:","Select count(*) from Follow where aID = %d;")]
        
        print('\nArtist Info:')
        for c in SQLcommands: 
            self.mc.execute(c[1]% (self.a_ID))
            for r in self.mc:
                print(c[0], r[0])
    
    # returns list of all song names
    def songs(self):
        self.mc.execute("Select sName from Song where aID = %d;"% (self.a_ID))  
        print('\nAll songs:')
        for c in self.mc:
            print(f"{c[0]}")
    
    # return song title, date published, likes and playlists
    def song_info(self, s_ID):
        SQLcommands = [(['Name:','Publish date:','Likes:'],"""Select sName, publish_date, 
                        like_count From song Where sID = %s;"""),
                       (['Playlist(s) containing song:'], """Select P.pName From Playlist as P, Is_On as IO 
                       Where IO.sID = %s and IO.pID = P.pID;""")]

        for i in range(len(SQLcommands)): 
            self.mc.execute(SQLcommands[i][1]% (s_ID)) #0th command
            for j in range(len(self.mc)):
                print(SQLcommands[i][j], self.mc[j])                
    
    #
    def add(self, s_ID):
        return 0
    
    #
    def remove(self, s_ID):
        return 0




         
# TESTING XDD

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=".ec33x!FQ?6nM-8",
  use_pure = True
)

mycursor = mydb.cursor()
print(mydb)
mycursor.execute("USE FINAL_PROJECT;")
        
a1 = Artist(101, mycursor)
a1.info()
a1.songs()
#a1.song_info('101WeRise')

mydb.commit()