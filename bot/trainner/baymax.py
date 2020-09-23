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
    "#beyondcompare"
])
trainner.train([
    "open beyond compare",
    "#beyondcompare"
])

trainner.train([
    "bcompare",
    "#beyondcompare"
])

trainner.train([
    "beyondcompare",
    "#beyondcompare"
])

trainner.train([
    "open redmine",
    "#redmine"
])

trainner.train([
    "redmine",
    "#redmine"
])

trainner.train([
    "what program you're writen in?",
    "python"
])

trainner.train([
    "what your name?",
    "baymax"
])

trainner.train([
    "haha",
    "what so funny lah?🤔"
])

trainner.train([
    "lol",
    "what so funny lah?🤔"
])

trainner.train([
    "open putty",
    "#putty"
])

trainner.train([
    "putty",
    "#putty"
])
#list [bizplay website , beyond compare deploy , redmine category , putty session , open eclipse ]