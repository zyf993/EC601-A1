from google.cloud import language

def analyze_text_sentiment(text):
    #Instantiates a client
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)
    #Call API to analyze text
    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = dict(
        text=text,
        score=f"{sentiment.score:.1%}",
        magnitude=f"{sentiment.magnitude:.1%}",
    )
    for k, v in results.items():
        print(f"{k:10}: {v}")

f = open("tweets.txt","r",encoding='utf-8')
text = f.read()  
f.close()
#can be import from tweet file
analyze_text_sentiment(text)
