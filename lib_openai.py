# Función para generar el archivo jsonl de requests para batch

import pandas as pd
import json
import configparser
import numpy as np
import openai
from pathlib import Path
import re

# Leer config.ini
config = configparser.ConfigParser()
config_path = Path(__file__).parent / "config.ini"
config.read(config_path)


OPENAI_API_KEY = config["OPENAI"]["API_KEY"]
openai.api_key = OPENAI_API_KEY
#MODEL='gpt-3.5-turbo'
MODEL='gpt-4.1-mini'

def get_completion_from_messages(messages, 
                                 model=MODEL,
                                 temperature=0,
                                 max_tokens=500):
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content.strip()