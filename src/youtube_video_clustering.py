#Noah Hansen and Angela Gentile
#5/4/2020
#CS484
#Professor Barbara
import numpy as np
import csv

def main():
    #---------------------------------------------------------------------------
    # LOAD IN THE DATA
    # We load in data from the file ./youtube_data/USVideos.csv
    # Data is read in from this format -->
    #   video_id,trending_date,title,channel_title,category_id,publish_time,tags,
    #   views,likes,dislikes,comment_count,thumbnail_link,comments_disabled,
    #   ratings_disabled,video_error_or_removed,description
    # (without newlines)
    #---------------------------------------------------------------------------

    ###
    # load in column IDs first
    # Column IDs is an array that allows us to determine what each column means
    #
    # Next (in the same for loop) load in the rest of the data into a NumPy array
    ###

    columnID = []
    data = []
    count = 0
    with open("../youtube_data/USVideos.csv", 'r+') as csvfile:
        read = csv.reader(csvfile, delimiter=',', quotechar='|')
        for i in read:
            if count == 0:
                columnID = i
                count += 1
            else:
                data.append(i)
    dataNumpy = np.array(data)

     




if __name__ == "__main__":
    main()
