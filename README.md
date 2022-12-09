# Voice Assistant

## The voice assistant created using Python, incorporates Web Scraping to help in tasks.

### The tasks that the voice assistant can help in are as follows:
1. Get weather information for a particular city
2. Search the meaning for a particular word
3. Write notes
4. Show existing notes
5. Show the top news
6. Play a YouTube Video

### Limitations:
The Voice Assistant uses the Speech Recognition module and the text-to-speech conversion library "pyttsx3". The "engine" used to show the results from the voice assistant incorporates the Microsoft Speech API (sapi5), which would not show the results for Mac OS X.
As an alternative, NSSpeechSynthesizer can be used for Mac OS X.

### Pointers: 
In the future, JavaScript and other tools can be incorporated to create a more interactive experience.

For further improvement in getting the weather information, Geolocation API can be used to pick up the exact current location which can be used to generate the weather information based on that location.
