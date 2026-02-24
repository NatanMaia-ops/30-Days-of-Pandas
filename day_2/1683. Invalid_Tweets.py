import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    condition = tweets['content'].apply(lambda content: len(content) > 15)
    return pd.DataFrame(tweets.loc[condition, ['tweet_id']])

    