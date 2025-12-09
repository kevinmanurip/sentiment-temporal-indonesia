import snscrape.modules.twitter as sntwitter
import pandas as pd

query = (
    "(agama OR gereja OR sabat OR iman OR ibadah OR doa OR toleransi) "
    "lang:id since:2022-01-01 until:2024-12-31"
)

tweets = []
limit = 10000  # mulai kecil dulu, nanti bisa scaling

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) >= limit:
        break
    tweets.append([
        tweet.date,
        tweet.content,
        tweet.likeCount,
        tweet.retweetCount
    ])

df = pd.DataFrame(
    tweets,
    columns=["date", "text", "likes", "retweets"]
)

df.to_csv("data/raw/tweets_raw.csv", index=False)
print("✅ Data collected:", len(df))
