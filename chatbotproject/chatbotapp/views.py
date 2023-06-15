# ------------------------------- PART-1 ------------------------------- #

# from django.shortcuts import render
# from django.http import HttpResponse

# #/------------------ chatbot-libraries ------------------/#

# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer

# from chatterbot import utils
# from chatterbot.storage import SQLStorageAdapter

# storage_adapter = {
#     'import_path': 'chatterbot.storage.SQLStorageAdapter',
#     'database_uri': 'sqlite:///D:/CHATBOT-DJANGO/chatbotproject/db.sqlite3',
#     'read_only': False
# }
# bot = ChatBot('chatbot')
# # bot = ChatBot('chatbot', storage_adapter=storage_adapter)
# # bot = ChatBot('chatbot', read_only=False, logic_adapters=['chatterbot.logic.BestMatch'])
# # bot = ChatBot('chatbot', read_only=False)

# list_to_train = [
#     "Hi", #question
#     "Hi, there", #answer
#     "What's Your Name", #question
#     "I'm just a Chatbot", #answer
#     "What is your favourite game ?", #question
#     "My favourite game is Cricket", #answer
# ]

# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)

# #/------------------ chatbot-libraries ------------------/#

# # Create your views here.
# def index(request):
#     return render(request,'chatbotapp/index.html')

# def specific(request):
#     return HttpResponse("This is specific url")

# def getResponse(request):
#     userMessage = request.GET.get('userMessage')
#     return HttpResponse(userMessage)

# ------------------------------- PART-2 ------------------------------- #

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
    "Is Vijeta Pagal ?",
    "Yes, Vijeta is Pagal ... ",
    "And What About Prilantee ?",
    "Prilantee is Badiii Pagallll...", 
    "Who is Archana ?",
    "Archana is a beautiful girl with beautiful Mind",
    "Any Other noticable things in Archana ?",
    "Bas Kar Pagle. Isse jyada juth nai bol sakta...... !!! "
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