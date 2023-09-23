# There is 20 devop in the company, that should be equally assigned to each 8 scrum teams.
#Find out how many Devops engineer will not be assigned with the team.
#Also find out how many devop engineer will be in the each scrum team.
devops = 20
scrum = 8
result = devops % scrum
print("Each team will have ", devops //scrum,"will be in the team")
print(result)
