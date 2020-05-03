CREATE DATABASE if not exists FINAL_PROJECT;
USE FINAL_PROJECT;



create table if not exists Subscriber (
	subID int primary key,
	subName varchar(50)
);

create table if not exists Artist (
	aID int primary key,
	aName varchar(50)
);

create table if not exists Playlist (
	pID int primary key,
    subID int,
	pName varchar(50),
    privacy boolean,
    FOREIGN KEY (subID) REFERENCES Subscriber(subID)
);

create table if not exists Song (
	sID int primary key,
    aid int,
    sName varchar(50),
    publish_date date,
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
	sid int,
    pid int,
	PRIMARY KEY (sID, pID),
	FOREIGN KEY (sID) REFERENCES Song(sID),
    FOREIGN KEY (pID) REFERENCES Playlist(pID)
    );
    

insert into Subscriber values (1, 'Nicholas Mitchell');
insert into Subscriber values (2, 'AvaHayako');
insert into Subscriber values (3, 'MaryMoki');
insert into Subscriber values (4, 'Johnny AppleSeed');

insert into Artist values (101, 'San Holo');
insert into Artist values (102, 'Raveena Aurora');

insert into Playlist values(110, 1, 'Liked', False);
insert into Playlist values(120, 2, 'Happy Songs', False);
insert into Playlist values(130, 3, 'Liked', True);
insert into Playlist values(140, 4, 'Upbeat', False);

insert into Song values(111, 102, 'Sweet Time', 06/10/2018);
insert into Song values(112, 102, 'Stronger', 07/15/2019);
insert into Song values(113, 102, 'Petal', 07/15/2019);
insert into Song values(114, 101, 'We Rise', 06/15/2015);
insert into Song values(115, 101, 'lift me from the ground', 03/11/2018);
insert into Song values(116, 101, 'I Still See Your Face', 04/15/2017);



insert into Follow values(1, 101);
insert into Follow values(2,102);

insert into Is_on values (111,120);
insert into Is_on values (112,120);
insert into Is_on values (113,120);