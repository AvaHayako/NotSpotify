CREATE DATABASE if not exists FINAL_PROJECT;
USE FINAL_PROJECT;

create table if not exists Subscriber (
	subID int primary key,
	subName varchar(50)
);

create table if not exists Artist (
	aID int primary key,
	aName varchar(50),
    follower_count int DEFAULT 0
);

create table if not exists Playlist (
	pID varchar(50) primary key,
    subID int,
	pName varchar(50),
    privacy boolean,
    FOREIGN KEY (subID) REFERENCES Subscriber(subID)
);

create table if not exists Song (
	sID varchar(50) primary key,
    aID int,
    sName varchar(50),
    publish_date date,
    like_count int DEFAULT 0,
    FOREIGN KEY (aID) REFERENCES Artist(aID)
    );

 create table if not exists Follow (
	subID int,
    aid int,
 	PRIMARY KEY(subID, aID),
	FOREIGN KEY (subID) REFERENCES Subscriber(subID),
	FOREIGN KEY (aID) REFERENCES Artist(aID)
);

create table if not exists Is_On (
	sid varchar(50),
    pid varchar(50),
	PRIMARY KEY (sID, pID),
	FOREIGN KEY (sID) REFERENCES Song(sID),
    FOREIGN KEY (pID) REFERENCES Playlist(pID)
    );
    

insert into Subscriber values (1, 'Nicholas Mitchell');
insert into Subscriber values (2, 'AvaHayako');
insert into Subscriber values (3, 'MaryMoki');
insert into Subscriber values (4, 'Johnny AppleSeed');

insert into Artist values (101, 'San Holo',0);
insert into Artist values (102, 'Raveena Aurora',0);

insert into Song values("102SweetTime", 102, 'Sweet Time', 06/10/2018, 0);
insert into Song values("102Stronger", 102, 'Stronger', 07/15/2019, 0);
insert into Song values("102Petal", 102, 'Petal', 07/15/2019, 0);
insert into Song values("101WeRise", 101, 'We Rise', 06/15/2015, 0);
insert into Song values("101liftmefromtheground", 101, 'lift me from the ground', 03/11/2018, 0);

