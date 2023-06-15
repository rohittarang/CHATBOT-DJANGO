

asgiref==3.7.2
blis==0.7.9
catalogue==2.0.8
certifi==2023.5.7
charset-normalizer==3.1.0
ChatterBot==1.0.5
chatterbot-corpus==1.2.0
click==8.1.3
colorama==0.4.6
confection==0.0.4
cymem==2.0.7
Django==4.2.2
dnspython==2.3.0
greenlet==2.0.2
idna==3.4
Jinja2==3.1.2
joblib==1.2.0
langcodes==3.3.0
Mako==1.1.2
MarkupSafe==2.1.3
mathparse==0.1.2
murmurhash==1.0.9
nltk==3.8.1
numpy==1.24.3
packaging==23.1
pathy==0.10.1
Pint==0.22
preshed==3.0.8
pydantic==1.10.9
pymongo==4.3.3
python-dateutil==2.8.2
pytz==2023.3
PyYAML==5.1
regex==2023.6.3
requests==2.31.0
six==1.16.0
smart-open==6.3.0
spacy==3.5.3
spacy-legacy==3.0.12
spacy-loggers==1.0.4
SQLAlchemy==1.3.6
sqlparse==0.4.4
srsly==2.4.6
thinc==8.1.10
tqdm==4.65.0
typer==0.7.0
typing_extensions==4.6.3
tzdata==2023.3
urllib3==2.0.3
wasabi==1.1.2

//---------------

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
from chatterbot.trainers import ListTrainer

from chatterbot import utils
from chatterbot.storage import SQLStorageAdapter
from sqlalchemy import inspect

# storage_adapter = {
#     'import_path': 'chatterbot.storage.SQLStorageAdapter',
#     'database_uri': 'sqlite:///D:/CHATBOT-DJANGO/chatbotproject/db.sqlite3',
#     'read_only': False
# }


# bot = ChatBot('chatbot', storage_adapter='chatterbot.storage.SQLStorageAdapter',
#               database_uri='sqlite:///D:/CHATBOT-DJANGO/chatbotproject/db.sqlite3')

# if not inspect(bot.storage.adapter.engine).has_table('Statement'):
#     bot.storage.adapter.create()

# bot = ChatBot('chatbot')
# bot = ChatBot('chatbot', storage_adapter=storage_adapter)
bot = ChatBot('chatbot', read_only=False, logic_adapters=['chatterbot.logic.BestMatch'])
# bot = ChatBot('chatbot', read_only=False)

list_to_train = [
    "Hi", #question
    "Hi, there", #answer
    "What's Your Name", #question
    "I'm just a Chatbot", #answer
    "What is your favourite game ?", #question
    "My favourite game is Cricket", #answer
]

list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

#/------------------ chatbot-libraries ------------------/#

# Create your views here.
def index(request):
    return render(request,'chatbotapp/index.html')

def specific(request):
    return HttpResponse("This is specific url")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    return HttpResponse(userMessage)