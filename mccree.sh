#!/bin/bash
# all of the junk to run mccree bot


#Uncomment any following lines if this is your first run
#virtualenv mccree
source mccree/bin/activate
#pip install slackclient
for key in `cat .botkeys`; do
    export MCCREE_BOT_TOKEN=$key
    export MCCREE_ID=$(python print_bot_id.py 2>&1)
    nohup python mccree.py &
done

#export MCCREE_BOT_TOKEN=''
#export MCCREE_ID=$(python print_bot_id.py 2>&1)
#nohup python mccree.py &
