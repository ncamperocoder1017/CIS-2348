# Nicolas Campero
# 1856853

class Team:
    def __init__(self):
        self.team_name = 'None'
        self.team_wins = 0.0
        self.team_losses = 0.0

    def get_win_percentage(self):
        return self.team_wins / (self.team_losses + self.team_wins)

if __name__ == '__main__':
    team = Team()
    team.team_name = str(input())
    team.team_wins = float(input())
    team.team_losses = float(input())

    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team {} has a winning average!'.format(team.team_name))
    else:
        print('Team {} has a losing average.'.format(team.team_name))
