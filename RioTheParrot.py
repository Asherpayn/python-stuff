# Determining Rio the parrot's talkativeness.
# the parrot is talkative if: its between 5-10AM and/or it is sunny outside.

from datetime import datetime

# Things i need to do:
# - get current time
# - get current weather
# - figure Out whether Rio is talkative

# this is a harcoded time for while i find out how to get the current time.
current_time = 5

# his prints the actual time, this will be used later
now = datetime.now()
hour = now.hour
print(now)
print(hour)


print(f"The current time is: {current_time} AM/PM")