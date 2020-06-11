I worked on the data from: https://www.tdcj.texas.gov/death_row/dr_executed_offenders.html 
My aim was to get a list of all the last statements by those who were executed and then make a WordCloud visualization of the most often words by them, WITHOUT using the wordcloud or NLP libraries.
I put the conditions being that length of words should be greater than 5, other way could have been using wordcloud library and using the stopwords method from NLP library. 
I started with spidering the data from the site,using and modifying the spider.py file from code3, used BeautifulSoup for the anchor tags ,and then again for the consequent paragraph tags, put them into a list and consequently wrote into a file. I imported that file in a datagram, cleaned it and exported it to statements.csv, which helped me in converting to sqlite. Then I modified gword.py file to get the visualization. 


Run gmane.py

One nice thing is that once you have spidered all of the messages and have them in content.sqlite, you can run gmane.py again to get new messages as they get sent to the list.  gmane.py will quickly scan to the end of the already-spidered pages and check if there are new messages and then quickly retrieve those messages and add them to content.sqlite.
The content.sqlite data is pretty raw, with an innefficient data model, and not compressed. This is intentional as it allows you to look at content.sqlite to debug the process. It would be a bad idea to run any queries against this database as they would be slow.


Run gmodel.py

model.py reads the rough/raw data from content.sqlite and produces a cleaned-up and well-modeled version of the data in the file index.sqlite.  The file index.sqlite will be much smaller (often 10X smaller) than content.sqlite because it also compresses the header and body text.
Each time gmodel.py runs - it completely wipes out and re-builds index.sqlite, allowing you to adjust its parameters and edit the mapping tables in content.sqlite to tweak the data cleaning process.
The gmodel.py program does a number of data cleaing steps


Run gbasic.py


Run gword.py
This produces the file gword.js which you can visualize using the file 
gword.htm.


A second visualization is in gline.py.  It visualizes email participation by 
organizations over time.
Run gline.py
Its output is written to gline.js which is visualized using gline.htm.

Comments welcome.
