# twitterDB

Mainly two python scripts (twitterdb.py,tweetsSentiments.py) , Run first twitterdb.py then tweetsSentiments.py 

    - twitterdb.py -Fetches tweets from twitter based on hashtags and stores them into database
    - tweetsSentiments.py -Fetches tweets from Database and calculate Sentiments

Need few things before this to get started

    - A Twitter account and API credentials
    - A MySQL database
    - The Tweepy and mysql-connector Python Libraries
    
Run twitter.py file an PythonRich IDE - 

1. Account at https://developer.twitter.com then create an app to access these four keys,
   - consumer_key
   - consumer_secret
   - access_token
   - access_token_secret
2. Mysql local database ( for ex. in my case it is 'twitterdb' ) create table in your database accordingly with column names - 
      - username: VARCHAR(255)
      - created_at: VARCHAR(45)
      - tweet: TEXT
      - retweet_count: INT(11)
      - location: VARCHAR(100)
      - place: VARCHAR(100)
  
  Query -------
  
  CREATE TABLE `Golf` ( `username` varchar(255) DEFAULT NULL, `created_at` varchar(45) DEFAULT NULL,
        `tweet` varchar(255) DEFAULT NULL,  `retweet_count` int(11) DEFAULT NULL,
        `location` varchar(100) DEFAULT NULL,  `place` varchar(100) DEFAULT NULL )
