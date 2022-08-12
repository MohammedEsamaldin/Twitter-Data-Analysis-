import unittest
import pandas as pd
import sys, os

sys.path.append(os.path.abspath(os.path.join("C:/Users/mohammed/Desktop/Twitter-Data-Analysis-")))

from extract_dataframe import read_json
from extract_dataframe import TweetDfExtractor

# For unit testing the data reading and processing codes, 
# we will need about 5 tweet samples. 
# Create a sample not more than 10 tweets and place it in a json file.
# Provide the path to the samples tweets file you created below
sampletweetsjsonfile = "C:/Users/mohammed/Desktop/Twitter-Data-Analysis-/sampletweets_10.json"   #put here the path to where you placed the file e.g. ./sampletweets.json. 
tweet_list = read_json(sampletweetsjsonfile)

columns = [
    "created_at",
    "source",
    "original_text",
    "clean_text",
    "sentiment",
    "polarity",
    "subjectivity",
    "lang",
    "favorite_count",
    "retweet_count",
    "original_author",
    "screen_count",
    "followers_count",
    "friends_count",
    "possibly_sensitive",
    "hashtags",
    "user_mentions",
    "place",
    "place_coord_boundaries",
]


class TestTweetDfExtractor(unittest.TestCase):
    """
		A class for unit-testing function in the fix_clean_tweets_dataframe.py file

		Args:
        -----
			unittest.TestCase this allows the new class to inherit
			from the unittest module
	"""

    def setUp(self) -> pd.DataFrame:
        self.df = TweetDfExtractor(tweet_list[:5])
        # tweet_df = self.df.get_tweet_df()

    def test_find_statuses_count(self):
        self.assertEqual(
            self.df.find_statuses_count(), [888,1597,2293,44,1313]
        )

    def test_find_full_text(self):
        text = [
            '''#Pelosi airplane landed safely in #Taiwan ðŸ‡¹ðŸ‡¼ 1) - Both ðŸ‡¨ðŸ‡³ &amp;  ðŸ‡ºðŸ‡¸ are playing ""win win"" on financial markets. 2) - Taiwan may be the future Asian   Cuba  3) - ðŸ‡ºðŸ‡¸ &amp; ðŸ‡¨ðŸ‡³ need an Asian #NATO / #5G What's your thoughts?" ''', '''"Watch the video of the beginning of the Chinese bombing of Taiwan during Pelosi visit from here : https://t.co/twah6WU4fZ
                Ù€Ù€Ù€Ù€Ù€Ù€Ù€Ù€Ù€Ù€Ù€Ù€Ù€Ù€Ù€Ù€Ù€Ù€Ù€Ù€Ù€Ù€Ù€Ù€Ù€Ù€ #Pelosi #ãƒžãƒ„ã‚³ã®çŸ¥ã‚‰ãªã„ä¸–ç•Œ #Yediiklim #BadDecisionsTrailer1 #LawnBowls #ç¥_CALL119_MV900ä¸‡å›ž #à¸¡à¸²à¸à¸­à¸”à¸à¸±à¸™à¸™à¸°à¸‹à¸µà¸žà¸¤à¸à¸©à¹Œ https://t.co/m4CXfyZRS7"
                ''','''"#Pelosi #Taipei #taiwan #XiJinping  #China  On a verge of another war https://t.co/DuqDiSnWcd" ''','''#HOBIPALOOZA #LaAcademiaExpulsion #WEURO2022 #jhopeAtLollapalooza #SuzukiPakistan #Fantastico #Taiwan #breastfeeding #Kosovo #BORNPINK  strong âœï¸ðŸ’œ https://t.co/GtZeNL24rm
                ''', '''"#Pelosi #china China Time âœŒï¸ https://t.co/tEDjzTlszu" '''
                ]

        self.assertEqual(self.df.find_full_text(), text)

    def test_find_sentiments(self):
        self.assertEqual(
            self.df.find_sentiments(self.df.find_full_text()),
            ([0.30 ,0 ,0.433333333,0],[0.203571429,0,0,0.733333333,0]
            ),
        )


    def test_find_screen_name(self):
        name = ['original_author','DzCritical','toopsat','NassimaLilEmy','d_dhayae','Mohamme65404115']
        self.assertEqual(self.df.find_screen_name(), name)

    def test_find_followers_count(self):
        f_count = [318,764,64,60,39]
        self.assertEqual(self.df.find_followers_count(), f_count)

    def test_find_friends_count(self):
        friends_count = [373,144,47,463,206]
        self.assertEqual(self.df.find_friends_count(), friends_count)

    def test_find_is_sensitive(self):
        self.assertEqual(self.df.is_sensitive(), [None, False,False,False,False])


    # def test_find_hashtags(self):
    #     self.assertEqual(self.df.find_hashtags(), )

    # def test_find_mentions(self):
    #     self.assertEqual(self.df.find_mentions(), )



if __name__ == "__main__":
    unittest.main()

