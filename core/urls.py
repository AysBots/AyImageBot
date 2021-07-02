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
    api_request = requests.get(
        r"https://api.unsplash.com/search/photos?query={}&client_id={}".format(query, CLIENT_KEY))
    api_request_data = api_request.json()
    random_page_index = randint(1, api_request_data['total_pages'])
    final_api_request = requests.get(
        r"https://api.unsplash.com/search/photos?page={}&query={}&client_id={}".format(str(random_page_index), query, CLIENT_KEY))
    final_api_request_data = final_api_request.json()
    z = 0
    for i in final_api_request_data['results']:
        z += 1
    random_image_index = randint(0, z-1)
    # Full , Raw, Regular, Small, Thumb
    final_result_url = final_api_request_data['results'][random_image_index]['urls']['regular']
    return final_result_url


def get_final_image(CLIENT_KEY, query, filename):
    url = fetch_unsplash_api(CLIENT_KEY, query)
    urlretrieve(url, filename)
    return None


if __name__ == "__main__":
    # Testing Code
    get_image(get_url_source_unsplash(search="computer"), True)
