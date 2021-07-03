import os, sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from api_loader import UNSPLASH_CLIENT_KEY


DATAFILE = 'auth_data.json'
SEARCHDATAFILE = 'search_data.txt'
