# Project 2
Reference : Tweepy link "https://docs.tweepy.org/en/latest/#" use the library and most model here. GoogleNLP model can be checked at the offical website. If using python: "https://codelabs.developers.google.com/codelabs/cloud-natural-language-python3"
# Phase 1
Twitter delayed the developer account application. Notified at the beginning.

Twitter:
Make sure to use the command install tweepy, after choosing the command, find function names in this given verison library.

For example, some verisions have function name as "search_id" insead of "search"
```
pip install tweepy
```
Then from your Twitter developer account, download your keys. Use the following code to connect to your account
```
import tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
```
After all settings, apple model and edit code to test the features of twitter api.

GoogleNLP:
To set the googleNLP, we need to have the google cloud account open and create a project. 

Under the project, create a key and download it. Make sure enable API for this project.

If you choose key as a json file, apply CREDENTIALS for google by
```
set GOOGLE_APPLICATION_CREDENTIALS=KEY_PATH
```
using cmd, or PowerShell
```
$env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"
```
Every time open a new cmd, you need to redo the above code, or you can write it in code to avoid reset.

Also you need to download the Google Cloud SDK Shell to link to your cloud. After the setting, you can apply the code.
# Phase 2
For my use case, I plan to let users to find the most recent news or information that related with their search key words. And the Google NLP can analysis and give a semtiment score and magnitude towards these tweets's  information. For example, someone tries to find out what's going on in Boston this week.

You can read and write the results from tweet file and import in google NLP to get the analysis result by
```
f=open("tweets.txt","w",encoding='utf-8')
     
for line in search_tweets():
    f.write(line+'\n')
f.close()
```
What I do here is to type key words "Boston" and most recent 10 tweets from September.
In text file I find the result as

```
RT @BleacherReport: RED SOX WALK IT OFF IN THE 13TH 😱 @BRWalkoff

Christian Vásquez gives Boston a 2-1 series lead https://t.co/ke6sWtMawS
BOSTON STRONNNGGG https://t.co/pTJSQSZ1zp
Im so glad i didnt go to boston, id be in jail tonight
RT @KFILE: Team Beans, if you got a Team Beans Boston Marathon shirt. 
We'd love if posted a photo of yourself in it tomorrow with the hasht…
RT @BleacherReport: RED SOX WALK IT OFF IN THE 13TH 😱 @BRWalkoff

Christian Vásquez gives Boston a 2-1 series lead https://t.co/ke6sWtMawS
@TBTimes_Rays Can you explain why Interference wasn’t called when Boston’s 1 st basemen tripped Arozerena??
Man do I wish I was in Boston right now #electric
WHAT A WAY TO END IT!!!

AFTER 5+ HOURS WE’VE GOT PANDEMONIUM IN BOSTON 
 https://t.co/sp4GQVmTfl
 To be clear, the *regular* ground-rule double rule also creates a lot of unfair/nonsensical situations 
 w/r/t runner… https://t.co/q9b1Kv0ILB
RT @BleacherReport: RED SOX WALK IT OFF IN THE 13TH 😱 @BRWalkoff

Christian Vásquez gives Boston a 2-1 series lead https://t.co/ke6sWtMawS

```
Score: 0.0%

Magnitude: 310.00%

Another of the example is to deal with the COVID news and we can see the difference with the one th key words "Boston" above
```
RT @SallyLawry: What @Barnaby_Joyce doesn’t realise it is the regions in WA that are at the greatest risk of Covid .
People from metro WA a…
RT @DmSambalpur: Helpline numbers for Covid-19 Vaccination for the  citizens who are bed-ridden or 
having extreamly restricted mobility or…
RT @skye_daddy: Yeah yeah yeah and our weapon of mass destruction is asymptomatic covid..we know, 
we know… https://t.co/DW4VEESLwY
RT @drdavidsamadi: We need to know the origins of COVID-19 so we can make sure 
we NEVER have another virus like it again!

This is not poli…
RT @benheck: 3 word solution to weak job reports/labor shortage: DITCH THE MASKS. Now, 
all the COVID-Karens who make 6 figure salaries work…
RT @OttenbergEve: Cuba leads global covid vaccine rates per 100 inhabitants, Telesur reports. 
It also developed 5 vaccines including pediat…
RT @SeguraOSD: I'm sick with #COVID, but working on some #OSDBuilder updates. Hello #Windows11 ... 
goodbye #Windows7 #Server2016 #Windows10…
RT @TheLastRefuge2: Eleven simple truths, you can fact check, that tell you all of 
these government COVID rules are not about health.

1) W…
RT @ElectionWiz: REPORT: The union representing pilots for American Airlines warned the company 
could face a staffing shortage ahead of the…
RT @BrianMteleSUR: Public prosecutors investigate claims that the Brazilian Army stationed Captains 
in military hospital consulting rooms i…
```

score     : -30.0%
magnitude : 580.0%


