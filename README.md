# mixtape-editor
ingest input, ingest changes to that input, produce output, using batches

For this exercise, you will write 3 functions for a command-line batch application. Highspot's product leverages batch processing so this exercise is relevant to real-life Highspot engineering work.This should take between one and two hours to complete.

IMPLEMENTATION SUMMARY
Your application will
- Ingest an input JSON file which we will provide, mixtape.json.
- Ingest a changes file which you will create.
- Produce output.json which must have the same structure as the mixtape.json input.
- You choose the format for the changes file -text, YAML, CSV, JSON, etc.  
- Your application will apply the changes from the change file to the mixtape.json data, and produce output.json.


REQUIREMENTS
Ingest mixtape.json and a changes file.  
The changesfile should include multiple changes in a single file:
* Add a new playlist; the playlist should contain at least one song.
* Remove a playlist.
* Add an existing song to an existing playlist.
Output output.json using the same structure as mixtape.json with the changes applied.
Add a README describing how you would scale this application to handle very large input files and/or very large changes files.

EVALUATION CRITERIA
Are all requirements met?
Does the application run successfully on a Mac or Linux?
Does your README explain how to run your application?
Have you provided justification(s) in your scaling discussion?
