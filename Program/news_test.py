from newsapi.newsapi_client import NewsApiClient
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords 
stopwords.words("english")
from nltk.tokenize import word_tokenize
nltk.download('punkt')
import tkinter as tk
import requests


HEIGHT = 700
WIDTH = 800

def input(entry):
    print (entry)


def get_news(headline): 
    news_key = '6485ea77ce3447fc80b37f4dd113f4f3'
    url = 'https://newsapi.org/v2/top-headlines'
    params = {'apiKey': news_key, 'articles': 'name'}
    response = requests.get(url, params=params)
    print(respone.json())





GUI = tk.Tk()

canvas = tk.Canvas(GUI, height=HEIGHT, width=WIDTH)
canvas.pack()

#background = tk.PhotoImage(file='test.png')
#background_Label = tk.Label(GUI, image=background)
#background_Label.place(x=0, y=0, relwidth=1, relheight=1)

heading = tk.Label(canvas, text="Please enter a news site.", font=40)
heading.place(relx=0.1, relheight=0.1, relwidth=0.6)

frame = tk.Frame(GUI, bg='light blue', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')




search = tk.Button(frame, text="Get News", bg='white', command=lambda: get_news(entry.get()))
search.place(relx=0.7, relheight=1, relwidth=0.3)


entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

frame_l = tk.Frame(GUI, bg='light grey', bd=10)
frame_l.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

lower_label = tk.Label(frame_l, font=40)
lower_label.place(relwidth=1, relheight=1)



#stop_words = set(stopwords.words('english')) 
#init 
#newsapi = NewsApiClient(api_key='6a4d8068c73d4b6e8dc5f9ed70d34beb')
#data = newsapi.get_top_headlines(sources='input')
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



