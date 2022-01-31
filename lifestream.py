#!/usr/bin/python
# coding=utf-8

import feedparser
from dateutil.parser import parse
import datetime
import time

entries = []

def build_entries():
    for line in open('sources.txt'):
        add_entries(line)

def add_entries(link):
    try:
        d = feedparser.parse(link)
    except:
        return

    feed_title = d.feed.get('title', '')
    feed_description = d.feed.get('description', '')

    if 'image' in d.feed: 
        feed_image = d.feed.image.get('href', '')
    else:
        feed_image = ''

    for x in range(0, 10):
        try:
            e = d['items'][x]
        except:
            return

        # Thumbnail handling
        try:
            if 'url' in e.media_thumbnail[0]:
                feed_post_image = e.media_thumbnail[0].get('url')
            else:
                feed_post_image = ''	
        except:
            feed_post_image = ''

        # site specific formatting fixes
        if link.find('newsblur') != -1:
            feed_summary = 'Shared from <a href="https://pdp68.newsblur.com/">NewsBlur</a>'
        elif link.find('xiffy') != -1:
            feed_summary = 'Loved on <a href="https://www.last.fm/user/expatpaul">Last.fm</a>'
        elif link.find('letterboxd') != -1:
            if e.summary.find('<img') == -1:
                feed_summary = e.summary
            else:
                gFrom = e.summary.find('</p> <p>')
                gString = e.summary[ : gFrom] + ' ' + e.summary[gFrom + 8: ]
                gFrom = gString.find('img src')
                gFrom = gString.find('/>', gFrom)
                feed_summary = gString[3 : gFrom] + ' width="50" height="75" align="right" ' + gString[gFrom : len(gString) - 4]
        else:
            try:
                feed_summary = e.summary
            except:
                feed_summary = ''

        if link.find('goodreads') != -1:
            feed_image = ''

        if link.find('github') != -1:
            feed_post_image = ''

        try:
            feed_published_parsed = e.published_parsed
        except:
            feed_published_parsed = ''

        try:
            feed_link = e.link
        except:
            feed_link = ''

        try:
            feed_title = e.title
        except:
            feed_title = ''

        try:
            feed_published = e.published
        except:
            feed_published = ''

        if feed_link != '':
            entries.append([feed_published_parsed, feed_title, feed_image, feed_description, feed_link, feed_title, feed_published, feed_summary, feed_post_image])

def display_entries():
    entries.sort(key = lambda row: row[0], reverse = True)
    count = 0
    olddate = ''
    for x in entries:
        newdatetime = datetime.datetime.fromtimestamp(time.mktime(x[0]))
        newdate = newdatetime.strftime("%A %d. %B %Y")
        if newdate != olddate:
            olddate = newdate
            print('<h2>' + newdate + '</h2>')
        
        print('<div id=post>')
        print('<h3>')
        if x[2] != '':
            print('<img src="' + x[2] + '" align="left" width="32" height="32" />')
        print('<a href=\'' + x[4] + '\'>' + x[5] + '</a>')
        print('</h3>')

        if x[8] != '':
            print('<a href=\'' + x[4] + '\'><img src="' + x[8] + '" height="200" /></a>')
            print('<br />')


        print('<p>', x[7], '</p>')
        print('<br />')
        print('</div>')

        count += 1
        if count == 20:
            break

def print_heading():
    heading = '''<!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8"/>
    <title>The Lightly Seared Life Stream</title>
    <link rel="icon" href="icon.png?w=32" sizes="32x32" />
    <link rel="icon" href="icon.png?w=192" sizes="192x192" />
    <style>
        <!--
        body {margin: 1%; color: black; background: white;}
        div#headerimage {background: green url("banner.jpg") center no-repeat; background-size: cover; height: 300px; position: relative;}
        .heading {text-align: center; color: white;} 
        h1.heading {font-style: italic; position: absolute; top: 0; bottom: 0; left: 0; right: 0; width: 50%; height: 30%; margin: auto; }
        div#content {text-align: justified; margin-left: 20%; margin-right: 20%; padding: 0 1.75em;} 
        div#post {margin-left: 5%;}
        a:hover {color: red; }
        -->
    </style>    
    </head>
    <body>'''
    print(heading)

    banner = '''<div id=headerimage><h1 class=heading>Lightly Streamed on the Reality Grill</h1></div>'''  
    print(banner)            

    print('''<div id=content>''')

def print_tail():
    tail = '''</div></body></html>'''
    print(tail)

def main():
    build_entries()
    print_heading()
    display_entries()
    print_tail()

if __name__ == "__main__":
    main()
