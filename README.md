# Madrix_text_analysis
## Team: Madrix  

Team members:
- Aishwarya Ponni P
- Akilandeshwari R
- Indu Subramaniam
- Indu Subramanian

### Abstract: 
The **objective** of this project is to perform **text sentiment analysis** - to find emotion by text. The datasets were obtained from Kaggle. 
IMDB review dataset for sentiment analysis: https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews  
Classified as 'positive' or 'negative' sentiment.  
**Models used**: Support Vector Machine, Logistic Regression, Bidirectional Long Short Term Memory network  
**SVM provided the highest accuracy of 88.94%**. It was deployed using Flask.    
On the website, tamil words can be written in english, which will be transliterated to Tamil and translated to English. The model predicts output on the English sentence.  

Emotions dataset for emotion classification: https://www.kaggle.com/praveengovi/emotions-dataset-for-nlp  
Classified as 'joy', 'sadness', 'anger', 'fear', 'surprise', 'love'.  
**Model used:** Bidirectional Long Short Term Memory with Embedding and Dense layers  
**Training accuracy: 93.98%**  
**Valiation accuracy: 88.16%**  
The model thus developed was deployed as a chatbot which could detect the emotion of a given text and respond accordingly.  

Thus sentiment and emotion analysis can be performed on huge corpora and can provide wider insights into the society's mental state. As the amount of textual data available in the form of news articles, tweets and social media posts increases, these models will prove to be very useful for analyses. 
