import boto3
import os
import ruamel.yaml

from ruamel.yaml.emitter import Emitter
# Key name can be very long for suggestions
Emitter.MAX_SIMPLE_KEY_LENGTH = 1024

translate = boto3.client('translate')
polly = boto3.client('polly')


def translate_text(text, source_lang, target_lang):
    response = translate.translate_text(
        Text=text,
        SourceLanguageCode=source_lang,
        TargetLanguageCode=target_lang
    )
    translated = response['TranslatedText']
    print(f'Translating "{text}" to "{translated}"')
    return translated


def synthesize_speech(text, voice_id):
    response = polly.synthesize_speech(
        OutputFormat='mp3',
        Text=text,
        VoiceId=voice_id
    )
    audio = response['AudioStream'].read()
    return audio


def save_audio_file(audio, directory, file_name):
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'wb') as file:
        file.write(audio)
    print(f"Saving to {file_path}")


def process_yaml_file(file_path, target_lang, output_directory):

    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True

    with open(file_path, 'r') as file:
        data = yaml.load(file)

    for key, _ in data.items():

        # Limit filename to 50 characters
        filename = f'{key.replace(" ", "")[:50]}.mp3'
        data[key] = filename

        if os.path.exists(os.path.join(output_directory, filename)):
            print(f"Audio file {filename} already exists, skipping")
            continue

        translated_key = translate_text(key, 'en', target_lang)
        audio = synthesize_speech(translated_key, 'Celine')  # French voice ID
        save_audio_file(audio, output_directory, filename)

    with open(file_path, 'w') as file:
        yaml.dump(data, file)


input_file = './French/mapping.yaml'
target_language = 'fr'
output_directory = './French/Audio'

if __name__ == '__main__':
    process_yaml_file(input_file, target_language, output_directory)
