#a devops team needs to perform a system update on 212 servers.
#However they can only update 8 server per day due to resource restrictions.
#They want to find out how many full days it will take to cpmlete the updates
#and if there will be server left over on the end final day

syste_server = 212
per_day = 8
full_day = syste_server // per_day
print("full days will be", full_day, "updated")
print("dairly will be left", syste_server % per_day)