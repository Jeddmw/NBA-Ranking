# NBA Rankings

Uses method described [here](http://blog.biophysengr.net/2012/03/eigenbracket-2012-using-graph-theory-to.html) to rank NBA teams.

Data is extracted from [landofbasketball.com](http://www.landofbasketball.com/).

In order to run this program download the [BeautifulSoup library](https://www.crummy.com/software/BeautifulSoup/?), the [Networkx library](https://networkx.github.io/documentation/latest/install.html), the [requests library](http://docs.python-requests.org/en/master/user/install/), and the [psycopg2 library](http://initd.org/psycopg/download/).

This program also requires [PostgreSQL](https://www.postgresql.org/download/); after download, create a database named "nbarankings" and a table named "rankings" with columns "year", "team", and "score", with types VARCHAR(10), VARCHAR(50), and float.

To run from command line:
```
python NBARanking.py
```

Example data for query -> "SELECT * FROM rankings WHERE year = '2017_2018'" (Rank every team from the 2017-2018 season):
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

Example data for query -> "SELECT * FROM rankings WHERE team = 'Los Angeles Lakers' ORDER BY score DESC" (Rank every Los Angeles Lakers team from all seasons):
```
year          team                          score    
"1964_1965"   "Los Angeles Lakers"          0.349999999999999
"1960_1961"   "Los Angeles Lakers"          0.349999999999999
"1962_1963"   "Los Angeles Lakers"          0.34
"1965_1966"   "Los Angeles Lakers"          0.34
"1961_1962"   "Los Angeles Lakers"          0.34
"1963_1964"   "Los Angeles Lakers"          0.33
"1966_1967"   "Los Angeles Lakers"          0.32
"1967_1968"   "Los Angeles Lakers"          0.299999999999999
"1968_1969"   "Los Angeles Lakers"          0.28
"1971_1972"   "Los Angeles Lakers"          0.28
"1969_1970"   "Los Angeles Lakers"          0.28
"1970_1971"   "Los Angeles Lakers"          0.26
"1986_1987"   "Los Angeles Lakers"          0.25
"1972_1973"   "Los Angeles Lakers"          0.25
"1984_1985"   "Los Angeles Lakers"          0.25
"1979_1980"   "Los Angeles Lakers"          0.25
"1973_1974"   "Los Angeles Lakers"          0.239999999999999
"1996_1997"   "Los Angeles Lakers"          0.239999999999999
"1987_1988"   "Los Angeles Lakers"          0.239999999999999
"1983_1984"   "Los Angeles Lakers"          0.23
"1982_1983"   "Los Angeles Lakers"          0.23
"1990_1991"   "Los Angeles Lakers"          0.23
"1994_1995"   "Los Angeles Lakers"          0.23
"1975_1976"   "Los Angeles Lakers"          0.23
"1989_1990"   "Los Angeles Lakers"          0.23
"1999_2000"   "Los Angeles Lakers"          0.23
"1997_1998"   "Los Angeles Lakers"          0.23
"1978_1979"   "Los Angeles Lakers"          0.23
"2003_2004"   "Los Angeles Lakers"          0.23
"2008_2009"   "Los Angeles Lakers"          0.23
"1985_1986"   "Los Angeles Lakers"          0.23
"1976_1977"   "Los Angeles Lakers"          0.23
"2009_2010"   "Los Angeles Lakers"          0.22
"1988_1989"   "Los Angeles Lakers"          0.22
"1980_1981"   "Los Angeles Lakers"          0.22
"2007_2008"   "Los Angeles Lakers"          0.22
"2010_2011"   "Los Angeles Lakers"          0.22
"2002_2003"   "Los Angeles Lakers"          0.22
"1977_1978"   "Los Angeles Lakers"          0.209999999999999
"1981_1982"   "Los Angeles Lakers"          0.209999999999999
"1995_1996"   "Los Angeles Lakers"          0.209999999999999
"2000_2001"   "Los Angeles Lakers"          0.209999999999999
"2001_2002"   "Los Angeles Lakers"          0.209999999999999
"2012_2013"   "Los Angeles Lakers"          0.209999999999999
"2011_2012"   "Los Angeles Lakers"          0.209999999999999
"1974_1975"   "Los Angeles Lakers"          0.209999999999999
"2005_2006"   "Los Angeles Lakers"          0.209999999999999
"1991_1992"   "Los Angeles Lakers"          0.2
"1992_1993"   "Los Angeles Lakers"          0.2
"2006_2007"   "Los Angeles Lakers"          0.19
"1998_1999"   "Los Angeles Lakers"          0.179999999999999
"2004_2005"   "Los Angeles Lakers"          0.17
"2013_2014"   "Los Angeles Lakers"          0.17
"2017_2018"   "Los Angeles Lakers"          0.17
"1993_1994"   "Los Angeles Lakers"          0.17
"2016_2017"   "Los Angeles Lakers"          0.16
"2014_2015"   "Los Angeles Lakers"          0.13
"2015_2016"   "Los Angeles Lakers"          0.11
```

Ranking is based on every game played by each team, including the playoffs/finals.
