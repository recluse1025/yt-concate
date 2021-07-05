import urllib.request
import json
from yt_concate.settings import API_KEY
# print(API_KEY)
# youtube頻道ID
CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


# 取得youtube頻道影片網址清單
def get_all_video_in_channel(channel_id):
    # GCP上取得 youtube APIKEY
    api_key = API_KEY

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url + F'key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25'

    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + F'&pageToken={next_page_token}'
        except KeyError:
            break
    return video_links


video_list = get_all_video_in_channel(CHANNEL_ID)
print(video_list)
print(len(video_list))
