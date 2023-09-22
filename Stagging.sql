
CREATE TABLE IF NOT EXISTS football_matchs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date_time DATE,
    region VARCHAR(255),
    tournament VARCHAR(255),
    matchday VARCHAR(255) NULL DEFAULT NULL,
    league_href VARCHAR(255) NULL DEFAULT NULL,
    begin_time TIME NULL DEFAULT NULL,
    first_team VARCHAR(255),
    second_team VARCHAR(255),
    full_match_goals VARCHAR(10) NULL DEFAULT NULL,
    half_match_goals VARCHAR(10) NULL DEFAULT NULL,
    first_team_goals INT NULL DEFAULT NULL,
    second_team_goals INT NULL DEFAULT NULL,
    match_href VARCHAR(255) NULL DEFAULT NULL
);
INSERT INTO football_matchs (date_time, region, tournament, matchday, league_href, begin_time, first_team, second_team, full_match_goals, half_match_goals, first_team_goals, second_team_goals, match_href)
VALUES ('{date_time}', '{region}', '{tournament}', '{matchday}', '{league_href}', '{begin_time}', '{first_team}', '{second_team}', '{full_match_goals}', '{half_match_goals}', '{first_team_goals}', '{second_team_goals}', '{match_href}');

UPDATE football_matchs
SET full_match_goals = '{full_match_goals}', half_match_goals = '{half_match_goals}', first_team_goals = '{first_team_goals}', second_team_goals = '{second_team_goals}', match_href = '{match_href}'
WHERE region = '{region}' AND tournament = '{tournament}' AND begin_time = '{begin_time}' AND first_team = '{first_team}' AND second_team = '{second_team}';

SELECT COUNT(*) FROM football_matchs
WHERE date_time = '{date_time}';