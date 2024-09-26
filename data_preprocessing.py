from PyPDF2 import PdfReader
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import bs4



class DataPreProcessing:
    # def __init__(self,pdf):

    #     self.pdf = pdf
        
    
    def read_pdf(self):
        # pdf_reader = PdfReader(self.pdf)
        # text = ""
        # for page in pdf_reader.pages:
            
        #     text += page.extract_text()
        blog_url = "https://nepatronix.org/blogs"
        shop_url = "https://nepatronix.org/shop"
        books_url = "https://nepatronix.org/books"
        contact_url = "https://nepatronix.org/team"
        gallery_url = "https://nepatronix.org/gallery"
        product_url = "https://nepatronix.org/products"
        services = "https://nepatronix.org/services"
        about_url = "https://nepatronix.org/about"
        service1 = "https://nepatronix.org/services/in-house-product-selling"
        service2="https://nepatronix.org/services/training-on-iot-and-robotic"
        service3 = "https://nepatronix.org/services/pcb-design-"
        service4="https://nepatronix.org/services/website-development"
        kit = 'https://nepatronix.org/products/robotic-kit-'
        attendance = 'https://nepatronix.org/products/rfid-based-attendance-machine'
        tut1 = "https://nepatronix.org/tutorials"
        blog1 = "https://nepatronix.org/blogs/20-arduino-projects-for-beginners"
        blog2 = "https://nepatronix.org/blogs/66b1bcffac3bd112f76e70ea"
        blog3 = "https://nepatronix.org/blogs/6687fa0192d56de95c0ee021"
        blog4 = "https://nepatronix.org/blogs/fire-detection-through-esp32-mobile-app-(iot-project-in-nepal)"
        blog5 ="https://nepatronix.org/blogs/top-three-raspberry-pi-project"
        blog6 = "https://nepatronix.org/blogs/lora(long-range)alert-system(iot-projects-arduino)"
        book1 ="https://nepatronix.org/books/20-easy-raspberry-pi-projects"
        book2  ="https://nepatronix.org/books/arduino-for-beginners"
        book3 = "https://nepatronix.org/books/a-beginer-guide-to-esp8266"
        home ="https://nepatronix.org/"






        # Create an instance of the UnstructuredURLLoader

        loader = UnstructuredURLLoader(urls = [tut1,book1,book2,book3,blog1,blog2,blog3,blog4,blog5,blog6,home,service1,service2,service3,service4,kit,attendance,blog_url,shop_url,books_url,contact_url,gallery_url,services,product_url,about_url])
        docs = loader.load()


        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)
        
        
        website_text = ""
        for split in splits:
            text = split.page_content
            website_text += text
        
        return website_text
        
    def extract_chunk(self, text,chunk_size=1000, chunk_overlap=100):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size = chunk_size, chunk_overlap = chunk_overlap)
        splits = text_splitter.split_text(text=text)
        return splits

        
        



        
                
        

