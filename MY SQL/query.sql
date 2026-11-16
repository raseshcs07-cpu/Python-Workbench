CREATE TABLE movies(
    id    INTEGER PRIMARY KEY,
    name  VARCHAR(255) NOT NULL,
    genre  VARCHAR(50),
    year   INTEGER,
    imbd_rating  DECIMAL(3,1)
);

ALTER TABLE movies
RENAME COLUMN imbd_rating TO imdb_rating;

INSERT INTO movies (id, name, genre, year, imdb_rating) 
VALUES
(1, 'Avatar', 'action', 2009, 7.9),
(2, 'Jurassic World', 'action', 2015, 7.3),
(3, 'The Avengers', 'action', 2012, 8.1),
(4, 'The Dark Knight', 'action', 2008, 9.0),
(5, 'Star Wars: Episode I - The Phantom Menace', 'action', 1999, 6.6),
(6, 'Star Wars', 'action', 1977, 8.7),
(7, 'Avengers: Age of Ultron', 'action', 2015, 7.9),
(8, 'The Dark Knight Rises', 'action', 2012, 8.5),
(9, 'Pirates of the Caribbean: Dead Mans Chest', 'action', 2006, 7.3),
(10, 'Iron Man 3', 'action', 2013, 7.3),
(11, 'Spider-Man', 'action', 2002, 7.3),
(12, 'Transformers: Revenge of the Fallen', 'action', 2009, 6.0),
(13, 'Star Wars: Episode III - Revenge of the Sith', 'action', 2005, 7.7),
(14, 'Spider-Man 2', 'action', 2004, 7.3),
(15, 'Transformers: Dark of the Moon', 'action', 2011, 6.3),
(16, 'American Sniper', 'action', 2014, 7.4),
(17, 'Furious Seven', 'action', 2015, 7.4),
(18, 'Spider-Man 3', 'action', 2007, 6.2),
(19, 'Guardians of the Galaxy', 'action', 2014, 8.1),
(20, 'Transformers', 'action', 2007, 7.1),
(21, 'Iron Man', 'action', 2008, 7.9),
(22, 'Indiana Jones and the Kingdom of the Crystal Skull', 'action', 2008, 6.2),
(23, 'Iron Man 2', 'action', 2010, 7.1),
(24, 'Star Wars: Episode II - Attack of the Clones', 'action', 2002, 6.7),
(25, 'Pirates of the Caribbean: At Worlds End', 'action', 2007, 7.1),
(26, 'Star Wars: Episode VI - Return of the Jedi', 'action', 1983, 8.4),
(27, 'Independence Day', 'action', 1996, 6.9),
(28, 'Pirates of the Caribbean: The Curse of the Black Pearl', 'action', 2003, 8.1),
(29, 'Skyfall', 'action', 2012, 7.8),
(30, 'Inception', 'action', 2010, 8.8),
(31, 'Man of Steel', 'action', 2013, 7.2),
(32, 'Star Wars: Episode V - The Empire Strikes Back', 'action', 1980, 8.8),
(33, 'The Matrix Reloaded', 'action', 2003, 7.2),
(34, 'The Amazing Spider-Man', 'action', 2012, 7.1),
(35, 'The Incredibles', 'action', 2004, 8.0),
(36, 'Captain America: The Winter Soldier', 'action', 2014, 7.8),
(37, 'The Lego Movie', 'action', 2014, 7.8),
(38, 'Star Trek', 'action', 2009, 8.0),
(39, 'Batman', 'action', 1989, 7.6),
(40, 'Night at the Museum', 'action', 2006, 6.4),
(41, 'Transformers: Age of Extinction', 'action', 2014, 5.8),
(42, 'Twister', 'action', 1996, 6.3),
(43, 'Maleficent', 'action', 2014, 7.0),
(44, 'Pirates of the Caribbean: On Stranger Tides', 'action', 2011, 6.7),
(45, 'Fast & Furious 6', 'action', 2013, 7.2),
(46, 'Beverly Hills Cop', 'action', 1984, 7.3),
(47, 'X-Men: The Last Stand', 'action', 2006, 6.8),
(48, 'X-Men: Days of Future Past', 'action', 2014, 8.1),
(49, 'The Lost World: Jurassic Park', 'action', 1997, 6.5),
(50, 'Star Trek Into Darkness', 'action', 2013, 7.8),
(51, 'Shrek 2', 'comedy', 2004, 7.2),
(52, 'Toy Story 3', 'comedy', 2010, 8.4),
(53, 'Frozen', 'comedy', 2013, 7.6),
(54, 'Finding Nemo', 'comedy', 2003, 8.2),
(55, 'Despicable Me 2', 'comedy', 2013, 7.5),
(56, 'Inside Out', 'comedy', 2015, 8.6),
(57, 'Shrek the Third', 'comedy', 2007, 6.0),
(58, 'Minions', 'comedy', 2015, 6.7),
(59, 'Up', 'comedy', 2009, 8.3),
(60, 'Monsters, Inc.', 'comedy', 2001, 8.1),
(61, 'Home Alone', 'comedy', 1990, 7.4),
(62, 'Meet the Fockers', 'comedy', 2004, 6.3),
(63, 'The Hangover', 'comedy', 2009, 7.8),
(64, 'Monsters University', 'comedy', 2013, 7.4),
(65, 'Shrek', 'comedy', 2001, 7.9),
(66, 'How the Grinch Stole Christmas', 'comedy', 2000, 6.0),
(67, 'The Hangover Part II', 'comedy', 2011, 6.5),
(68, 'Despicable Me', 'comedy', 2010, 7.7),
(69, 'Men in Black', 'comedy', 1997, 7.2),
(70, 'Toy Story 2', 'comedy', 1999, 7.9),
(71, 'Cars', 'comedy', 2006, 7.2),
(72, 'Bruce Almighty', 'comedy', 2003, 6.7),
(73, 'My Big Fat Greek Wedding', 'comedy', 2002, 6.6),
(74, 'Shrek Forever After', 'comedy', 2010, 6.4),
(75, 'Brave', 'comedy', 2012, 7.2),
(76, 'Ghostbusters', 'comedy', 1984, 7.8),
(77, 'Rush Hour 2', 'comedy', 2001, 6.6),
(78, 'Big Hero 6', 'comedy', 2014, 7.9),
(79, 'Alvin and the Chipmunks: The Squeakquel', 'comedy', 2009, 4.4),
(80, 'Mrs. Doubtfire', 'comedy', 1993, 6.9),
(81, 'Ted', 'comedy', 2012, 7.0),
(82, 'Aladdin', 'comedy', 1992, 8.0),
(83, 'Alvin and the Chipmunks', 'comedy', 2007, 5.3),
(84, 'Madagascar 3: Europes Most Wanted', 'comedy', 2012, 7.0),
(85, 'Kung Fu Panda', 'comedy', 2008, 7.6),
(86, 'The Lorax', 'comedy', 2012, 6.5),
(87, 'Austin Powers in Goldmember', 'comedy', 2002, 6.2),
(88, 'Back to the Future', 'comedy', 1985, 8.5),
(89, 'Wedding Crashers', 'comedy', 2005, 7.0),
(90, 'Charlie and the Chocolate Factory', 'comedy', 2005, 6.7),
(91, 'Ratatouille', 'comedy', 2007, 8.0),
(92, 'Austin Powers: The Spy Who Shagged Me', 'comedy', 1999, 6.6),
(93, 'Tangled', 'comedy', 2010, 7.8),
(94, 'Monsters vs. Aliens', 'comedy', 2009, 6.6),
(95, 'Happy Feet', 'comedy', 2006, 6.5),
(96, 'Ice Age: Dawn of the Dinosaurs', 'comedy', 2009, 7.0),
(97, 'Ice Age: The Meltdown', 'comedy', 2006, 6.9),
(98, 'World War Z', 'horror', 2013, 7.0),
(99, 'What Lies Beneath', 'horror', 2000, 6.6),
(100, 'Gremlins', 'horror', 1984, 7.2),
(101, 'The Blair Witch Project', 'horror', 1999, 6.4),
(102, 'The Conjuring', 'horror', 2013, 7.5),
(103, 'The Ring', 'horror', 2002, 7.1),
(104, 'The Grudge', 'horror', 2004, 5.9),
(105, 'Paranormal Activity', 'horror', 2007, 6.3),
(106, 'Interview with the Vampire: The Vampire Chronicles', 'horror', 1994, 7.6),
(107, 'Paranormal Activity 3', 'horror', 2011, 5.9),
(108, 'Scream', 'horror', 1996, 7.2),
(109, 'Jaws 2', 'horror', 1978, 5.7),
(110, 'Scream 2', 'horror', 1997, 6.1),
(111, 'Sleepy Hollow', 'horror', 1999, 7.4),
(112, 'The Others', 'horror', 2001, 7.6),
(113, 'The Haunting', 'horror', 1999, 4.9),
(114, 'Scream 3', 'horror', 2000, 5.5),
(115, 'Saw II', 'horror', 2005, 6.6),
(116, 'The Amityville Horror', 'horror', 1979, 6.2),
(117, 'Aliens', 'horror', 1986, 8.4),
(118, 'Paranormal Activity 2', 'horror', 2010, 5.7),
(119, 'Annabelle', 'horror', 2014, 5.4),
(120, 'Scooby-Doo 2: Monsters Unleashed', 'horror', 2004, 4.9),
(121, 'Insidious: Chapter 2', 'horror', 2013, 6.6),
(122, 'Dracula', 'horror', 1992, 7.5),
(123, 'Freddy vs. Jason', 'horror', 2003, 5.8),
(124, 'Blade II', 'horror', 2002, 6.7),
(125, 'Saw III', 'horror', 2006, 6.2),
(126, 'The Texas Chainsaw Massacre', 'horror', 2003, 6.2),
(127, 'Cloverfield', 'horror', 2008, 7.1),
(128, 'Dark Shadows', 'horror', 2012, 6.2),
(129, 'The Ring Two', 'horror', 2005, 5.4),
(130, 'Zombieland', 'horror', 2009, 7.7),
(131, 'Constantine', 'horror', 2005, 6.9),
(132, 'The Exorcism of Emily Rose', 'horror', 2005, 6.7),
(133, 'I Know What You Did Last Summer', 'horror', 1997, 5.6),
(134, '1408', 'horror', 2007, 6.8),
(135, 'Mama', 'horror', 2013, 6.2),
(136, 'The Purge: Anarchy', 'horror', 2014, 6.5),
(137, 'Scary Movie 2', 'horror', 2001, 5.2),
(138, 'Blade', 'horror', 1998, 7.1),
(139, 'End of Days', 'horror', 1999, 5.7),
(140, 'The Forgotten', 'horror', 2004, 5.8),
(141, 'The Final Destination', 'horror', 2009, 5.2),
(142, 'Warm Bodies', 'horror', 2013, 6.9),
(143, 'Anaconda', 'horror', 1997, 4.6),
(144, 'Wolf', 'horror', 1994, 6.2),
(145, 'Friday the 13th', 'horror', 2009, 5.6),
(146, 'The Purge', 'horror', 2013, 5.6),
(147, 'Titanic', 'romance', 1997, 7.7),
(148, 'Forrest Gump', 'romance', 1994, 8.8),
(149, 'The Twilight Saga: Eclipse', 'romance', 2010, 4.9),
(150, 'The Twilight Saga: New Moon', 'romance', 2009, 4.6),
(151, 'The Twilight Saga: Breaking Dawn - Part 2', 'romance', 2012, 5.6),
(152, 'The Twilight Saga: Breaking Dawn - Part 1', 'romance', 2011, 4.9),
(153, 'Beauty and the Beast', 'romance', 1991, 8.0),
(154, 'King Kong', 'romance', 2005, 7.3),
(155, 'Ghost', 'romance', 1990, 7.0),
(156, 'Cinderella', 'romance', 2015, 7.1),
(157, 'Gone with the Wind', 'romance', 1939, 8.2),
(158, 'Pearl Harbor', 'romance', 2001, 6.0),
(159, 'Twilight', 'romance', 2008, 5.2),
(160, 'Mr. & Mrs. Smith', 'romance', 2005, 6.5),
(161, 'Snow White and the Seven Dwarfs', 'romance', 1937, 7.7),
(162, 'What Women Want', 'romance', 2000, 6.4),
(163, 'Top Gun', 'romance', 1986, 6.8),
(164, 'Pretty Woman', 'romance', 1990, 6.9),
(165, 'Hitch', 'romance', 2005, 6.7),
(166, 'Tootsie', 'romance', 1982, 7.4),
(167, 'Theres Something About Mary', 'romance', 1998, 7.1),
(168, 'Elf', 'romance', 2003, 6.9),
(169, 'Tarzan', 'romance', 1999, 7.2),
(170, 'Bridesmaids', 'romance', 2011, 6.8),
(171, 'Fifty Shades of Grey', 'romance', 2015, 4.2),
(172, 'Robin Hood: Prince of Thieves', 'romance', 1991, 6.9),
(173, 'The Proposal', 'romance', 2009, 6.7),
(174, 'The Sound of Music', 'romance', 1965, 8.0),
(175, 'Jerry Maguire', 'romance', 1996, 7.3),
(176, 'Sex and the City', 'romance', 2008, 5.5),
(177, 'Runaway Bride', 'romance', 1999, 5.4),
(178, 'Les Misérables', 'romance', 2012, 7.6),
(179, 'Knocked Up', 'romance', 2007, 7.1),
(180, 'Little Fockers', 'romance', 2010, 5.5),
(181, 'As Good as It Gets', 'romance', 1997, 7.8),
(182, 'American Pie 2', 'romance', 2001, 6.4),
(183, 'The Great Gatsby', 'romance', 2013, 7.3),
(184, 'Mamma Mia!', 'romance', 2008, 6.4),
(185, 'Juno', 'romance', 2007, 7.5),
(186, 'Marley & Me', 'romance', 2008, 7.1),
(187, 'Pocahontas', 'romance', 1995, 6.6),
(188, 'Slumdog Millionaire', 'romance', 2008, 8.0),
(189, 'Look Whos Talking', 'romance', 1989, 5.8),
(190, 'Click', 'romance', 2006, 6.4),
(191, 'The Lion King', 'drama', 1994, 8.5),
(192, 'Harry Potter and the Deathly Hallows: Part 2', 'drama', 2011, 8.1),
(193, 'The Sixth Sense', 'drama', 1999, 8.2),
(194, 'Jaws', 'drama', 1975, 8.1),
(195, 'I Am Legend', 'drama', 2007, 7.2),
(196, 'The Blind Side', 'drama', 2009, 7.7),
(197, 'Cast Away', 'drama', 2000, 7.7),
(198, 'Signs', 'drama', 2002, 6.7),
(199, 'Saving Private Ryan', 'drama', 1998, 8.6),
(200, 'Dawn of the Planet of the Apes', 'drama', 2014, 7.7),
(201, 'Interstellar', 'drama', 2014, 8.7),
(202, 'Gladiator', 'drama', 2000, 8.5),
(203, 'Dances with Wolves', 'drama', 1990, 8.0),
(204, 'The Perfect Storm', 'drama', 2000, 6.4),
(205, 'Lincoln', 'drama', 2012, 7.4),
(206, 'Rise of the Planet of the Apes', 'drama', 2011, 7.6),
(207, 'The Karate Kid', 'drama', 2010, 6.2),
(208, 'Rain Man', 'drama', 1988, 8.0),
(209, 'Air Force One', 'drama', 1997, 6.4),
(210, 'True Grit', 'drama', 2010, 7.7),
(211, 'A Beautiful Mind', 'drama', 2001, 8.2),
(212, 'The Help', 'drama', 2011, 8.1),
(213, '3 Men and a Baby', 'drama', 1987, 5.9),
(214, 'Gone Girl', 'drama', 2014, 8.2),
(215, 'Kung Fu Panda 2', 'drama', 2011, 7.3),
(216, 'Hannibal', 'drama', 2001, 6.7),
(217, 'Catch Me If You Can', 'drama', 2002, 8.0),
(218, 'Big Daddy', 'drama', 1999, 6.4),
(219, 'Se7en', 'drama', 1995, 8.6),
(220, 'Seven', 'drama', 1979, 6.1),
(221, 'The Good, the Bad and the Ugly', 'action', 1966, 8.8),
(222, 'Dawn of the Dead', 'horror', 1978, 7.8),
(223, 'Shaun of the Dead', 'comedy', 2004, 7.9),
(224, 'Star Wars: The Force Awakens', 'action', 2015, 8.1),
(225, 'Star Wars: The Last Jedi', 'action', 2017, 6.9),
(226, 'The Shining', 'horror', 1985, 8.4),
(227, 'The Devil and Daniel Johnston', NULL, 2005, 8.0),
(228, 'Ali Wong: Baby Cobra', 'comedy', 2016, 7.5),
(229, 'The Big Sick', 'romance', 2017, 7.5),
(230, 'Deadpool', 'action', 2016, 8.0),
(231, 'Avengers: Infinity War', 'action', 2018, 8.4),
(232, 'Black Panther', 'action', 2018, 7.3),
(233, 'Avengers: Endgame', 'action', 2019, 8.4),
(234, 'Top Gun: Maverick', 'action', 2022, 8.2),
(235, 'Spider-Man: Across the Spider-Verse', 'action', 2023, 8.6),
(236, 'John Wick: Chapter 4', 'action', 2023, 7.6),
(237, 'Mission: Impossible - Dead Reckoning Part One', 'action', 2023, 7.6),
(238, 'Dune: Part Two', 'action', 2024, 8.5),
(239, 'Furiosa: A Mad Max Saga', 'action', 2024, 7.5),
(240, 'Deadpool & Wolverine', 'action', 2024, 7.5),
(241, 'Mission: Impossible - The Final Reckoning', 'action', 2025, 7.2),
(242, 'Thunderbolts\*', 'action', 2025, 7.1),
(243, 'Superman', 'action', 2025, 7.0),
(244, 'One Battle After Another', 'action', 2025, 7.7),
(245, 'Toy Story 4', 'comedy', 2019, 7.6),
(246, 'Knives Out', 'comedy', 2019, 7.9),
(247, 'Jojo Rabbit', 'comedy', 2019, 7.9),
(248, 'Palm Springs', 'comedy', 2020, 7.4),
(249, 'Free Guy', 'comedy', 2021, 7.1),
(250, 'The Mitchells vs. the Machines', 'comedy', 2021, 7.6),
(251, 'Everything Everywhere All at Once', 'comedy', 2022, 7.7),
(252, 'The Banshees of Inisherin', 'comedy', 2022, 7.6),
(253, 'Glass Onion: A Knives Out Mystery', 'comedy', 2022, 7.1),
(254, 'Barbie', 'comedy', 2023, 6.9),
(255, 'Dumb Money', 'comedy', 2023, 6.8),
(256, 'Anora', 'comedy', 2024, 7.4),
(257, 'The Naked Gun', 'comedy', 2025, 6.3),
(258, 'Midsommar', 'horror', 2019, 7.1),
(259, 'Ready or Not', 'horror', 2019, 6.9),
(260, 'The Lighthouse', 'horror', 2019, 7.4),
(261, 'A Quiet Place Part II', 'horror', 2020, 7.2),
(262, 'Candyman', 'horror', 2021, 5.9),
(263, 'The Black Phone', 'horror', 2021, 6.9),
(264, 'Barbarian', 'horror', 2022, 7.0),
(265, 'Smile', 'horror', 2022, 6.5),
(266, 'Pearl', 'horror', 2022, 7.0),
(267, 'Talk to Me', 'horror', 2022, 7.1),
(268, 'Scream VI', 'horror', 2023, 6.4),
(269, 'Late Night with the Devil', 'horror', 2023, 7.0),
(270, 'The Substance', 'horror', 2024, 7.2),
(271, 'Bring Her Back', 'horror', 2025, 7.1),
(272, 'Crazy Rich Asians', 'romance', 2018, 6.9),
(273, 'To All the Boys I''ve Loved Before', 'romance', 2018, 7.5),
(274, 'A Star Is Born', 'romance', 2018, 8.0),
(275, 'Aladdin', 'romance', 2019, 6.9),
(276, 'Portrait of a Lady on Fire', 'romance', 2019, 7.8),
(277, 'Licorice Pizza', 'romance', 2021, 7.1),
(278, 'CODA', 'romance', 2021, 7.9),
(279, 'Red, White & Royal Blue', 'romance', 2023, 7.1),
(280, 'Poor Things', 'romance', 2023, 8.2),
(281, 'Past Lives', 'romance', 2023, 7.9),
(282, 'Elemental', 'romance', 2023, 7.3),
(283, 'The Idea of You', 'romance', 2024, 6.3),
(284, 'Wicked', 'romance', 2024, 7.3),
(285, 'The Fall Guy', 'romance', 2024, 7.3),
(286, 'Green Book', 'drama', 2018, 8.2),
(287, 'The Irishman', 'drama', 2019, 7.8),
(288, 'Joker', 'drama', 2019, 8.3),
(289, '1917', 'drama', 2019, 8.2),
(290, 'Nomadland', 'drama', 2021, 7.2),
(291, 'Judas and the Black Messiah', 'drama', 2021, 8.0),
(292, 'King Richard', 'drama', 2021, 7.6),
(293, 'The Whale', 'drama', 2022, 7.6),
(294, 'All Quiet on the Western Front', 'drama', 2022, 7.8),
(295, 'Oppenheimer', 'drama', 2023, 8.2),
(296, '12th Fail', 'drama', 2023, 8.7),
(297, 'Society of the Snow', 'drama', 2024, 7.8),
(298, 'Sinners', 'drama', 2025, 7.5),
(299, 'Hamnet', 'drama', 2025, 7.9),
(300, 'Nuremberg', 'drama', 2025, 7.4);

SELECT * FROM Movies;
SELECT name, genre FROM movies;

SELECT COUNT(*) AS total_movies FROM Movies;
SELECT name AS 'Titles' FROM movies;

SELECT DISTINCT year FROM movies;

SELECT * FROM movies WHERE imdb_rating > 8;
SELECT * FROM movies WHERE year > 2024;

SELECT * FROM movies WHERE name LIKE 'Se_en'
SELECT * FROM movies WHERE name LIKE 'A%';
SELECT * FROM movies WHERE name LIKE '%a';
SELECT * FROM movies WHERE name LIKE '%man%';
SELECT * FROM movies WHERE name LIKE 'The %';

SELECT name FROM movies WHERE imdb_rating IS NOT NULL;
SELECT name FROM movies WHERE imdb_rating IS NULL;

SELECT * FROM movies WHERE year BETWEEN 1990 AND 1999;
SELECT * FROM movies WHERE name BETWEEN 'A' AND 'J';
SELECT * FROM movies WHERE name BETWEEN 'D'  AND 'G';
SELECT * FROM movies WHERE year BETWEEN 1970  AND 1979;

SELECT * FROM movies WHERE year BETWEEN 1990 AND 1999 
   AND genre = 'romance';
SELECT * FROM movies WHERE year BETWEEN 1970 AND 1979
  AND imdb_rating > 8;
SELECT * FROM movies WHERE year < 1985
  AND genre = 'horror';

SELECT * FROM movies WHERE year > 2021
   OR genre = 'action';
SELECT * FROM movies WHERE genre = 'romance'
   OR genre = 'comedy';

SELECT * FROM movies ORDER BY name;
-- ascending order by default.
SELECT * FROM movies WHERE imdb_rating > 8 ORDER BY year DESC;
-- ASC
SELECT name, year,imdb_rating FROM movies ORDER BY imdb_rating DESC;

SELECT * FROM movies LIMIT 10;
SELECT * FROM movies  ORDER BY imdb_rating DESC LIMIT 3;

SELECT name, 
 CASE 
  WHEN imdb_rating > 8 THEN
'Fantastic'
  WHEN imdb_rating > 6 THEN 'Poorly Received'
  ELSE 'Avoid ay All Costs'
 END
FROM movies;

SELECT name,
 CASE
  WHEN imdb_rating > 8 THEN 'Fantastic'
  WHEN imdb_rating > 6 THEN 'Poorly Received'
  ELSE 'Avoid at All Costs'
 END AS 'Review'
FROM movies;

SELECT name,
 CASE
  WHEN genre = 'romance' THEN 'Chill'
  WHEN genre = 'comedy' THEN 'Chill'
  ELSE 'Intense'
 END AS 'Mood'
FROM movies;

WITH temporary_name AS (
   SELECT *
   FROM table_name)
SELECT *
FROM temporary_name
WHERE column_name operator value;

/*
SELECT
AS
DISTINCT
WHERE
LIKE 
BETWEEN
AND 
OR 
ORDER BY
LIMIT
CASE
with
*/


SELECT * FROM restaurants;
SELECT DISTINCT neighborhood FROM restaurants;
SELECT DISTINCT cuisine FROM restaurants;
SELECT * FROM restaurants WHERE cuisine = 'Chinese' ;
SELECT * FROM restaurants WHERE review > 4;
SELECT * FROM restaurants WHERE cuisine = 'Italian' AND price = '$$$';
SELECT * FROM restaurants WHERE name LIKE '%meatball%' ;
SELECT * FROM restaurants WHERE neighborhood = 'Midtown' OR neighborhood = 'Downtown' OR neighborhood = 'Chinatown';
SELECT * FROM restaurants WHERE health IS NULL;
SELECT * FROM restaurants  ORDER BY review DESC LIMIT 10;
SELECT review,
 CASE 
  WHEN review > 4.5 THEN 'Extraordinary'
  WHEN review > 4 THEN 'Excellent'
  WHEN review > 3 THEN 'Good '
  WHEN review > 2 THEN 'Fair  '
  ELSE 'Poor'
 END 'markup'
FROM restaurants