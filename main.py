#!/bin/python3

import requests
import xml.etree.ElementTree as ET
import os.path

MFP_URL = "http://musicforprogramming.net/rss.php"

DIR_PATH = "/media/Multimedia/Music/MusicForProgramming/"

def get_url(url):

    return requests.get(url).text

def download_url(url):

    return requests.get(url,stream=True)

def load_songs():

    tab_songs = []

    tab_song = {
        "title" : "",
        "url"   : ""
    }

    request_xml = ET.fromstring(get_url(MFP_URL))

    for i in request_xml:

        for j in i:

            if j.tag == "item":

                for k in j :

                    # BUG HERE
                    if k.tag == "comments":

                        tab_song['url'] = k.text

                    elif k.tag == "title":

                        tab_song['title'] = k.text

                        tab_songs.append(tab_song)
    return tab_songs



def download_songs():

    tab_songs = load_songs()

    for song in tab_songs:

        ## Download the song and store it into the variable
        song_music = download_url(song['url'])

        print("TEST")

        print(song['title'])

        if not os.path.isfile(DIR_PATH + song['title']):

            print("TEST2")
            #
            # with open(DIR_PATH + "{}".format(song['title']),"wb") as file :
            #
            #     for chunk in song_music.iter_content(chunk_size = 1024):
            #
            #         file.write(chunk)


def __main__():

    download_songs()


if __name__ :

    __main__()
