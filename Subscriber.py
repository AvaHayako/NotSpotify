# -*- coding: utf-8 -*-
"""
Created on Mon May  4 00:53:12 2020

@author: Nicholas
"""

import mysql.connector
#import date


class Subscriber:
    def __init__(self, sub_ID, cursor, db):
        self.sub_ID = sub_ID
        self.db = db
        self.c = cursor
    # list songs in input playlist
    def list_songs(self, pID):
        self.c.execute("select S.sName from Song S, Is_On O where S.sID=O.sID and O.pID=%s;"% (pID))
        results = self.c.fetchall()
        self.c.execute("Select pName from Playlist where pID=%s"%(pID))
        p = self.c.fetchall()[0]
        print(f"Songs on {p}")
        for x in results:
            print(x)
    
    # add input song to input playlist
    def add_song(self, pID, sID):
        self.c.execute("insert into Is_On values (%s,'%s');"% (sID, pID))
        self.db.commit()
        self.c.execute("Select sName from Song where sID=%s"%(sID))
        s = self.c.fetchall()[0]
        self.c.execute("Select pName from Playlist where pID='%s'"%(pID))
        p = self.c.fetchall()[0]
        print(f"= {s} has been added to {p} =")
    
    # update playlsit privacy
    def change_privacy(self, pID, privacy):
        self.c.execute("update Playlist set privacy=%s where pID='%s';"% (privacy, pID))
        self.db.commit()
        self.c.execute("Select pName from Playlist where pID='%s'"%(pID))
        p = self.c.fetchall()[0]
        if (privacy == "TRUE"):
            print(f"= {p} is now public! =")
        else:
            print(f"= {p} is now private! =")
            
    # remove input song from input playlsit
    def remove_song(self, pID, sID):
        self.c.execute("delete from Is_On where sID=%s and pID='%s';"% (sID, pID))
        self.db.commit()
        self.c.execute("Select sName from Song where sID=%s"%(sID))
        s = self.c.fetchall()[0]
        self.c.execute("Select pName from Playlist where pID='%s'"%(pID))
        p = self.c.fetchall()[0]
        print(f"= {s} has been removed from {p} =")
        
    # follow input artist
    def follow(self, aID):
        self.c.execute("insert into Follow values (%s,%s);"% (self.sub_ID, aID))
        self.db.commit()
        self.c.execute("Select aName from Artist where aID=%s"%(aID))
        a = self.c.fetchall()[0]
        print(f"= Followed {a} =")
    
    # unfollow input artist
    def unfollow(self, aID):
        self.c.execute("delete from Follow where subID=%d and aID=%s;"% (self.sub_ID, aID))
        self.db.commit()
        self.c.execute("Select aName from Artist where aID=%d"%(aID))
        a = self.c.fetchall()
        print(f"= Unfollowed {a} =")
    
    # list all playlists
    def playlists(self):
        self.c.execute("select P.pName from Playlist P where P.subID=%s;"% (self.sub_ID))
        results = self.c.fetchall()
        for x in results:
            print(x)

    # create a new playlsit
    def add_playlist(self, pName):
        self.c.execute("insert into Playlist values('%s',%s,'%s',False);"% (str(self.sub_ID)+(pName.replace(" ", "")), self.sub_ID, pName ))
        self.db.commit()
        print(f"= Created Playlist {pName} =")
    # remove a playlsit
    def remove_playlist(self, pID):
        self.c.execute("select P.pName from Playlist P where P.pID='%s';"% (pID))
        pName = self.c.fetchall()[0]
        self.c.execute("delete from Playlist where pID=%s;"% (pID))
        self.c.execute("delete from Is_On where pID=%s;"% (pID))
        self.db.commit()
        print(f"= Created Playlist {pName} =")
        
    # return artists you are following
    def following(self):
        self.c.execute("select A.aName from Artist A, Follow F where F.subID=%s and F.aID=A.aID;"% (self.sub_ID))
        result = self.c.fetchall()
        print("Artists You Are Following:")
        for x in result:
            print(x)
    
if __name__ == "__main__": 
    try:
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="nimitchell220",
          use_pure = True
        )
        mycursor = mydb.cursor()
        try:
            mycursor.execute('USE final_project;')
        except Exception:
            file = open('not_spotify.sql', 'r')
            sql = s = " ".join(file.readlines())
            sql_lines = sql.replace('\n','').replace(';',';\n').split("\n")
            for l in sql_lines:
                if len(l) > 0:
                    try:
                        mycursor.execute(l) # this line should only be ran the first time you run this code
                    except Exception as exc:
                        print(exc)
            mydb.commit()
            file.close()
    except Exception as exc:
        print(exc)
    sub = Subscriber(1, mycursor, mydb)
    #sub.add_playlist("Fyre Beatz")
    sub.playlists()
    sub.add_song("1FyreBeatz", 101)
    sub.list_songs("1FyreBeatz")
    sub.change_privacy("1FyreBeatz", "TRUE")
    sub.remove_song("1FyreBeatz", 101)
    sub.list_songs("1FyreBeatz")
    sub.remove_playlist("1FyreBeatz")
    sub.follow(101)
    sub.following()
    sub.unfollow(101)
    sub.following()
    

    
