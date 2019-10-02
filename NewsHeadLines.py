# Rss stands for Really Simple Syndication. It is a technology used to manage content feed

# On news websites, news is usually laid out similarly to a print newspaper with 
# more important articles being given more space and also staying on the page for longer. 
# This means that frequent visitors to the page will see some content repeatedly and have to look out for new content. 
# On the other hand, some web pages are updated only very infrequently, such as some authors' blogs. 
# Users have to keep on checking these pages to see whether they are updated, even when they haven't changed most of the time. 
# RSS feeds solve both of these problems. If a website is configured to use RSS feeds,
# all new content is published to a feed. A user can subscribe to the feeds of his or her choice and consume these using an RSS reader. 
# New stories from all feeds he or she has subscribed to will appear in the reader and disappear once they are marked as read


# WE will use a python library called feedparser to parse the Rss Feed and display it in our application
# The library abstracts away things such as different versions of RSS 
# and allows us to access the data we need in a completely consistent fashion





import feedparser   
from flask import Flask
from flask import render_template
app = Flask(__name__)

RSS_FEED = {
	
			'bbc' : 'http://feeds.bbci.co.uk/news/rss.xml',
			'cnn' : 'http://rss.cnn.com/rss/edition.rss', 
			'fox' :  'http://feeds.foxnews.com/foxnews/latest'
}

@app.route("/")
@app.route("/<publication>") #if we specify a part of our URL path in angle brackets <>, then it is taken as a variable and is passed to our application code...Ex - localhost:5000/cnn(Here publication=cnn).
def get_news(publication="bbc"): # Default publication is bbc

	feed = feedparser.parse(RSS_FEED[publication]) # Feedparser downloads the feed, parses it and returns a dictonary
	first_article = feed['entries'][0] # we grabbed just the first article from the feed and assigned it to a variable
	# Build a HTML page and display the content using the particular field('title', published,...)
	# We use placeholders
	return render_template("home.html", articles=feed['entries']) # looks in our templates directory for a file named home.html, reads this, parses any Jinja logic, and creates an HTML string to return to the user

if __name__ == '__main__':
	app.run(port=5000,debug=True)