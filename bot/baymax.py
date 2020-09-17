from chatterbot import ChatBot

bot = ChatBot('baymax',
              logic_adapters=[
                  {
                      'import_path': 'chatterbot.logic.BestMatch',
                      'default_response': 'I am sorry, but I do not understand.',
                      'maximum_similarity_threshold': 0.3
                  }, {
                      'import_path': 'chatterbot.logic.MathematicalEvaluation'
                  }
              ])
bot.read_only = True


def get_response(words):
    return bot.get_response(words)
