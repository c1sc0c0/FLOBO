# Yoga Flow Bot (flobo - The Yoga Robo)

## Overview

Flobo is a Yoga Bot that can suggest Yoga flows based on user input. It's a personal research project to explore the intersection between classical Symbolic AI and modern Neural LLM-based approaches.

## Installation

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    
## Python Dependencies

* ollama
* clips
* chromadb
* jupyter
* scrapy
* pytube
* numpy
* nltk

# Homebrew Dependencies

* imagemagick
* libheif

## Getting Started

The best way to explore this is to run the Jupyter notebooks. demo.ipynb contains a chat demo and playground.ipynb is where development happens.

    jupyter lab
    
# Development Notes

Don't forget to clean the output from the .ipynb files before git commit! (clean.sh)

    jupyter nbconvert --clear-output --inplace *.ipynb

Periodically push to destination git repository.

    git push destination main




