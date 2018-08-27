# NBA Rankings

Uses method described [here](http://blog.biophysengr.net/2012/03/eigenbracket-2012-using-graph-theory-to.html) to rank NBA teams.

Data is extracted from landofbasketball.com.

In order to run this program download the [BeautifulSoup library](https://www.crummy.com/software/BeautifulSoup/?), the [Networkx library](https://networkx.github.io/documentation/latest/install.html), and the [requests library](http://docs.python-requests.org/en/master/user/install/).

To run from command line:
```
python NBARankings.py
```

Example output for 2017-2018 season:
```
 1. Boston Celtics-----------------------------Score: 0.22
 2. Golden State Warriors----------------------Score: 0.22
 3. Houston Rockets----------------------------Score: 0.22
 4. Minnesota Timberwolves---------------------Score: 0.21
 5. New Orleans Pelicans-----------------------Score: 0.21
 6. Oklahoma City Thunder----------------------Score: 0.21
 7. Philadelphia 76ers-------------------------Score: 0.21
 8. Toronto Raptors----------------------------Score: 0.21
 9. Washington Wizards-------------------------Score: 0.21
10. Cleveland Cavaliers------------------------Score: 0.20
11. Denver Nuggets-----------------------------Score: 0.20
12. Portland Trail Blazers---------------------Score: 0.20
13. San Antonio Spurs--------------------------Score: 0.20
14. Utah Jazz----------------------------------Score: 0.20
15. Detroit Pistons----------------------------Score: 0.19
16. Indiana Pacers-----------------------------Score: 0.19
17. Los Angeles Clippers-----------------------Score: 0.19
18. Milwaukee Bucks----------------------------Score: 0.19
19. Los Angeles Lakers-------------------------Score: 0.17
20. Miami Heat---------------------------------Score: 0.17
21. New York Knicks----------------------------Score: 0.16
22. Atlanta Hawks------------------------------Score: 0.15
23. Charlotte Hornets--------------------------Score: 0.15
24. Dallas Mavericks---------------------------Score: 0.14
25. Sacramento Kings---------------------------Score: 0.14
26. Brooklyn Nets------------------------------Score: 0.13
27. Orlando Magic------------------------------Score: 0.13
28. Chicago Bulls------------------------------Score: 0.12
29. Memphis Grizzlies--------------------------Score: 0.12
30. Phoenix Suns-------------------------------Score: 0.10

```

Ranking is based on every game played by each team, including the playoffs/finals.
