# from django.shortcuts import render

# # Create your views here.
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from data_preprocessing import DataPreProcessing
# from data_ingestion import DataIngestion
# from chat_pipeline import ChatPipeline
# from dotenv import load_dotenv
# import os

# load_dotenv()

# PDF_DIRECTORY = ".chatbot/pdfs"
# PDF_FILENAME = "Nepatronix_syllabus.pdf"
# PDF_PATH = os.path.join(PDF_DIRECTORY, PDF_FILENAME)

# # class LoadPDFView(APIView):
# #     def get(self, request):
# #         if not os.path.exists(PDF_PATH):
# #             return Response({"detail": "PDF file not found."}, status=status.HTTP_400_BAD_REQUEST)
        
# #         data_preprocessor = DataPreProcessing(PDF_PATH)
# #         text = data_preprocessor.read_pdf()
# #         if not text:
# #             return Response({"detail": "No text extracted from PDF."}, status=status.HTTP_400_BAD_REQUEST)
        
# #         chunks = data_preprocessor.extract_chunk(text)
        
# #         store_name = PDF_FILENAME
# #         data_ingestor = DataIngestion(store_name)
# #         vectorstore = data_ingestor.create_vectorstore(chunks)
        
# #         request.session['vectorstore'] = vectorstore
# #         request.session['chunks_count'] = len(chunks)
# #         request.session['chat_pipeline'] = ChatPipeline(vectorstore)
        
# #         return Response({"message": "PDF processed successfully", "chunks_count": len(chunks)})

# class AskQuestionView(APIView):
    
#     # request.session['vectorstore'] = vectorstore
#     # request.session['chunks_count'] = len(chunks)
#     # request.session['chat_pipeline'] = ChatPipeline(vectorstore)
#     def post(self, request):
#         if not os.path.exists(PDF_PATH):
#            Response({"detail": "PDF file not found."}, status=status.HTTP_400_BAD_REQUEST)
    
#         data_preprocessor = DataPreProcessing(PDF_PATH)
#         text = data_preprocessor.read_pdf()
#         if not text:
#             Response({"detail": "No text extracted from PDF."}, status=status.HTTP_400_BAD_REQUEST)
        
#         chunks = data_preprocessor.extract_chunk(text)
        
#         store_name = PDF_FILENAME
#         data_ingestor = DataIngestion(store_name)
#         vectorstore = data_ingestor.create_vectorstore(chunks)
#         chat_pipeline = ChatPipeline(vectorstore)
#         chat_pipeline = chat_pipeline
#         if not chat_pipeline:
#             return Response({"detail": "PDF has not been processed yet."}, status=status.HTTP_400_BAD_REQUEST)
            
#         # question = request.data.get('question')
#         question = request
    
#         if not question:
#             return Response({"detail": "Question is required."}, status=status.HTTP_400_BAD_REQUEST)
        
#         response = chat_pipeline.process_query(question)
#         # chat_history = request.session.get('chat_history', [])
#         # chat_history.append((question, response))
#         # request.session['chat_history'] = chat_history
        
#         return Response({"question": question, "response": response})

# # class ChatHistoryView(APIView):
# #     def get(self, request):
# #         chat_history = request.session.get('chat_history', [])
# #         return Response({"chat_history": chat_history})
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuestionSerializer
from data_preprocessing import DataPreProcessing
from data_ingestion import DataIngestion
from chat_pipeline import ChatPipeline
from dotenv import load_dotenv
import os

load_dotenv()

PDF_DIRECTORY = "./pdfs"
PDF_FILENAME = "Nepatronix_syllabus.pdf"
# PDF_PATH = os.path.join(PDF_DIRECTORY, PDF_FILENAME)
PDF_PATH = "E:/Projects/nepatronix_chatbot/chatbot/pdfs/Nepatronix_syllabus.pdf"

# Initialize global variables to store the chat pipeline and chat history
CHAT_PIPELINE = None
CHAT_HISTORY = []

# Load and process the PDF during the startup
if os.path.exists(PDF_PATH):
    data_preprocessor = DataPreProcessing()
    text = data_preprocessor.read_pdf()
    if text:
        chunks = data_preprocessor.extract_chunk(text)
        store_name = PDF_FILENAME
        data_ingestor = DataIngestion(store_name)
        vectorstore = data_ingestor.create_vectorstore(chunks)
        CHAT_PIPELINE = ChatPipeline(vectorstore)
    else:
        print("No text extracted from PDF.")
else:
    print("PDF file not found.")
 # testing  sesion with manual static data
print(len(chunks))
response = CHAT_PIPELINE.process_query("What is nepatronix ?")
print(response)

class AskQuestionView(APIView):
    def post(self, request):
        global CHAT_PIPELINE, CHAT_HISTORY

        if not CHAT_PIPELINE:
            return Response({"detail": "PDF has not been processed yet."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.validated_data['question']
            response = CHAT_PIPELINE.process_query(question)
            CHAT_HISTORY.append((question, response))
            
            return Response({"response": response})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
