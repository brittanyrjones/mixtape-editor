import json
import sys
import os
import multiprocessing as mp

# import argparse

# If scaling up, I would use a class with more helper methods
# VS having 3 functions doing the work.
# In the class (or classes), it would be easy to define specific attributes
# for each object. I was thinking, it would be important to
# normalize the mixtape data, maybe by creating a class object of mixtape
# and then initializing that class with all of the attributes that the
# mixtape needs to be considered valid. That way, it would be less complex
# and more DRY to type check when adding and deleting mixtape items.


def delete_mixtape_object(mixtape_data: dict, change_object: dict):
    '''
    This function consumes mixtape data object, and dumps
    it into an output file.

    params - dict: mixtape_data
    '''
    # Delete mixtape object
    for key, value in mixtape_data.items():
        for item in value:
            # making sure they are the same key, and same id.
            if change_object['id'] == item['id'] and change_object[
                    'type'] == key:
                value.remove(item)

def add_mixtape_object(mixtape: dict, change_object: dict):
    '''
    This function will first check to change object action. If the action
    is add, we look through each key value pair and assert that if the change object is
    playlist and the key to the mixtape objects we are looping though is also playlist,
    then we can assume we are adding the playlist(change object) into the correct key value.
    We then assert that if the change object type is song, a song is being added and also 
    if the key is playlist, then a song is being added to a playlist. 

    params - dict: change_object
             dict: mixtape
    '''

    # before adding and item, it would be good to make sure the item_id
    # doesnt already exist within the dataset.
    # in the real world data with large data sets that
    # arent created by me, there can be no
    # certainty. It would help to assure the data is clean either
    # by using a certain database, or manually clean the data,
    # by writing some lines that will randomize and check for dup item id numbers.

    # Add a playlist. 
    for key, value in mixtape_data.items():
        if change_object['type'] == 'playlists' and key == 'playlists':

            value.append({
                "id": change_object['id'],
                "user_id": change_object['user_id'],
                "song_ids": change_object['song_ids']
            })

        # Adds a song to an existing playlist
        if change_object['type'] == 'songs' and key == 'playlists':
            for item in value:
                if change_object['playlist_id'] == item['id']:
                    item['song_ids'].append(change_object['id'])

#TODO: MUTLIPROCESS THE DATA IN MEMORY
def get_data(input_file :str):
    '''
    This function takes in data from a file, and returns that data as a dict.

    params - str: input file
    '''
    

    data = {}

    if not os.path.exists(input_file):
        sys.exit(f'ERROR: unable to locate file {input_file}')

    with open(input_file) as infile:
        input_object = json.load(infile)

    data.update(input_object)

    return data


# Since we know exactly what we want to injest, im going to keep it simple
# by just checking that all 3 arguments are there, and printing out
# a basic usage if there is an argument(input file) missing.
if sys.argv[1] != "mixtape.json" or len(sys.argv) < 3:
    sys.exit(f'Usage: {sys.argv[0]} mixtape.json changes')

mixtape_data = get_data(sys.argv[1])
changes_data = get_data(sys.argv[2])

for key, value in changes_data.items():
    for change_item in value:
        if change_item['action'] == 'add':
            add_mixtape_object(mixtape_data, change_item)
        if change_item['action'] == 'delete':
            delete_mixtape_object(mixtape_data, change_item)
            
#TODO: MUTLIPROCESS THE DATA writing

with open('output.json', 'w') as outfile:
    json.dump(mixtape_data, outfile, indent=2, separators=(',', ' : '))

# execute_changes("changes.json")

# parser = argparse.ArgumentParser()

# parser.add_argument("-c", "--change", help="Password")
# parser.add_argument("-m", "--mixtape", help="Size")

# args = parser.parse_args()

# mixtape_data = get_data(args.mixtape)

# print(mixtape_data)
