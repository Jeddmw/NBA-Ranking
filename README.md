# NBA Rankings

Uses method described [here](http://blog.biophysengr.net/2012/03/eigenbracket-2012-using-graph-theory-to.html) to rank NBA teams.

Data is extracted from landofbasketball.com.

In order to run this program download the [BeautifulSoup library](https://www.crummy.com/software/BeautifulSoup/?), the [Networkx library](https://networkx.github.io/documentation/latest/install.html), and the [requests library](http://docs.python-requests.org/en/master/user/install/).

This program also requires [PostgreSQL](https://www.postgresql.org/download/); after download, create a database named "nbarankings" and a table named "rankings" with columns "year", "team", and "score", with types VARCHAR(10), VARCHAR(50), and float.

To run from command line:
```
python NBARanking.py
```

Example data for query -> "SELECT * from rankings WHERE year = 2017_2018" (2017-2018 season):
```
year          team                          score    
"2017_2018"   "Boston Celtics"              0.22
"2017_2018"   "Golden State Warriors"       0.22
"2017_2018"   "Houston Rockets"             0.22
"2017_2018"   "Minnesota Timberwolves"      0.209999999999999
"2017_2018"   "New Orleans Pelicans"        0.209999999999999
"2017_2018"   "Oklahoma City Thunder"       0.209999999999999
"2017_2018"   "Philadelphia 76ers"          0.209999999999999
"2017_2018"   "Toronto Raptors"             0.209999999999999
"2017_2018"   "Washington Wizards"          0.209999999999999
"2017_2018"   "Cleveland Cavaliers"         0.2
"2017_2018"   "Denver Nuggets"              0.2
"2017_2018"   "Portland Trail Blazers"      0.2
"2017_2018"   "San Antonio Spurs"           0.2
"2017_2018"   "Utah Jazz"                   0.2
"2017_2018"   "Detroit Pistons"             0.19
"2017_2018"   "Indiana Pacers"              0.19
"2017_2018"   "Los Angeles Clippers"        0.19
"2017_2018"   "Milwaukee Bucks"             0.19
"2017_2018"   "Los Angeles Lakers"          0.17
"2017_2018"   "Miami Heat"                  0.17
"2017_2018"   "New York Knicks"             0.16
"2017_2018"   "Atlanta Hawks"               0.149999999999999
"2017_2018"   "Charlotte Hornets"           0.149999999999999
"2017_2018"   "Dallas Mavericks"            0.14
"2017_2018"   "Sacramento Kings"            0.14
"2017_2018"   "Brooklyn Nets"               0.13
"2017_2018"   "Orlando Magic"               0.13
"2017_2018"   "Chicago Bulls"               0.12
"2017_2018"   "Memphis Grizzlies"           0.12
"2017_2018"   "Phoenix Suns"                0.1

```

Ranking is based on every game played by each team, including the playoffs/finals.

Everything is inserted into a PostgreSQL database.
