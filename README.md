PyLifestream

A simple lifestream written in python.

Not included is: 
- The banner image. You will need a `banner.jpg` located in the same folder as the script for this
- The site icon. You will  need an `icon.png` file located in the same folder for this.
- A list of sources. This should be handled using a `sources.ini` file. 

The sources.ini file needs the following:
- Each feed is a separate section. The section header as the Feed title.
- Each section needs a key/value of `RSS` and the URI to the RSS feed.
- Optionally, a section can have a `summary` key. Any value here overrides the summary text from the feed.
- Optionally, a section can have a `HidePostTitle` boolean key. A value of yes in here causes the post title to be not displayed.
