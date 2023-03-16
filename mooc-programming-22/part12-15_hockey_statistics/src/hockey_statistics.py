from json import *

def read_data():
    filename = input("file name: ")
    
    data = []
    players = []

    with open(filename) as data_file:
        data = loads(data_file.read())
        print(f"read the data of {len(data)} players\n")

    for player in data:
        players.append(Player(player["name"],player["nationality"],player["assists"],player["goals"],player["penalties"],player["team"],player["games"]))

    return players

class Player:
    def __init__(self, name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
        self.points = goals + assists

    def __str__(self):
        return f"{self.name:<21}{self.team:<5}{self.goals:>2} + {self.assists:>2} = {self.points:>3}"
    
class Application:
    def __init__(self):
        self.__players = read_data()

    def help(self):
        print("commands: ")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def search_for_player(self):
        name = input("name: ")

        for player in self.__players:
            if player.name==name:
                print(player)

    def teams(self):
        teams_list = sorted(set([player.team for player in self.__players]))

        for player in teams_list:
            print(player)

    def countries(self):
        countries_list = sorted(set([player.nationality for player in self.__players]))

        for player in countries_list:
            print(player)

    def players_in_team(self):
        team = input("team: ")
        team_players_list = []

        for player in self.__players:
            if player.team==team:
                team_players_list.append(player)

        for team_player in sorted(team_players_list, key = lambda player: player.points, reverse=True):
            print(team_player) 

    def players_from_country(self):
        country = input("country: ")
        country_players_list = []

        for player in self.__players:
            if player.nationality==country:
                country_players_list.append(player) 

        for country_player in sorted(country_players_list, key = lambda player: player.points, reverse=True):
            print(country_player)

    def most_points(self):
        number_of_players = int(input("how many: "))

        points_list = sorted(self.__players, key = lambda player: (player.points, player.goals), reverse=True)

        for player in range(number_of_players):
            print(points_list[player])

    def most_goals(self):
        number_of_players = int(input("how many: "))

        scorers_list = sorted(self.__players, key = lambda player: (player.goals, -player.games), reverse=True)
        
        for player in range(number_of_players):
            print(scorers_list[player])

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.search_for_player()
            elif command == "2":
                self.teams()
            elif command == "3":
                self.countries()
            elif command == "4":
                self.players_in_team()
            elif command == "5":
                self.players_from_country()
            elif command == "6":
                self.most_points()
            elif command == "7":
                self.most_goals()
            else:
                self.help()

application = Application()
application.execute()