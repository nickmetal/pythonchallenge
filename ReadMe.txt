Features:
    - we can't create a player if no one team has been created
    - "team name" must equal to already existing team name
    - run server as http://localhost:8000/ for correct work with js


Use default database with:
    - login nba_admin
    - password nba12345


-/ ->

- GET /team/:teamId  -> http://localhost:8000/api/v1/team/1/ -> json data
- GET /player/:playerId -> http://localhost:8000/api/v1/player/1/ -> json data


- POST /team ->
curl -H "Content-Type: application/json" -X GET -d '{"name":"RedDevils","city":"NewYork"}' http://localhost:8000/api/v1/team/ ->
created a record in db or raise error if city is already exist


- POST /player ->
curl -H "Content-Type: application/json" -X POST -d '{"name":"nick jager","age":33,"team":"red","height":180,"experience":11,"goals":33}' http://localhost:8000/api/v1/player/  ->
created a record in db or raise error if player is already exist or team not created yet

