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
    "open beyondcompare",
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



#list [bizplay website , beyond compare deploy , redmine category , putty session , open eclipse ]