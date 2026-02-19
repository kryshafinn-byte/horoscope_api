CREATE DATABASE horoscope_api;
USE horoscope_api;

CREATE TABLE signs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    date_range VARCHAR(50) NOT NULL,
    element VARCHAR(20) NOT NULL
);

CREATE TABLE lucky_colours (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sign_name VARCHAR(50) NOT NULL,
    colour1 VARCHAR(50) NOT NULL,
    colour2 VARCHAR(50) NOT NULL,
    colour3 VARCHAR(50) NOT NULL
);


CREATE TABLE compatibility (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sign_name VARCHAR(50) NOT NULL,
    compatible_with VARCHAR(50) NOT NULL
);

INSERT INTO signs (name, date_range, element) VALUES
('Aries', 'March 21 - April 19', 'Fire'),
('Taurus', 'April 20 - May 20', 'Earth'),
('Gemini', 'May 21 - June 20', 'Air'),
('Cancer', 'June 21 - July 22', 'Water'),
('Leo', 'July 23 - August 22', 'Fire'),
('Virgo', 'August 23 - September 22', 'Earth'),
('Libra', 'September 23 - October 22', 'Air'),
('Scorpio', 'October 23 - November 21', 'Water'),
('Sagittarius', 'November 22 - December 21', 'Fire'),
('Capricorn', 'December 22 - January 19', 'Earth'),
('Aquarius', 'January 20 - February 18', 'Air'),
('Pisces', 'February 19 - March 20', 'Water');
