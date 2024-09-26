from django.urls import path
from .views import  AskQuestionView
# from .views import ChatHistoryView
# from .views import LoadPDFView
urlpatterns = [
    # path('load_pdf/', LoadPDFView.as_view(), name='load_pdf'),
    path('ask_question/', AskQuestionView.as_view(), name='ask_question'),
    # path('chat_history/', ChatHistoryView.as_view(), name='chat_history'),
]
