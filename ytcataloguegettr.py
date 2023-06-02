import requests

def get_channel_videos(channel_id, api_key):
    try:
        url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            'channelId': channel_id,
            'key': api_key,
            'part': 'snippet',
            'maxResults': 50,
            'order': 'date',
            'type': 'video'
        }
        videos = []
        next_page_token = None

        while True:
            if next_page_token:
                params['pageToken'] = next_page_token

            response = requests.get(url, params=params)
            data = response.json()
            videos.extend(data['items'])
            
            next_page_token = data.get('nextPageToken')

            if not next_page_token:
                break

        for video in videos:
            video_title = video['snippet']['title']
            video_id = video['id']['videoId']
            video_link = f"https://www.youtube.com/watch?v={video_id}"
            print(f"{video_link}")

        input("Holding...")
    except requests.exceptions.RequestException as e:
        print('Error:', e)

# Replace 'YOUR_CHANNEL_ID' and 'YOUR_API_KEY' with your actual channel ID and API key
channel_id = input("Enter Channel ID: ")
api_key = 'AIzaSyCn5Yjez481fDtGO3XpbcooG-h1Pztf7A4'

get_channel_videos(channel_id, api_key)
