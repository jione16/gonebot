from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('baymax')
trainner = ListTrainer(bot)

trainner.train([
    "Hello",
    "hi"
])

trainner.train([
    "hi",
    "yes hi"
])

trainner.train([
    "Open beyondcompare",
    "Openning beyondcompare"
])

trainner.train([
    "beyondcompare",
    "Openning beyondcompare"
])

trainner.train([
    "open redmine",
    "Openning Redmine"
])

trainner.train([
    "redmine",
    "Openning Redmine"
])