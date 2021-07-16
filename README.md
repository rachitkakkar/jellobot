**UPDATE:** Development on jellobot has ceased, and the project is now discontinued. However, a friend has forked the project (called [jellobotv2](https://github.com/swissconfederation/jellobotv2)) and plans to continue adding features.

# jellobot
A discord bot made for an inside joke. Since then its evolved to have polling, an economy, some other fun commands, and of course I have made the original joke work better using nltk's wordnet (to find adjectives and verbs).

# Requirements
The discord.py and asyncio modules are required, and the code runs on Python 3.9. It also needs pandas to read/write the bank info. On top of this it needs regex, nltk, and the nltk wordnet. These modules are used for langauge parsing.

# Features
- The bot responds with `your face is {}` to sentences (uses things like verbs and adjectives to construct replies) - (15% chance)
- The bot also has a basic economy, but you must run `?save` before you close the bot to save the bank info, and `?load` is needed to get the data back after a restart.
- The bot has a thumbs up/thumbs down poll command - `?poll {number of hours} {prompt}` - automatically tallies after poll ends.
- The bot responds with a custom message for any message that has bruh, poop, and cool. (15% chance)
- The bot has a lot of other fun commands like `?die`, `?useless`, and `?green_screen`.

# Commands
```
create_account     This command gives you a bank account with $1,000
delete-bot-message This command deletes a bot message (you can get the id f...
die                This command returns a random last word
give               This command gives another person money
green_screen       This command helps you frame me
help               Shows this message
lb                 See leadboard
load               Load the bank info
poll               This command allows a poll with upvotes and downvote - a...
save               Save the bank info
useless            This command returns a useless image
work               This command gives you money ranging from 1-100, there i...
```
