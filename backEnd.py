

# making a class
# call main, 
# for whatever type, gonna make another instance of the class
# using whatever subid input it recieves.

#import dns
import mysql.connector
from datetime import date


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
                     ("Follow count:","Select count(*) from Follow where aID = %d;")]
        
        print('\nYour Artist Info:')
        for c in SQLcommands: 
            self.mc.execute(c[1]% (self.a_ID))
            for r in self.mc:
                print(c[0], r[0])
    
    
    # returns list of all song names
    def songs(self):
        self.mc.execute("Select sName from Song where aID = %d;"% (self.a_ID))  
        print('\nAll Songs:')
        for c in self.mc:
            print(f"{c[0]},",end=" ")
        print("\n")
    
    
    # return song title, date published, likes and playlists
    def song_info(self, s_ID):
        SQLcommands = [('Title:', "Select sName From song Where sID = %s;"),
                    ('Publish date:', "Select publish_date From song Where sID = %s;"),
                    ('Likes:', "Select like_count From song Where sID = %s;"),
                    ('Playlists with your song:', """Select P.pName From Playlist as P, Is_On as IO 
                            Where IO.sID = %s and IO.pID = P.pID;""")]
        print('\nYour Song Info:')
        for i in range(len(SQLcommands)): 
            self.mc.execute(SQLcommands[i][1]% (s_ID))
            result = self.mc.fetchall()
            if len(result) > 1:
                print(SQLcommands[i][0])
                for r in result:
                    print((r[0]+","),end=" ")
            else:
                print(SQLcommands[i][0],end=" ")
                for r in result:
                    print(r[0])
        print("\n")
            
    # adds new song to database            
    def add(self, s_ID, p_date = str(date.today())):
        sName = s_ID.replace(str(self.a_ID),"")
        self.mc.execute("insert into Not_Spotify.Song values('%s', %d, '%s', '%s', 0);"% (s_ID, self.a_ID, sName, p_date))
        print('\nSong %s added!'% (sName))
        mydb.commit()

    
    #
    def remove(self, sName):
        s_ID = str(self.a_ID)+sName
        self.mc.execute("delete from Not_Spotify.Song where sID = '%s';"% (s_ID))
        print('\nSong %s removed!'% (sName))
        mydb.commit()
        




         
# TESTING XDD

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=".ec33x!FQ?6nM-8",
  use_pure = True
)

mycursor = mydb.cursor()
print(mydb)
mycursor.execute("USE NOT_SPOTIFY;")
        
a1 = Artist(102, mycursor)
a1.info()
a1.songs()
a1.song_info('"102Stronger"')
#a1.add("102Nectar",p_date="2019/5/31")

mydb.commit()
                              
# SELECT S.sName, S.publish_date, S.like_count, P.pname 
#   FROM [Order] O 
#   JOIN OrderItem I ON O.Id = I.OrderId 
#   JOIN Product P ON P.Id = I.ProductId
# ORDER BY O.OrderNumber

