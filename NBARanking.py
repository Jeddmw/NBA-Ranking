#Method described in links below
#http://blog.biophysengr.net/2012/03/eigenbracket-2012-using-graph-theory-to.html
#https://patricktbrown.org/ranking-sports-teams-according-to-cumulative-connections/
import psycopg2
import csv
from os.path import expanduser
import networkx as nx
import requests
import re
from bs4 import BeautifulSoup

def rotationStr(selection):
	if selection == 0:
		return '2017_2018'
	if selection == 1:
		return '2016_2017'
	if selection == 2:
		return '2015_2016'
	if selection == 3:
		return '2014_2015'
	if selection == 4:
		return '2013_2014'
	if selection == 5:
		return '2012_2013'
	if selection == 6:
		return '2011_2012'
	if selection == 7:
		return '2010_2011'
	if selection == 8:
		return '2009_2010'
	if selection == 9:
		return '2008_2009'
	if selection == 10:
		return '2007_2008'
	if selection == 11:
		return '2006_2007'
	if selection == 12:
		return '2005_2006'
	if selection == 13:
		return '2004_2005'
	if selection == 14:
		return '2003_2004'
	if selection == 15:
		return '2002_2003'
	if selection == 16:
		return '2001_2002'
	if selection == 17:
		return '2000_2001'
	if selection == 18:
		return '1999_2000'
	if selection == 19:
		return '1998_1999'
	if selection == 20:
		return '1997_1998'
	if selection == 21:
		return '1996_1997'
	if selection == 22:
		return '1995_1996'
	if selection == 23:
		return '1994_1995'
	if selection == 24:
		return '1993_1994'
	if selection == 25:
		return '1992_1993'
	if selection == 26:
		return '1991_1992'
	if selection == 27:
		return '1990_1991'
	if selection == 28:
		return '1989_1990'
	if selection == 29:
		return '1988_1989'
	if selection == 30:
		return '1987_1988'
	if selection == 31:
		return '1986_1987'
	if selection == 32:
		return '1985_1986'
	if selection == 33:
		return '1984_1985'
	if selection == 34:
		return '1983_1984'
	if selection == 35:
		return '1982_1983'
	if selection == 36:
		return '1981_1982'
	if selection == 37:
		return '1980_1981'
	if selection == 38:
		return '1979_1980'
	if selection == 39:
		return '1978_1979'
	if selection == 40:
		return '1977_1978'
	if selection == 41:
		return '1976_1977'
	if selection == 42:
		return '1975_1976'
	if selection == 43:
		return '1974_1975'
	if selection == 44:
		return '1973_1974'
	if selection == 45:
		return '1972_1973'
	if selection == 46:
		return '1971_1972'
	if selection == 47:
		return '1970_1971'
	if selection == 48:
		return '1969_1970'
	if selection == 49:
		return '1968_1969'
	if selection == 50:
		return '1967_1968'
	if selection == 51:
		return '1966_1967'
	if selection == 52:
		return '1965_1966'
	if selection == 53:
		return '1964_1965'
	if selection == 54:
		return '1963_1964'
	if selection == 55:
		return '1962_1963'
	if selection == 56:
		return '1961_1962'
	if selection == 57:
		return '1960_1961'
	if selection == 58:
		return '1959_1960'
	if selection == 59:
		return '1958_1959'
	if selection == 60:
		return '1957_1958'
	if selection == 61:
		return '1956_1957'
	if selection == 62:
		return '1955_1956'
	if selection == 63:
		return '1954_1955'
	if selection == 64:
		return '1953_1954'
	if selection == 65:
		return '1952_1953'
	if selection == 66:
		return '1951_1952'
	if selection == 67:
		return '1950_1951'
	if selection == 68:
		return '1949_1950'
	if selection == 69:
		return '1948_1949'
	if selection == 70:
		return '1947_1948'
	if selection == 71:
		return '1946_1947'

#need user agent to get past 406 error message
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}
conn = psycopg2.connect("host=localhost dbname=nbarankings user=postgres")
cur = conn.cursor()

cur.execute("DELETE FROM rankings")
for count in range(0, 72):
	#TODO: create networkx directed Graph object
	G = nx.DiGraph()
	#read in html
	year = rotationStr(count)
	print("Currently Storing " + year + "...")
	link = 'http://www.landofbasketball.com/results/' + year + '_scores_full.htm'
	# r = requests.get('http://www.landofbasketball.com/results/2017_2018_scores_full.htm', headers=headers)
	r = requests.get(link, headers=headers)
	soup = BeautifulSoup(r.text, 'html5lib')

	#get table and loop through all the rows
	for row in soup.find('table', {"class" : "color-alt"}).find_all('tr'):
	    cells = row.findAll(['td', 'div'])
	    if len(cells) == 2:
	        date = cells[0].text.strip()
	    if len(cells) == 9:
	        away_team = cells[3].text.strip()
	        home_team = cells[6].text.strip()
	        #print(cells[3].text.strip() + ' at ')
	        #print(cells[6].text.strip())
	        #print(cells[8].text.strip())
	    #only rows with game data are of length 11 or 13 with OT
	    if len(cells) == 11 or len(cells) == 13:
	        #get team info
	        try:
	            #for index in range(1, len(cells)):
	            #print(str(index) + '	' + cells[index].text.strip())
	            winning_team = cells[3].text.strip()
	            winning_score = int(re.findall('\d+', cells[4].text.strip())[0])
	            losing_team = cells[8].text.strip()
	            losing_score = int(re.findall('\d+', cells[9].text.strip())[0])
	            if len(cells) == 11:
	                away_team_short = cells[10].text.strip()[3:].splitlines()[0]
	            else:
	                away_team_short = cells[12].text.strip()[3:].splitlines()[0]
	            if away_team_short in winning_team:
	                home_team = losing_team
	                away_team = winning_team
	            else:
	                home_team = winning_team
	                away_team = losing_team
	            if away_team_short not in winning_team and away_team not in losing_team:
	                print("ERROR")
	            victory_margin = winning_score - losing_score
	            #TODO: add edge to Graph from losing team to winning team
	            G.add_edge(losing_team, winning_team, weight = victory_margin)
	        except:
	            pass

	#TODO: display team centralities from Graph
	centrality = nx.eigenvector_centrality_numpy(G)
	output = (['{} {:0.2f}'.format(node, centrality[node]) for node in sorted(centrality.iterkeys())])

	team_scorelist = []
	team_ranklist = []
	#iterate through the array that has the team names and scores
	for i in range(0, len(output)):
	    team_name = output[i]
	    #cut the team names to isolate the team score
	    team_scorelist.append(team_name[len(team_name) - 4:])
	    #keep the team names in a separate list
	    team_ranklist.append(team_name[0:len(team_name) - 5])

	#sort the two arrays so that the team name corresponds with the team score
	#example: team_scorelist[1] and team_ranklist[1] should correspond
	#             0.22          and      Golden State Warriors
	index = range(len(team_scorelist))
	index.sort(key=team_scorelist.__getitem__, reverse=True)

	team_scorelist[:] = [team_scorelist[i] for i in index]
	team_ranklist[:] = [team_ranklist[i] for i in index]

	#insert_query = "INSERT INTO NBARanking VALUES {}".format(""(, 'hello@dataquest.io', 5)")

	#print the rankings
	for i in range(0, len(output)):
	    sql = """INSERT INTO rankings (year, team, score) VALUES (%s, %s, %s)"""
	    width = 50 - len(team_ranklist[i])
	    if i < 9:
	        cur.execute(sql, (year, team_ranklist[i], float(team_scorelist[i])))
	        conn.commit()
	    else:
	        cur.execute(sql, (year, team_ranklist[i], float(team_scorelist[i])))
	        conn.commit()

	home = expanduser("~")
	cur.execute("COPY rankings TO "  + "'" + home + "/rankings.csv' DELIMITER ',' CSV HEADER")
