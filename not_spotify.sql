CREATE DATABASE if not exists NOT_SPOTIFY;
USE NOT_SPOTIFY;

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
    FOREIGN KEY (subID) REFERENCES Subscriber(subID) ON DELETE CASCADE
);

create table if not exists Song (
	sID varchar(50) primary key,
    aID int,
    sName varchar(50),
    publish_date date,
    like_count int DEFAULT 0,
    FOREIGN KEY (aID) REFERENCES Artist(aID) ON DELETE CASCADE
    );

 create table if not exists Follow (
	subID int,
    aID int,
 	PRIMARY KEY(subID, aID),
	FOREIGN KEY (subID) REFERENCES Subscriber(subID) ON DELETE CASCADE,
	FOREIGN KEY (aID) REFERENCES Artist(aID) ON DELETE CASCADE
);

create table if not exists Is_On (
	sID varchar(50),
    pID varchar(50),
	PRIMARY KEY (sID, pID),
	FOREIGN KEY (sID) REFERENCES Song(sID) ON DELETE CASCADE,
    FOREIGN KEY (pID) REFERENCES Playlist(pID) ON DELETE CASCADE
    );
    

insert into Subscriber values (1, 'Nicholas Mitchell');
insert into Subscriber values (2, 'AvaHayako');
insert into Subscriber values (3, 'MaryMoki');
insert into Subscriber values (4, 'Johnny AppleSeed');

insert into Artist values (101, 'San Holo',0);
insert into Artist values (102, 'Raveena Aurora',0);

insert into Song values('102SweetTime', 102, 'Sweet Time', '2018-06-10', 0);
insert into Song values('102Stronger', 102, 'Stronger', '2019-07-15', 0);
insert into Song values('102Petal', 102, 'Petal', '2019-07-15', 0);
insert into Song values('101WeRise', 101, 'We Rise', '2015-06-15', 0);


insert into Playlist values('2Happy', 2, 'Happy', False);
insert into Playlist values('3Boop', 3, 'Boop', False);
insert into Is_On values('102Stronger', '2Happy');
insert into Is_On values('102Stronger', '3Boop');
