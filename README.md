# Capstone Project, Group 8

John Espinoza, Tom Stowell, Choua Vang, Juniper Cherne, Zach Diercks

## Executive Summary

### Introduction
The purpose of our project is to create a recommender model that will allow a user to get song recommendations they may enjoy.  We utilized a Kaggle Spotify Dataset sampling over 600,00 songs to build our model from.  Our inspiration came from our love of music and that regardless of anyone’s demographics can listen to their favorite songs and artists.  Our expectation from our model is to provide 10 songs that are similar to the user’s input.  The recommender model is based on multiple song characteristics and audio features of each song within our dataset. 

### Machine Learning Recommender
Once our data was cleaned, we imported our cleaned csv’s and reviewed the correlations to identify which features would help us make accurate song recommendations.  The features we chose to focus on were popularity, duration, explicit, danceability, energy, key, mode, speechiness, acoustics, instrumentals and valence.  These features had the highest correlation which meant they would be the most helpful in accurately suggesting similar songs for the user.  The algorithm utilized for the song recommender is the Nearest Neighbors method form scikit-learn. The principle behind nearest neighbor methods is to find a predefined number of training samples closest in distance to the new point and predict that label from these. We established the knn model utilizing the select metric, alogorithm, and number or n_neighbors.  From there we fit the KNN_top_Tracks_proc dataframe with the generated knn model and used these to develop the recommender model.

![webpage](https://github.com/junipear21/capstone-group-8-Spotify/blob/main/Zach%20Work/Recommender%20code%20pic.png)

### Tableau
We created two dashboards for our web page.  Between the two dashboards the users can explore our data at a high level with visualizations that focus on artist and genre popularity and how music popularity and audio features have changed over time by utilizing the global filters that have been added to the dashboards for effortless use.  Within each dashboard you will have the ability to filter by a specific genre to focus on popular artists or by the artist to identify their overall popularity rating.  You will also be able to review how genres popularity and audio features have changed over the past sixty years to identify trends.

### Web page
Our webpage design was selected from StartBootstrap.com templates. Using CSS stylesheets and HTML we made customizations to the template. This template was selected not only for its simple look but also for its easy-to-use functions that allows for continued user engagement throughout the page. The navigation bar is easily accessible and utilized throughout the user’s time on our page. It includes buttons to navigate the user to specific sections and back to the top of the page.  We utilized the official Spotify Colors as our scheme for the webpage (RGB, CMYK, Pantone, Hex).  Additionally, we added the feature to play a song we imbedded within our webpage from Spotify.

![webpage](https://github.com/junipear21/capstone-group-8-Spotify/blob/main/Zach%20Work/Recommender%20web%20pic.png)

### Conclusion
We created a machine learning recommender model that we feel users can rely on to provide song recommendations similar to their user input.  The machine learning recommender model along with our tableau dashboards and designed web app not only provides song recommendations for the user, but also tells a story of who the most popular artists are based on Spotify records and tells a story of how music has changed over the last sixty years.  The user has the ability to input their song selection and interact with both dashboards to learn more about the attributes that contribute to the recommender model.   

#### Webpage
https://mycapstone-group-8-song-rec.herokuapp.com/

#### Tableau Dashboards
https://public.tableau.com/app/profile/tom.stowell8009/viz/Spotify-test/Dashboard1?publish=yes

https://public.tableau.com/views/Spotify_Dashboard_16612875479370/Dashboard2?:language=en-US&:display_count=n&:origin=viz_share_link