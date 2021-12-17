import json
import os

response_data = {}


def get_response_data():
    global response_data

    path_to_lang_files = "resource/language"

    for Lang_file in os.listdir(path_to_lang_files):
        full_filename = "%s/%s" % (path_to_lang_files, Lang_file)

        with open(full_filename, 'rb') as file:
            base_name = os.path.basename(file.name)

            file_name, extension = os.path.splitext(base_name)

            data = json.load(file)

            result = {file_name + "_" + str(key): val for key, val in data.items()}

            response_data = response_data | result


def response_process(lang, error):
    response = response_data

    if lang is None:
        lang = "en"

    elif lang == "ar":
        lang = "ar"

    else:
        lang = "en"

    if isinstance(error, dict):
        prefix_add = {key: lang + "_" + val for key, val in error.items()}

        result = {key: response[val] for key, val in prefix_add.items()}

        return result

    else:
        result = response[lang + "_" + error]

        return result
