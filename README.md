### ELO


- To Submit results:
```python
python3 main.py --game "chess" --player1 "dean" --player2 "eid" --score 0.0
```
where player1 is considered white, and score is the score from perspective of player1 (ie 0.0 means player1 lost).

- To graph rating progression use:
```python
python3 graph.py "chess/eid.csv" "chess/anthony.csv" "chess/dean.csv"
```
where the resulting graph will be ratings.png.

New games/players can be added via
```python
python3 new_player.py
```
where one should first edit the new_player.py specifying which new players are being added and for what game. 
Each already specified game-player pair shall reset the statistics for that player.
