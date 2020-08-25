import argparse
import json
import os

import sys


class Mixtape_Editor:
    # When refactoring for optimal code, I would initialize my class with the changes and mixtape data, and objects needed
    # for logging. I would also use way more helper functions, for typechecking and to simplify
    # adding, deleting, and updating items.
    # I would also be more specific about the structure of each input object for the class functions

    # ex.

    # def __init__(self, mixtape_data, changes_data):
        # self.logger = logger
        # self.mixtape_data = mixtape_data
        # self.changes_data = changes_data

    def run_mixtape_object_edits(self, mixtape_data: dict, change_object: dict):
        '''
        This function consumes mixtape data object, changes object. 
        The data is parsed from the changes, and depending on the action being taken (add or delete),
        the function will determine which item should be acted upon, and from which object (users, playlists, songs)
        it should be acted upon in the within the mixtape.

        params - dict: mixtape_data
                 dict: change_object
        '''

        for key, value in mixtape_data.items():
            # Delete mixtape object
            if change_object['action'] == "delete":
                for item in value:
                    # making sure they are the same key, and same id.
                    if change_object['id'] == item['id'] and change_object[
                            'type'] == key:
                        value.remove(item)
            
            # Add mixtape object
            elif change_object['action'] == "add":
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


    def get_data(self, input_file :str):
        '''
        This function takes in a file, and returns the data as a dict.

        params - str: input file
        '''
        
        data = {}
        if not os.path.exists(input_file):
            sys.exit(f'ERROR: unable to locate file {input_file}')

        with open(input_file) as infile:
            input_object = json.load(infile)

        data.update(input_object)

        return data
        
    def output_data(self, data, output_file):
        '''
        This function takes in data, and an output file. The data is dumped 
        to the output file, output.json

        params - dict: data 
                 str: output file
        '''

        with open(output_file, 'w') as outfile:
            # Keeping the format EXACTLY the same
            json.dump(data, outfile, indent=2, separators=(',', ' : '))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=
        '')
    parser.add_argument('mixtape', required=True)
    parser.add_argument('changes', required=True)

    if len(sys.argv) < 2:
        sys.stderr.write('Usage: ')
        sys.exit(1)
    else:
        args = parser.parse_args()

        mixtape_editor = Mixtape_Editor()

        mixtape_data = mixtape_editor.get_data(args.mixtape)
        changes_data = mixtape_editor.get_data(args.changes)

        for key, value in changes_data.items():
            for change_item in value:
                mixtape_editor.run_mixtape_object_edits(mixtape_data, change_item)

        mixtape_editor.output_data(mixtape_data, 'output.json')   
    