# Q12. Repeatedly enter team names and wins/losses; calculate a team's winning percentage, list wins for each team, and list teams with winning records.
teams = {}
while True:
    name = input("Enter team name (or 'done' to finish): ").strip()
    if name.lower() == 'done':
        break
    wins = int(input("Number of wins: "))
    losses = int(input("Number of losses: "))
    teams[name] = [wins, losses]

if teams:
    selected = input("Enter a team name to calculate its winning percentage: ").strip()
    if selected in teams:
        wins, losses = teams[selected]
        games = wins + losses
        percentage = (wins / games * 100) if games else 0
        print(f"Winning percentage: {percentage:.2f}%")
    else:
        print("Team not found")

print("Number of wins of each team:", [record[0] for record in teams.values()])
winning_teams = [name for name, record in teams.items() if record[0] > record[1]]
print("Teams with winning records:", winning_teams)
