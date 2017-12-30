#!/bin/python3
# Todo :
# - Be able to add arguments to set the recurence of the download
# - Find a way to sync it to a device e.g. Phone


import requests
import xml.etree.ElementTree as ET
import os.path
import argparse

URL = ""

XML = ""

DIR_PATH = ""

tab_song_url = []

tab_song_title = []


def get_argv():

    # https://docs.python.org/3.3/library/argparse.html
    parser = argparse.ArgumentParser(description="""Specify the URL and the path
                                                directory""")

    parser.add_argument('--dir', nargs=1, help="""the path to the directory 
        where you saved the rss file you want to download.""")

    parser.add_argument('--url', help="the URL that you want to download.")

    return parser.parse_args()


def get_url2xml(url):

    return ET.fromstring(requests.get(url).text)


def download_url(url):

    return requests.get(url, stream=True)


# Append the url of the song into the tab_song
# dictionnary
def load_song_url(xml):

    # Add validation for presence of XML variable.

    for i in xml:

        for j in i:

            if j.tag == "item":

                for k in j:

                    if k.tag == "comments":

                        tab_song_url.append(k.text)

# Append the title of the song into the tab_song
# dictionnary


def load_song_name(xml):

    for i in xml:

        for j in i:

            if j.tag == "item":

                for k in j:

                    if k.tag == "title":

                        song_name_file = k.text.replace(" ", "_")

                        song_name_file = song_name_file.replace(":", "")

                        song_name_file += ".mp3"

                        tab_song_title.append(song_name_file)


# If the name of the song is not in the directory download it.
def download_songs(DIR_PATH):

    for i in range(0, len(tab_song_url)):

        # Download the song and store it into the variable
        song_file = download_url(tab_song_url[i])

        if not os.path.isfile(DIR_PATH + tab_song_title[i]):

            with open(DIR_PATH + "{}".format(tab_song_title[i]), "wb") as file:

                for chunk in song_file.iter_content(chunk_size=1024):

                    file.write(chunk)


def __main__():

    args = get_argv()

    DIR_PATH = args.dir[0]

    URL = args.url

    XML = get_url2xml(URL)

    load_song_url(XML)

    load_song_name(XML)

    download_songs(DIR_PATH)


if __name__:

    __main__()
