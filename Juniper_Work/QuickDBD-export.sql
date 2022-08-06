-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE `Artists` (
    `id` varchar  NOT NULL ,
    `followers` float  NOT NULL ,
    `genres` varchar  NOT NULL ,
    `name` varchar  NOT NULL ,
    `popularity` int  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `Tracks` (
    `id` varchar  NOT NULL ,
    `name` varchar  NOT NULL ,
    `popularity` int  NOT NULL ,
    `duration_ms` int  NOT NULL ,
    `explicit` int  NOT NULL ,
    `artists` varchar  NOT NULL ,
    `id_artists` varchar  NOT NULL ,
    `release_date` date  NOT NULL ,
    `danceability` float  NOT NULL ,
    `energy` float  NOT NULL ,
    `key` int  NOT NULL ,
    `loudness` float  NOT NULL ,
    `mode` int  NOT NULL ,
    `speechiness` float  NOT NULL ,
    `acousticness` float  NOT NULL ,
    `instrumentalness` float  NOT NULL ,
    `liveness` float  NOT NULL ,
    `valencetempo` float  NOT NULL ,
    `time_signature` int  NOT NULL 
);

