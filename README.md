# Madrix_text_analysis
## Team: Madrix  

Team members:
- Aishwarya Ponni P
- Akilandeshwari R
- Indu Subramaniam
- Indu Subramanian

### Hacakthon Domain: AI/ML for human development  

### Problem Statement Chosen: Text Sentiment Analysis - trying to get emotion from text

Development tools: Google Colaboratory, VSCode  
Front-end: HTML Bootstrap  
Web framework: Python Flask  

Python packages used: numpy, pandas, sklearn, tensorflow, pickle  

### Abstract: 
The **objective** of this project is to perform **text sentiment analysis** - to find emotion by text. The datasets were obtained from Kaggle.  
IMDB review dataset for sentiment analysis: https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews  
Classes: 'positive' or 'negative' sentiment.  
**Models used**: Support Vector Machine, Logistic Regression, Bidirectional Long Short Term Memory network  
**SVM provided the highest accuracy of 88.94%**. It was deployed using Flask.    
On the website, tamil words can be written in english, which will be transliterated to Tamil and translated to English. The model predicts output on the English sentence.  

Emotions dataset for emotion classification: https://www.kaggle.com/praveengovi/emotions-dataset-for-nlp  
Classes: 'joy', 'sadness', 'anger', 'fear', 'surprise', 'love'.  
**Model used:** Bidirectional Long Short Term Memory with Embedding and Dense layers  
**Training accuracy: 93.98%**  
**Validation accuracy: 88.16%**  
The model thus developed was deployed as a chatbot which could detect the emotion of a given text and respond accordingly.  

Thus sentiment and emotion analysis can be performed on huge corpora and can provide wider insights into the society's mental state. As the amount of textual data available in the form of news articles, tweets and social media posts increases, these models will prove to be very useful for analyses. 

### User Interface: 
**Senti Text Webpage for Sentiment Model**
![SentiHome page](Images/SentiText_Homepage.png?raw=true "Optional Title")
![SentiText_English](Images/SentiText_English.png?raw=true "Optional Title")
![SentiText_Tamil](Images/SentiText_Tamil.png?raw=true "Optional Title")

**EmCee ChatBot for Emotional Model** <br /> <br />
![EmCee Chat1](Images/ChatBot2.png?raw=true "Optional Title")
![EmCee_Chat2](Images/ChatBot3.png?raw=true "Optional Title")
