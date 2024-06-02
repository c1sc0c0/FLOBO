#!/usr/bin/python

#from pytube import YouTube
#
#def download_captions(url, language='en', output_path='.'):
#    yt = YouTube(url)
#    yt.bypass_age_gate()
#    # Check if the video has captions in the specified language
#    print(yt.captions)
#    if language in yt.captions:
#        caption = yt.captions[language]
#        caption_text = caption.generate_srt_captions()
#
#        # Save the captions to a file
#        output_file = f"{output_path}/{yt.title}.srt"
#        with open(output_file, 'w', encoding='utf-8') as file:
#            file.write(caption_text)
#        
#        print(f"Captions saved to: {output_file}")
#    else:
#        print(f"No captions found for language: {language}")
#
## Example usage
#url = 'https://www.youtube.com/watch?v=7yOtsZNU4Us'
#download_captions(url, language='en', output_path='./data/youtube')


from pytube import YouTube
from datetime import timedelta
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


def remove_tags(text):
    # Parse the text with BeautifulSoup
    soup = BeautifulSoup(text, "html.parser")
    # Extract the plain text
    return soup.get_text()

def download_captions(ytid, language='en', output_path='.'):
    yt = YouTube("https://www.youtube.com/watch?v=" + ytid)
    yt.bypass_age_gate()

    # Check if the video has captions in the specified language
    if language in yt.captions:
        caption = yt.captions[language]
        xml_captions = caption.xml_captions
        cleaned_captions = remove_tags(xml_captions)
        print(cleaned_captions)
        # Save the captions to a file
        output_file = f"{output_path}/{ytid}.srt"
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(cleaned_captions)
        
        print(f"Captions saved to: {output_file}")
    else:
        print(f"No captions found for language: {language}")

# Example usage
ytid = 'KlYkyAUHrO8'
download_captions(ytid, language='en', output_path='./youtube')