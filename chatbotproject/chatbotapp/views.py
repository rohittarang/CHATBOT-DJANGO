from django.shortcuts import render
from django.http import HttpResponse

#/------------------ chatbot-libraries ------------------/#

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

#/------------------ chatbot-libraries ------------------/#

bot = ChatBot('chatbot', read_only=False, 
              logic_adapters=[{
                  'import_path':'chatterbot.logic.BestMatch',
                #   'default_response':'Sorry, I dont know !',
                #   'maximum_similarity_threshold':0.90
              }])

list_to_train = [
    "Hi", #question
    "Hi, there", #answer
    "What's Your Name", #question
    "I'm just a Chatbot", #answer
    "What is your favourite game ?", #question
    "My favourite game is Cricket", #answer
    "What is your favourite food ? ", #question
    "My favourite food is Internet", #answer
]

# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)

chatterBotCorpus = ChatterBotCorpusTrainer(bot)
chatterBotCorpus.train('chatterbot.corpus.english')


# Create your views here.
def index(request):
    return render(request,'chatbotapp/index.html')

def specific(request):
    return HttpResponse("This is specific url")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatbotResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatbotResponse)