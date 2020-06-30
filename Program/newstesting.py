from newsapi.newsapi_client import NewsApiClient
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords 
stopwords.words("english")
from nltk.tokenize import word_tokenize
nltk.download('punkt')
import tkinter as tk
from PIL import ImageTk,Image
import requests
import json


HEIGHT = 850
WIDTH = 950

def input(entry):
    print (entry)


def format_response(title):
    
    try:
        titleheadfirst = title['articles'][0]['source']['name']
        titleheadsecond = title['articles'][0]['title']
        titleheadthree = title['articles'][0]['source']['id']
        final_str = 'The latest article name: %s \n Title: %s \n This is the ID %s' % (titleheadfirst, titleheadsecond, titleheadthree)
    except:
        final_str= 'There was a problem in retrieving your data, or there are no headlines. please try again.'
    return final_str

def get_news(id):  
    getnews_key = '6485ea77ce3447fc80b37f4dd113f4f3'
    url = 'https://newsapi.org/v2/top-headlines'
    parameters = {
    'q': id,
    'country' : 'gb',# query phrase
    'pageSize': 10,  # maximum is 100
     'apiKey': getnews_key }
    response = requests.get(url, params=parameters)
    response_json = response.json()
    print(response_json)

    #print(response_json['articles'][0]['source']['name'])
    #print(response_json['articles'][0]['title'])
    #print(response_json['articles'][0]['source']['id'])
    lower_label['text'] = format_response(response_json)
    

GUI = tk.Tk()

canvas = tk.Canvas(GUI, height=HEIGHT, width=WIDTH)


background = tk.PhotoImage(file='C:\\Users\\Jonny\\Desktop\\SE\\newstesting\\test.png')
background_Label = tk.Label(GUI, image=background)
background_Label.place(x=0, y=0, relwidth=1, relheight=1)

canvas.pack()

heading = tk.Label(canvas, text="Please enter a news site", font=40)
heading.place(relx=0.1, relheight=0.15, relwidth=0.25)



frame = tk.Frame(GUI, bg='light blue', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.90, relheight=0.1, anchor='n')




search = tk.Button(frame, text="Get News", bg='white', command=lambda: get_news(entry.get()))
search.place(relx=0.8, relheight=1, relwidth=0.20)


entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.75, relheight=1)

frame_l = tk.Frame(GUI, bg='light grey', bd=10)
frame_l.place(relx=0.5, rely=0.25, relwidth=0.80, relheight=0.6, anchor='n')



lower_label = tk.Label(frame_l, font=10)
lower_label.place(relwidth=1, relheight=1)

frame_bottom = tk.Frame(GUI, bg='light grey', bd=5)
frame_bottom.place(relx=0.5, rely=0.85, relwidth=0.90, relheight=0.1, anchor='n')

bottom_label = tk.Label(frame_bottom, text="Sites to search are; bbc-news, Theguardian.com, ars-technica, Skysports.com, Mirror.co.uk, Telegraph.co.uk,\n Dailymail.co.uk, Thesun.co.uk, independent" , font=10)
bottom_label.place(relx=0.05, relwidth=0.90, relheight=1)


#stop_words = set(stopwords.words('english')) 
#init 
#newsapi = NewsApiClient(api_key='6a4d8068c73d4b6e8dc5f9ed70d34beb')
#data = newsapi.get_top_headlines(sources='bbc-news')
#articles = data['articles']
#for w in articles:
    #word_tokens = word_tokenize(w["title"])
    #filtered_sentence = [w for w in word_tokens if not w in stop_words]
    #filtered_sentence = []  
    #for w in word_tokens: 
        #if w not in stop_words: 
            #filtered_sentence.append(w) 

    #print(word_tokens) 
    #print(filtered_sentence) 



GUI.mainloop()
# single article test


# test = data['articles'][0]
# #print(test["title"])

# #remove common words
# word_tokens = word_tokenize(test["title"]) 

# filtered_sentence = [w for w in word_tokens if not w in stop_words] 

# filtered_sentence = [] 
  
# for w in word_tokens: 
#     if w not in stop_words: 
#         filtered_sentence.append(w) 
  
# print(word_tokens) 
# print(filtered_sentence) 



#for w in articles:
    #print(w["title"])




