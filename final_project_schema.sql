CREATE DATABASE if not exists FINAL_PROJECT;
USE FINAL_PROJECT;

create table Subscriber (
	subID int primary key,
	subName varchar(50)
);

create table Artist (
	aID int primary key,
	aName varchar(50)
);

create table Playlist (
	pID int primary key,
    subID int,
	pName int,
    privacy boolean,
    FOREIGN KEY (subID) REFERENCES Subscriber(subID)
);
    
create table Song (
	sID int primary key,
    aid int,
    sName varchar(50),
    FOREIGN KEY (aID) REFERENCES Artist(aID)
    );

 create table Follow (
	subID int,
    aid int,
 	PRIMARY KEY(subID, aID),
	FOREIGN KEY (subID) REFERENCES Subscriber(subID),
	FOREIGN KEY (aID) REFERENCES Artist(aID)
);

create table Is_On (
	sid int,
    pid int,
	PRIMARY KEY (sID, pID),
	FOREIGN KEY (sID) REFERENCES Song(sID),
    FOREIGN KEY (pID) REFERENCES Playlist(pID)
    );
    

insert into Subscriber values (1, 'Nicholas');
 