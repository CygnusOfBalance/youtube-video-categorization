#Noah Hansen and Angela Gentile
#5/4/2020
#CS484
#Professor Barbara
import numpy as np
import csv
import json

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
        read = csv.reader(csvfile, delimiter=',', quotechar='"')
        for i in read:
            if count == 0:
                columnID = i
                count += 1
            else:
                data.append(i)
    dataNumpy = np.array(data)

    #print(columnID)
    #print(dataNumpy[0])

    #---------------------------------------------------------------------------
    # CATEGORIZE BASED ON ID
    # the data comes with an "ID" column in which the uploaders of the video
    # can manually categorize their videos.
    # We can use this for either straight up categorizing our videos OR as a
    # means of cross validation
    #---------------------------------------------------------------------------

    ###
    # Load in JSON categories file into a dictionary
    # dict format: {Category ID : Category String}
    #   ID is a number representing the category id
    #   String is just the exact category i.e. "Automobiles"
    ###
    f = open("../youtube_data/US_category_id.json", "r+")
    js = json.load(f)
    categories = {}

    for i in range(len(js["items"])):
        categories[js["items"][i]["id"]] = js["items"][i]["snippet"]["title"]

    #print(categories["24"])

    ###
    #place videos in their proper categories
    ###
    categorizedVideos = {}
    count = 0
    for i in dataNumpy:
        x = str(i[4])
        if x in categorizedVideos and count != 0:
            categorizedVideos[x].append([(i[2], categories[x], count)])
        elif count != 0:
            categorizedVideos[x] = [(i[2], categories[x], count)]
        count += 1

    for i in categorizedVideos:
        print(i + ":")
        for x in categorizedVideos[i]:
            print("\t" + str(x))
        print()






if __name__ == "__main__":
    main()
