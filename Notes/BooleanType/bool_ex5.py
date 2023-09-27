# Company wants to increase their server according to their CPU usage. 
# Create a python program that gets average cpu usage as an input 
# and prints True if we need to launch more servers for our application.
# When average cpu usage is between 40 and 70 inclusive
# we should launch a new server.

avg_cpu_util = int(input("Enter the avg cpu utiliztion please: "))
should_launch = 40 <= avg_cpu_util <= 70
print(should_launch)