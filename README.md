# tito
Tito Discord Bot
My first program using python
Bot uses the discord API to read messages sent on a discord server, and based on message uploads an image from a local directory.

Noteable things I learned making this:
Uses of dictionary to assign messages a key value, so that images can be called in O(1) time.
Using a .json file to hold the discord bot key, and importing the file, to maintain security and not display private key
while still being able to share the source code on GitHub.
The use of various python features such as random, asyncio, etc.

Things to add to make features more robust:
Allow users to submit images and keyword pairs which, with approval, would be added to the dictionary of keywords and associated image files.
Scrape images from image hosting services directly to bot and easily make them available.
Though I don't know how to do this currently, something I would like to do is use machine learning and web scraping to create a "tranding image", something based on any image that is trending on twitter, facebook, etc. and have the trending image update each day.
Host the bot on a VM server to allow for continuous uptime, rather than just running it from my PC.
