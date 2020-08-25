# Acceptance

Ingest mixtape.json and a changesfile. The changesfile should include multiple changes in a single file: Add a new playlist; the playlist should contain at least one song. Remove a playlist. Add an existing song to an existing playlist. Output output.json using the same structure as mixtape.json with the changes applied. Add a README describing how you would scale this application to handle very large input files and/or very large changes files.

## Installation

Clone this project:
```
$ git clone https://github.com/brittanyrjones/mixtape-editor.git
```

 # Running the Script

Make sure you are in the right directory:
```
$ cd mixtape-editor
```

Now you can run the script:
```
$ python3 mixtape_editor.py mixtape.json changes
```
 
 # Scaling Up
 
 My code would not run optimally given a larger data set, with larger files. 
 In my current working example, the files being injested are being loaded into memory from
 JSON files, and then I am running CRUD on selected resources. 

I would consider making the following changes to scale up:

First of all, I would start by writing tests. It would be important to validate all objects before starting to manipulate them. 

### The Changes file ingestion 
 * Using a stream/batch based approach in reading file. 
 - Reading the changes file and writing separate files (into batches) based on intended CRUD operation. Each "CRUD" file would contain all of the related changes. If we batched the processes by action (add, delete, update), it would be easier to keep track of what has been processed in the queue.
    * One downside to this idea: What if there are 1 million delete actions, and nothing else? In this case, we should consider batching the file by line....
 - This would help with reducing memory in space needed for reading changes file. 
 - This would also be helpful for keeping records in sync, as we could lock our resources as we make changes to them.
 
 ## The Mixtape file ingestion
 * Using a database (mongodb, for example) to load data.
 * Using a stream/batch based approach in reading file. 
 - Reading the changes file and writing separate files (into batches) based on intended CRUD operation. Each "CRUD" file would contain all of the related changes. If we batched the processes by action (add, delete, update), it would be easier to keep track of what has been processed in the queue.
    * One downside to this idea: What if there are 1 million playlist actions, and nothing else? In this case, we should consider batching the file by line....
 - By loading the data into a database, it would be easier to separate smaller chunks of data to then read through.
 - It may also be easier to use a json serializing/deserializing library to read each mixtape object line by line into a Database or a new batch file, reducing the chances of running out of memory.

 ## Using multiple process 
 * Using multiple processes to read the input file into a database or batch files (the batch files then can be used in smalller chunks if a database is not an option), and also using multiple processes to write
 the changes data to the database, or batch files. 
 
 ## Refactoring the class
 I would also refactor the class to create playlist data type objects based on the file data. This would help
 with type checking the file data, and cleaning the data before it gets pushed into a database. I would also
 write a lot of different helper methods, it would be helpful for each function to have only one job, for example, 
 just adding an item, or deleting an item, instead of doing a "changes" function that does both. 
 
 # In Closing
Thank you for taking the time to check out my code! There were so many ways to do this depending on
so many factors (memory, space, budget, read/write/throughput, etc), and I appreciate you
taking the time to look see this code from my point of view. I look forward to hearing from you and the team soon, 
and take care!
 
*Brittany Jones