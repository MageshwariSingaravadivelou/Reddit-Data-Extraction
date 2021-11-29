import pandas as pd
import datetime as dt

start_epoch=int(dt.datetime(2021, 5, 1).timestamp())
end_epoch=int(dt.datetime(2021, 10, 31).timestamp())

from psaw import PushshiftAPI

# Initialize PushShift
api = PushshiftAPI()

api_request_generator = api.search_submissions(subreddit='brave_browser', after = start_epoch, before=end_epoch, limit=10000)

submissions = list()
for element in api_request_generator:
    submissions.append(element.d_)
print(len(submissions))

df = pd.DataFrame(submissions)
df.to_csv('rbrave_browser.csv', header=True, index=False, columns=[
    'id', 'author', 'author_fullname', 'subreddit', 'subreddit_id', 'created_utc', 'domain','url', 'title',
    'score', 'selftext', 'num_comments', 'num_crossposts', 'full_link'
])
