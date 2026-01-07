# Determining Rio the parrot's talkativeness.
# the parrot is talkative if: it's between 5-10AM and/or it is sunny outside.
# AI: I did not use ai to write any of this code. There would be a CLAUDE.md file, or it would be in .gitignore
# It might have been used to simplify/find python documentation as it sometimes looks like another language (not just the python snippets)

from datetime import datetime

# Tasks:
# - get current time (DONE)
# - get current weather (DONE) - giving up on actual data I will instead ask you to look out the window
# - figure Out whether Rio is talkative (DONE)

# this is a hardcoded time (will remove)
fake_time = 6

# this gets and prints the actual time
now = datetime.now()
print(now)
hour = now.hour

print(f"The current time is: {hour}")

# Now getting the weather
weatherquestion = input("Look out the window, is it sunny? Y/N: ")
is_sunny = weatherquestion == "Y"

# Is Rio going to be talkative?
if is_sunny or (5 <= hour <= 10):
    print("Rio The Parrot will be talkative")
else:
    print("Rio The Parrot will not be talkative")
