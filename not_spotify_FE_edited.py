# -*- coding: utf-8 -*-

import mysql.connector
import not_spotify_BE as be

path = 'C:/Users/Ava/Desktop/CS 220 Materials/CSCI220-Final-Project/'

# TO CREATE A PLAYLIST
def playlist(sub, pName, pID):
    print(f'=== {pName} ===\n')
    print("L - List Songs\nS - Search Songs\nA - Add Song\nR - Remove Song\nB - Back")
    user_in = input("Input  Command: ")
    user_in = user_in.lower()
    # list
    if user_in == "l":
        be.Sub.list_songs(pID)
        playlist(sub, pName, pID)
    # search
    elif user_in == "s":
        search()
        playlist(sub, pName, pID)
    # add
    elif user_in == "a":
        input_sName = input("Enter song name:")
        try:
            mycursor.execute("select sID from Song where sName='%s';"% (input_sName))
            sID = mycursor.fetchall()[0]
            # check if song already on playlist
            if len(mycursor.execute("select sID from Is_On where pID=%d and sID=%d;"% (pID, sID)).fetchall()) > 0:
                print("Song Already In Playlist")
            else:
                be.Sub.add_song(pID, sID)
        except Exception:
            print("Song Not Found")
        be.Sub.add_song(pID, sID)
        playlist(sub, pName, pID)
    # remove
    elif user_in == "r":
        input_sName = input("Enter song name:")
        try:
            mycursor.execute("select sID from Song where sName='%s';"% (input_sName))
            sID = mycursor.fetchall()[0]
            # check if song is on playlist
            if len(mycursor.execute("select sID from Is_On where pID=%d and sID=%d;"% (pID, sID)).fetchall()) == 0:
                print("Song Not In Playlist")
            else:
                be.Sub.remove_song(pID, sID)
        except Exception:
            print("Song Not Found")
        playlist(sub, pName, pID)
    # back
    elif user_in == "b":
        sub_menu(sub)
    # unknown
    else:
        print('Command Not Found')
        playlist(sub, pName, pID)

# ARTIST HOME PAGE
def artist_home(sub, artist, aname, aID):
        print(f'=== {aname} ===\n')
        print("I - Info\nS - Songs\nF - Follow\nU - Unfollow\nB - Back")
        user_in = input("Input  Command: ")
        user_in = user_in.lower()
        
        # info
        if user_in == "i":
            be.Artist.info()
            artist_home(sub, artist, aname, aID)
        # songs list
        elif user_in == "s":
            be.Artist.songs()
            artist_home(sub, artist, aname, aID)
        # Follow
        elif user_in == "f":
            be.Sub.follow(aID)
            artist_home(sub, artist, aname, aID)
            # Unfollow
        elif user_in == "f":
            be.Sub.unfollow(aID)
            artist_home(sub, artist, aname, aID)
        elif user_in == "b":
            sub_menu(sub)
        else:
            print("Command Not Found")
            artist_home(sub, artist, aname, aID)

# SEARCH FUNCTION            
def search():
    querry = input("Search: ")
    querry = '"' + querry + "%" + '"'
    mycursor.execute("select sName from Song where sName like '%s';"% (querry))
    for x in mycursor:
        print(x)

# ARTIST SEARCH FUNCTION    
def a_search():
    querry = input("Search: ")
    querry = '"' + querry + "%" + '"'
    mycursor.execute("select aName from Artist where aName like '%s;'"% (querry))
    for x in mycursor:
        print(x)
    
# SUBSCRIBER MENU    
def sub_menu(sub):
    print('=== Subscriber Menu ===\n')
    print("L - Likes\nP - List Playlists\nEP - Edit Playlist\nAP - Add Playlist\nRP - Remove Playlist\nS - Search Songs\nSA - Search Artists\nA - Vew Artist Home\nB - Back To Login\nX - Close Application\n" )
    user_in = input("Input  Command: ")
    user_in = user_in.lower()
    # run playlist menu for likes playlist
    if user_in == "l":
        mycursor.execute('select pID from Playlist where pName="Likes";')
        pID = mycursor.fetchall()[0]
        playlist(sub, "Likes", pID)
        sub_menu(sub)
    # list playlists
    elif user_in == "p":
        be.Sub.playlists()
        sub_menu(sub)
    # edit playlist
    elif user_in == "ep":
        # get playlsit name from user
        pName = input("Input Name of Playlist You Would Like to Edit: ")
        try:
            # find related id
            mycursor.execute("select pID from Playlist where pName='%s';"% (pName))
            pID = mycursor.fetchall()[0]
            # run playist menu for input playlist
            playlist(sub, pName, pID)
        except Exception:
            print("Playlist Not Found")
        sub_menu(sub)
    # add playlist
    elif user_in == "ap":
        input_pName = input("Enter Playlist name:")
        try:
            if len(mycursor.execute("select pID from Playlist where pName='%s';"% (pName)).fetchall()) > 0:
                print("Name Already Taken")
            else:
                be.Sub.add_playlist(pName)
        except Exception as e:
            print(e)
        sub_menu(sub)
    # remove playlist
    elif user_in == "ap":
        input_pName = input("Enter Playlist name:")
        try:
            if len(mycursor.execute("select pID from Playlist where pName='%s';"% (pName)).fetchall()) == 0:
                print("No Such Playlist")
            else:
                be.Sub.remove_playlist(pName)
        except Exception as e:
            print(e)
        sub_menu(sub)
    # search songs
    elif user_in == "s":
        search()
        sub_menu(sub)
    # search artists
    elif user_in == "sa":
        a_search()
        sub_menu(sub)
    # view artist home page
    elif user_in == "A":
        aname = input ("Enter Artist Name: ")
        try:
            mycursor.execute("select aID from Artist where aName='%s';"% (aname))
            aID = mycursor.fetchall()[0]
            artist = Artist(aID, mycursor)
            artist_home(sub, artist, aname, aID)
        except Exception:
            print("Artist Not Found")
    # back
    elif user_in == "b":
        start()
    # close
    elif user_in == "x":
        print("Stopping")
    # not found
    else:
        print("Command Not Found\n")
        sub_menu(sub)

# ARTIST MENU    
def artist_menu(artist):
    print('=== Artist Menu ===\n')
    print("I - Info\nSL - Song List\nSI - Song Info\nA - Add Song\nR - Remove Song\nB - Back To Login\nX - Close Application\n;" )
    user_in = input("Input  Command: ")
    user_in = user_in.lower()
    if user_in == "i":
        be.Artist.info(artist)
        artist_menu(artist)
    elif user_in == "sl":
        be.Artist.songs(artist)
        artist_menu(artist)
    elif user_in == "si":
        input_sName = input("Enter song name:")
        try:
            mycursor.execute("select sID from Song where sName='%s';"% (input_sName))
            sID = mycursor.fetchall()[0][0]
            print("sID is: ", sID)
            be.Artist.song_info(artist, sID)
            artist_menu(artist)
        except Exception:
            print("Song Not Found")
    elif user_in == "a":
        input_sName = input("Enter song name:")
        try:
            be.Artist.add(input_sName)
            artist_menu(artist)
        except Exception:
            print("Invalid Song Name")
            artist_menu(artist)
    elif user_in == "r":
        input_sName = input("Enter song name:")
        try:
            mycursor.execute("select sID from Song where sName='%s';"% (input_sName))
            sID = mycursor.fetchall()[0]
            try:
                be.Artist.song_info(sID)
                artist_menu(artist)
            except Exception as e:
                print(e)
        except Exception:
            print("Song Not Found")
            artist_menu(artist)
    elif user_in == "b":
        start()
    elif user_in == "x":
        print("Stopping")
    else:
        print("Command Not Found")
        artist_menu(artist)
 
# ARTIST LOGIN    
def artist_start():
    aname = input("Log In With Username or Exit: ")
    mycursor.execute("select aID from artist where aName='%s';"% (aname))
    aID = mycursor.fetchall()[0]
    print(aID)
    artist = be.Artist(aID, mycursor)
    artist_menu(artist)

# SUBSCRIBER LOGIN    
def sub_start():
    subName = input("Log In With Username or Exit: ")
    mycursor.execute("select subID from subscriber where subName='%s';"% (subName))
    subID =  mycursor.fetchall()[0]
    sub = be.Subscriber(subID, mycursor)
    sub_menu(sub)

def start():
    print("========== Welcome To Not Spotify ==========")
    login_type = input("Type 'S' for Subscriber login or 'A' for Artist Login: ")
    login_type = login_type.lower()
    if login_type == "a":
        artist_start()
    elif login_type == "s":
        sub_start()
    else:
        print("Unkown input")
        start()


if __name__ == "__main__": 
    try:
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd=".ec33x!FQ?6nM-8",
          use_pure = True
        )
        
        mycursor = mydb.cursor()
        try:
            mycursor.execute("USE NOT_SPOTIFY;")
        except Exception:
            file = open(path+'not_spotify.sql', 'r')
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

        mydb.commit()
        start()
    except Exception as exc:
        print(exc)









