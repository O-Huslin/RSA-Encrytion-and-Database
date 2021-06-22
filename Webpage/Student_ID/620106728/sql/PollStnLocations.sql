USE VoteLogDB;
CREATE TABLE Polling_Station_Locations (
   id INT AUTO_INCREMENT,
   poll_division_id INT,
   polling_station VARCHAR(8),
   polling_station_loc VARCHAR(64),
   PRIMARY KEY(id));
