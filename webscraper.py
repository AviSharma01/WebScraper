#   NOTE: should incorporate JavaScript to create an interactive experience 
#   which will be beneficial for certain procedures involved in the code here.

import requests
from bs4 import BeautifulSoup as sp
import re
import speech_recognition as speech_rec
import webbrowser
from datetime import date
import pyttsx3


headers = { 
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

engine = pyttsx3.init('sapi5')

#   getting the weather information for a particular city

##  improvement can be done by using the Geolocation API to pick up the exact current location
##  and scrape the weather information based on the gather information from the API.

#   reasoning for using the first link, accuweather is the reliable source of weather information.
##  having said that, the other links can be used as well.
def weather_information(reqd_city) :

    url = 'https://www.google.com/search?q=weather+' + reqd_city
    page = requests.get(url)

    soup = sp(page.text, 'lxml')

    links = [a['href'] for a in soup.findAll('a')]
    reqd_link = str(links[16])
    reqd_link = reqd_link.split('=')
    reqd_link = str(reqd_link[1].split['&'])
    reqd_link = reqd_link[0]

    page = requests.get(reqd_link, headers = headers)

    soup = sp(page.content, 'lxml')

    time = soup.find('p', attrs = {'class': 'cur-con-weather-card__subtitle'})
    time = re.sub('\n', '', time.text)
    time = re.sub('\t', '', time)
    time = 'Time: ' + time

    temp = soup.find('div', attrs = {'class':'temp'})
    temp = 'Temperature: ' + temp.text

    actual_temp = soup.find('div', attrs = {'class':'real-feel'})
    actual_temp = re.sub('\n', '',actual_temp.text)
    actual_temp = re.sub('\t', '', actual_temp)
    actual_temp = 'RealFeel: ' + actual_temp[-3:] + 'C'

    climate_description = soup.find('span', attrs = {'class': 'phrase'})
    climate_description = "Description: " + climate_description.text

    more_information = 'For more information, please visit: ' + reqd_link

    print('The weather (' + reqd_city + ') for today is: ')
    print(time)
    print(temp)
    print(actual_temp)
    print(climate_description)
    print(more_information)

    engine.say('The weather today is: ')
    engine.say(time)
    engine.say(temp)
    engine.say(actual_temp)
    engine.say(climate_description)
    engine.say('For more information, please visit accuweather.com')
    engine.runAndWait()


def word_meaning(word):

    url = 'https://www.dictionary.com/browse/' + word
    page = requests.get(url)
    soup = sp(page.content, 'html.parser')

    soup
    meaning_list = soup.findAll('div', attrs = {'class' : 'css-1o58fj8 e1hk9ate4'})
    meaning = [x.text for x in meaning_list]

    meaning0 = meaning[0]
    for x in meaning:
        print(x)
        print('\n')
    engine.say(meaning0)
    engine.runAndWait()

def write_notes():

    recognizer = speech_rec.Recognizer()
    with speech_rec.Microphone() as source:
        print(' What is your TO BE COMPLETED LIST for today')
        engine.say(' What is your TO BE COMPLETED LIST for today')
        engine.runAndWait()
        audio = recognizer.listen(source)
        audio = recognizer.recognize_google(audio)
        print(audio)
        date_today = date.today()
        date_today = str(date_today)
        with open('Notes.txt','a') as f:
            f.write('\n')
            f.write(date_today)
            f.write('\n')
            f.write(audio)
            f.write('\n')
            f.write('...')
            f.write('\n')
            f.close() 
        engine.say('Notes Taken')
        engine.runAndWait()

def show_notes():

    with open('MyNotes.txt', 'r') as f:
        task = f.read()
        task = task.split('...')
    engine.say(task[-2])
    engine.runAndWait()
    webbrowser.open('http://localhost:8888/edit/Untitled%20Folder%201/Notes.txt')

def top_news():

    url = 'https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en '
    page = requests.get(url)
    soup = sp(page.content, 'html.parser')
    news_list = soup.findAll('h3', attrs = {'class':'ipQwMb ekueJc RD0gLb'})
    for news in news_list:
        print(news.text)
        print('\n')
        engine.say(news.text)
    print('For more information visit: ', url)
    engine.say('For more information, please visit Google News')
    engine.runAndWait()

def play_video(audio):

    url = 'https://www.google.com/search?q=youtube+' + audio
    engine.say('Playing')
    engine.say(audio)
    engine.runAndWait()

    page = requests.get(url, headers = headers)
    soup = sp(page.content, 'html.parser')
    link_list = soup.findAll('div', attrs = {'class' : 'r'})
    link = link_list[0]
    link = link.find('a')
    link = str(link)
    link = link.split('"')
    link = link[1]

    webbrowser.open(link)
 
def main():

    recognizer = speech_rec.Recognizer()
    with speech_rec.Microphone() as source: 
        print('Listening')
        engine.say('Listening')
        engine.runAndWait()
        audio = recognizer.listen(source)
        audio = recognizer.recognize_google(audio)

        if 'weather' in audio:
            print('..')
            words = audio.split(' ')
            print(words[-1])
            weather_information(words[-1])


        elif 'meaning' in audio:
            print('..')
            words = audio.split(' ')
            print(words[-1])
            word_meaning(words[-1])
            
        elif 'take notes' in audio:
            print('..')
            write_notes()
            print('Noted!!')
            
        elif 'show notes' in audio:
            print('..')
            show_notes()
            print('Done')
            
        elif 'news' in audio:
            print('..')
            top_news()
            
        elif 'play' in audio:
            print('..')
            words = audio.split(' ')
            print(words[-1])
            play_video(audio)
            
        elif 'open' in audio:
            print('..')
            words = audio.split('open')
            print(words[-1])
            link = str(words[-1])
            link = re.sub(' ', '', link)
            engine.say('Opening')
            engine.say(link)
            engine.runAndWait()
            link = f'https://{link}.com'
            print(link)
            webbrowser.open(link)
            
        #     For opening link, the following can be done:
        #     link = f'https://www.google.co.in/maps/place/{link}'
        
                    
        else:
            print(audio)
            print('Sorry, I did not understand that')
            engine.say('Sorry, I did not understand that')
            engine.runAndWait()


if __name__ == "__main__":
    main()