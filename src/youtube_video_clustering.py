#Noah Hansen and Angela Gentile
#5/4/2020
#CS484
#Professor Barbara
import numpy as np
import matplotlib.pyplot as plt
import pandas
import seaborn as sns
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

def main():
    #---------------------------------------------------------------------------
    # LOAD IN THE DATA
    # We load in data from the file ../youtube_data/USVideos.csv
    # Data is read in from this format -->
    #   video_id,trending_date,title,channel_title,category_id,publish_time,tags,
    #   views,likes,dislikes,comment_count,thumbnail_link,comments_disabled,
    #   ratings_disabled,video_error_or_removed,description
    # (without newlines)
    # we use the pandas package here because it's an easy one liner
    #---------------------------------------------------------------------------

    data = pandas.read_csv("../youtube_data/USvideos.csv")

    #---------------------------------------------------------------------------
    # LINEAR REGRESSION
    # we will use linear regression in order to properly predict the Number
    # of likes in the video.
    #
    # DEFINITIONS OF VARS
    # xc = number of video views
    # yc = number of likes (what we are trying to predict)
    # cc = number of comments
    # dl = number of dislikes
    #---------------------------------------------------------------------------

    xc = np.array(data["views"])
    yc = np.array(data["likes"])
    cc = np.array(data["comment_count"])
    dl = np.array(data["dislikes"])

    ###
    #NOTES ON ADDITIONS THAT DIDN'T DO ANYTHING
    #I attempted to add the category_id as a vector but it saw no improvement
    #---
    #I also added comments_disabled as a vector and it didn't improve it at all \
    #---
    #Lastly I added title as a vector and converted the title to an integer and
    #this also did nothing.
    #NOTES ON ADDITIONS THAT DIDN'T DO ANYTHING
    ###

    ###
    #NOTES ON ADDITIONS THAT WORKED
    #the "cc" array or "comment_count" array originally didn't exist. I added
    #the vector to raise the accuracy from 72% to 83%
    #---
    #the "dl" arr or "dislikes" array was added to bring up accuracy from 83% to
    #88%
    #NOTES ON ADDITIONS THAT WORKED
    ###
    xc = xc[:, None]
    cc = cc[:, None]
    dl = dl[:, None]

    xc = np.append(xc, cc, axis=1)
    xc = np.append(xc, dl, axis=1)


    yc = yc[:, None]

    xc_train = xc[:len(xc)//2]
    xc_test = xc[len(xc)//2:]
    yc_train = yc[:len(xc)//2]
    yc_test = yc[len(xc)//2:]

    regr = linear_model.LinearRegression()
    regr.fit(xc_train, yc_train)

    yc_pred = regr.predict(xc_test)

    print('Coefficients: \n', regr.coef_)
    # The mean squared error
    print('Mean squared error: %.2f' % mean_squared_error(yc_test, yc_pred))
    # The coefficient of determination: 1 is perfect prediction
    print('Coefficient of determination: %.2f' % r2_score(yc_test, yc_pred))

    #---------------------------------------------------------------------------
    #PLOT THE DATA
    #---------------------------------------------------------------------------
    x1 = np.log(data["likes"])
    y1 = np.log(data["views"])
    y2 = np.log(data["dislikes"])
    y3 = np.log(data["comment_count"])

    #---------------------------------------------------------------------------
    # LIKES v VIEWS
    #---------------------------------------------------------------------------
    sns.regplot(x=x1,y=y1,fit_reg=False)
    plt.show()
    plt.close()

    #---------------------------------------------------------------------------
    # LIKES v DISLIKES
    #---------------------------------------------------------------------------
    sns.regplot(x=x1,y=y2,fit_reg=False)
    plt.show()
    plt.close()

    #---------------------------------------------------------------------------
    # LIKES v COMMENTS 
    #---------------------------------------------------------------------------
    sns.regplot(x=x1,y=y3,fit_reg=False)
    plt.show()
    plt.close()







if __name__ == "__main__":
    main()
