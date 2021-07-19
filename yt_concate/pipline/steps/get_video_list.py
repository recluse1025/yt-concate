# 2.建立youtube影片清單
import urllib.request
import json

from yt_concate.pipline.steps.step import Step
from yt_concate.settings import API_KEY


class GetVideoList(Step):
    def process(self, data, inputs, utils):
        # self.get_all_video_in_channel(inputs['channel_id'])
        channel_id = inputs['channel_id']

        if utils.caption_file_exits(channel_id):
            print('Found existing video list file for channel id', channel_id)
            return self.read_file(utils.get_video_list_filepath(channel_id))
        # 取得youtube頻道影片網址清單
        # def get_all_video_in_channel(channel_id):
        # GCP上取得 youtube APIKEY
        # api_key = API_KEY

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + F'key={API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25'

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

        print(video_links)
        self.write_to_file(video_links, utils.get_video_list_filepath(channel_id))
        return video_links

    def write_to_file(self, video_links, filepath):
        with open(filepath, 'w') as f:
            for url in video_links:
                f.write(url + '\n')

    def read_file(self, filepath):
        video_links = []
        with open(filepath, 'r') as f:
            for url in f:
                video_links.append(url.strip())
        return video_links


