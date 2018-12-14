# Transcription algorithm from Russian cyryllic to Polish latin

The aim of this algorith is to be as precise as possible, as there's currently no good apps for that—they miss on some details.
The implementation will be as flexible as possible in order to allow adding more langauges and options in future.

## Testing
Just enter the root folder of the app and run `pytest`. Ensure you have all the required dependencies by running `pip install -r requirements.txt` first.

## Contents
- `/rules` contains rules on how to transcribe various languages
- `/utils` contains all the classes and functions that operate on input data and rules
- `/tests` contains tests for all the app