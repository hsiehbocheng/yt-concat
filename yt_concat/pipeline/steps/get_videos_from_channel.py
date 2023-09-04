import json
import urllib.request

from yt_concat.pipeline.steps.step import step, StepException
from yt_concat.settings import YOUTUBE_API_KEY



class GetVideoList(step):
    def process(self, inputs):
        CHANNEL_ID = inputs['channel_id']
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + f'key={YOUTUBE_API_KEY}&channelId={CHANNEL_ID}&part=snippet,id&order=date&maxResults=25'

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
                url = first_url + f'&pageToken={next_page_token}'
            except KeyError:
                break
        print(video_links)
        return video_links