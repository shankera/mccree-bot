# mccree-bot
A mccree bot for slack

Source tutorial on [FullStackPython.com](https://www.fullstackpython.com/blog/build-first-slack-bot-python.html).

##Instructions
###Version 1
 - install [pip](https://pip.pypa.io/en/stable/) and [virtualenv](https://virtualenv.pypa.io/en/stable/)
 - clone this repository to a directory
 - create a file called `.botkeys` in the `Version1` directory, and add your slack bot api-keys to it
 - run `mccree.sh` as a bash script

###Version 2
 - add your slack bot api key to your Heroku app with the key `MCCREE_GB_BOT_ID`
 - push your local fork of this repository to your Heroku app
 - deploy build on Heroku

If you encounter an InsecurePlatformWarning, either ensure that you are on python version 2.7.9 or follow the steps in [this StackOverflow post](http://stackoverflow.com/questions/29134512/insecureplatformwarning-a-true-sslcontext-object-is-not-available-this-prevent).
