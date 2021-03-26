SELECT * FROM players;

SELECT * FROM seasons_stats;

SELECT id, player, height, weight, college, born, position, tm
FROM players
INNER JOIN seasons_stats on 
players.id = seasons_stats.player_id
and id in (0,1,2);