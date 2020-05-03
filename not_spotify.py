
import mysql.connector

def playlist(sub, name, pid):
    print(f'=== {name} ===\n')
    print("L - List Songs\nS - Search Songs\nA - Add Song\nR - Remove Song\nB - Back")
    user_in = input("Input  Command: ")
    user_in = user_in.lower()
    # list
    if user_in == "l":
        sub.list_songs(pid)
        playlist(sub, name, pid)
    # search
    elif user_in == "s":
        search()
        playlist(sub, name, pid)
    # add
    elif user_in == "a":
        input_sname = input("Enter song name:")
        try:
            sid =  mycursor.execute("select sid from Song where sname==%(input_sname)s", (input_sname))
            # check if song already on playlist
            if len(mycursor.execute("select sid from Is_On where pid==%(pid)d and sid==%(sid)d", (pid, sid))) > 0:
                print("Song Already In Playlist")
            else:
                sub.add_song(pid, sid)
        except Exception:
            print("Song Not Found")
        sub.add_song(pid, sid)
        playlist(sub, name, pid)
    # remove
    elif user_in == "r":
        input_sname = input("Enter song name:")
        try:
            sid =  mycursor.execute("select sid from Song where sname==%(input_sname)s", (input_sname))
            # check if song is on playlist
            if len(mycursor.execute("select sid from Is_On where pid==%(pid)d and sid==%(sid)d", (pid, sid))) == 0:
                print("Song Not In Playlist")
            else:
                sub.remove_song(pid, sid)
        except Exception:
            print("Song Not Found")
        playlist(sub, name, pid)
    # back
    elif user_in == "b":
        sub_menu(sub)
    # unknown
    else:
        print('Command Not Found')
        playlist(sub, name, pid)
        
def artist_home(sub, artist, aname, aid):
        print(f'=== {aname} ===\n')
        print("I - Info\nS - Songs\nF - Follow\nU - Unfollow\nB - Back")
        user_in = input("Input  Command: ")
        user_in = user_in.lower()
        
        # info
        if user_in == "i":
            artist.info()
            artist_home(sub, artist, aname, aid)
        # songs list
        elif user_in == "s":
            artist.songs()
            artist_home(sub, artist, aname, aid)
        # Follow
        elif user_in == "f":
            sub.follow(aid)
            artist_home(sub, artist, aname, aid)
            # Unfollow
        elif user_in == "f":
            sub.unfollow(aid)
            artist_home(sub, artist, aname, aid)
        elif user_in == "b":
            sub_menu(sub)
        else:
            print("Command Not Found")
            artist_home(sub, artist, aname, aid)
            
def search():
    querry = input("Search: ")
    querry = '"' + querry + "%" + '"'
    mycursor.execute("select sname from Song where sname like %(querry)s", (querry))
    for x in mycursor:
        print(x)
    
def a_search():
    querry = input("Search: ")
    querry = '"' + querry + "%" + '"'
    mycursor.execute("select aname from Artist where aname like %(querry)s", (querry))
    for x in mycursor:
        print(x)
    
    
def sub_menu(sub):
    print('=== Subscriber Menu ===\n')
    print("L - Likes\nP - List Playlists\nEP - Edit Playlist\nAP - Add Playlist\nRP - Remove Playlist\nS - Search Songs\nSA - Search Artists\nA - Vew Artist Home\nB - Back To Login\nX - Close Application\n" )
    user_in = input("Input  Command: ")
    user_in = user_in.lower()
    # run playlist menu for likes playlist
    if user_in == "l":
        pid =  mycursor.execute('select pid from Playlist where pname=="Likes"')
        playlist(sub, "Likes", pid)
        sub_menu(sub)
    # list playlists
    elif user_in == "p":
        sub.playlists()
        sub_menu(sub)
    # edit playlist
    elif user_in == "ep":
        # get playlsit name from user
        pname = input("Input Name of Playlist You Would Like to Edit: ")
        try:
            # find related id
            pid =  mycursor.execute('select pid from Playlist where pname==%(pname)s', (pname))
            # run playist menu for input playlist
            playlist(sub, pname, pid)
        except Exception:
            print("Playlist Not Found")
        sub_menu(sub)
    # add playlist
    elif user_in == "ap":
        input_pname = input("Enter Playlist name:")
        try:
            if len(mycursor.execute("select pid from Playlist where pname==%(pname)d", (pname)) > 0:
                print("Name Already Taken")
            else:
                sub.add_playlist(pname)
        except Exception as e:
            print(e)
        sub_menu(sub)
    # remove playlist
    elif user_in == "ap":
        input_pname = input("Enter Playlist name:")
        try:
            if len(mycursor.execute("select pid from Playlist where pname==%(pname)s", (pname))) == 0:
                print("No Such Playlist")
            else:
                sub.remove_playlist(pname)
        except Exception as e:
            print(e)
        sub_menu(sub)
    # search songs
    elif user_in == "s":
        search()
        sub_menu(sub)
    # search artists
    elif user_in == "sa"
        a_search()
        sub_menu(sub)
    # view artist home page
    elif user_in == "A":
        aname = input ("Enter Artist Name: ")
        try:
            aid = mycursor.execute("select aid from Artist where aname==%(aname)s", (aname))
            artist = Artist(aid, mycursor)
            artist_home(sub, artist, aname, aid)
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
        print("Command Not Found")
        sub_menu(sub)

    
def artist_menu(artist):
    print('=== Artist Menu ===\n')
    print("I - Info\nSL - Song List\nSI - Song Info\nA - Add Song\nR - Remove Song\nB - Back To Login\nX - Close Application\n" )
    user_in = input("Input  Command: ")
    user_in = user_in.lower()
    if user_in == "I":
        aritist.info()
    elif user_in == "sl":
        artist.songs()
    elif user_in == "si":
        input_sname = input("Enter song name:")
        try:
            s_id =  mycursor.execute("select sid from Song where sname==%(input_sname)s", (input_sname))
            artist.song_info()
        except Exception:
            print("Song Not Found")
    elif user_in == "a":
        input_sname = input("Enter song name:")
        try:
            artist.add(input_sname)
        except Exception:
            print("Invalid Song Name")
    elif user_in == "r":
        input_sname = input("Enter song name:")
        try:
            s_id =  mycursor.execute("select sid from Song where sname==%(input_sname)s", (input_sname))
            try:
                artist.song_info()
            except Exception as e:
                print(e)
        except Exception:
            print("Song Not Found")
    elif user_in == "b":
        start()
    elif user_in == "x":
        print("Stopping")
    else:
        print("Command Not Found")
        artist_menu(artist)
    
def artist_start():
    aname = input("Log In With Username: ")
    a_id =  mycursor.execute("select subid from Subscriber where subname==%(aname)s", (aname))
    artist = Artist(a_id, mycursor)
    artist_menu(artist)
    
def sub_start():
    sname = input("Log In With Username: ")
    sub_id =  mycursor.execute("select subid from Subscriber where subname==%(subname)s", (subname))
    sub = Subscriber(sub_id, mycursor)
    sub_menu(sub)

def start():
    print("========== Welcome To Not Spotify ==========")
    login_type = input("Type S for Subscriber login or A for Artist Login: ")
    login_type = login_type.lower()
    if login_type == "a":
        artist_start()
    else if login_type == "s":
        sub_start()
    else:
        print("Unkown input")
        start()


if __name__ == "__main__": 
    try:
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="nimitchell220",
          use_pure=True
          )
        mycursor = mydb.cursor()
        try:
            mycursor.execute('USE final_project;')
        except Exception:
            file = open('final_project_schema.sql', 'r')
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
        start()
    except Exception as exc:
        print(exc)