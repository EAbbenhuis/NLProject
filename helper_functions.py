# we need the library json as the reddit data is stored in line-delimited json objects
# (one json object in each line, with each line representing a Reddit comment)
import json

# function to load all comment data into a list of strings
# Input: the path of the file including our data
# Output: a list of strings including the body of the Reddit comments
def load_reddit_comment_data(data_directory):

    comments_data = [] # list object that will store the loaded Reddit comments

    # we first open the file that includes our dataset
    with open(data_directory, 'r', encoding='utf-8') as f:
        # iterate the file, reading it line by line
        for line in f:
            # load the data petraining to a line into a json object in memory
            data = json.loads(line)

            # append the comment if not removed
            if data['body']!="[removed]":
                comments_data.append(data['body'])

    # the method returns all the loaded Reddit comments
    return comments_data