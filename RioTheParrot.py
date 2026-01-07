# Determining Rio the parrot's talkativeness.
# the parrot is talkative if: it's between 5-10AM and/or it is sunny outside.

from datetime import datetime

# Things I need to do:
# - get current time (DONE)
# - get current weather
# - figure Out whether Rio is talkative

# this is a hardcoded time for while I find out how to get the current time. (will remove)
fake_time = 5

# this gets and prints the actual time
now = datetime.now()
hour = now.hour
# print(now)
# print(hour)

print(f"The current time is: {hour}")