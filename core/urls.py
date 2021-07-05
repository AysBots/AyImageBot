import requests
from random import randint
from urllib.request import urlretrieve


def get_image(url, print_url=False):
    '''
    Convert URL to original image link
    '''
    response = requests.get(url)
    if print_url:
        print(response.url)
    return response.url


def get_url_source_unsplash(width='1600', height='900', search='random'):
    if search == "" or search == " ":
        search = 'random'
    raw_unsplash_url = f"https://source.unsplash.com/{width}x{height}/?{search}"
    return raw_unsplash_url


def fetch_unsplash_api(CLIENT_KEY, query):
    if query == "" or query == " ":
        query = 'random'
    api_request_data = requests.get(
        r"https://api.unsplash.com/search/photos?query={}&client_id={}".format(query, CLIENT_KEY)).json()  # Request 1
    random_page_index = randint(1, api_request_data['total_pages'])
    final_api_request = requests.get(
        r"https://api.unsplash.com/search/photos?page={}&query={}&client_id={}".format(str(random_page_index), query, CLIENT_KEY))  # Request 2
    final_api_request_data = final_api_request.json()
    z = 0
    for i in final_api_request_data['results']:
        z += 1
    random_image_index = randint(0, z-1)
    api_download = final_api_request_data['results'][random_image_index]['links']['download_location']
    download_url = api_download + \
        r"?client_id={}&utm_source=telegram-image-service&utm_medium=referral".format(
            CLIENT_KEY)
    # Request 3: Triggering Download request as given in Unsplash API Guidelines https://help.unsplash.com/api-guidelines/guideline-triggering-a-download
    download_request = requests.get(download_url)
    # Full , Raw, Regular, Small, Thumb
    # Requesting Regular Quality Image to increase speed and efficiency
    final_result_url = final_api_request_data['results'][random_image_index]['urls']['regular']
    # Building Caption
    caption = 'Photo by ' + r'<a href="https://unsplash.com/@{}?utm_source=telegram-image-service&utm_medium=referral">{}</a>'.format(
        final_api_request_data['results'][random_image_index]['user']['username'], final_api_request_data['results'][random_image_index]['user']['name']) + ' on ' + r'<a href="https://unsplash.com/?utm_source=telegram-image-service&utm_medium=referral">Unsplash</a>'
    return final_result_url, caption


def get_final_image(CLIENT_KEY, query, filename):
    url, caption = fetch_unsplash_api(CLIENT_KEY, query)
    urlretrieve(url, filename)
    return caption


if __name__ == "__main__":
    # Testing Code
    get_image(get_url_source_unsplash(search="computer"), True)
