import requests


def get_image(url, print_url=False):
    '''
    Convert URL to original image link
    '''
    response = requests.get(url)
    if print_url:
        print(response.url)
    return response.url


def get_url(width='1600', height='900', search='random'):
    if search == "" or search == " ":
        search = 'random'
    raw_url = f"https://source.unsplash.com/{width}x{height}/?{search}"
    return raw_url


if __name__ == "__main__":
    # Testing Code
    get_image(get_url(search="computer"), True)
