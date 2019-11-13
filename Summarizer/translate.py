def run_quickstart():

    # [START translate_quickstart]
    # Imports the Google Cloud client library
    from google.cloud import translate_v2 as translate

    # Instantiates a client
    translate_client = translate.Client()

    # The text to translate
    text = "Summary"

    # The target language
    target = 'es'

    # Translates some text into spanish
    translation = translate_client.translate(
        text,
        target_language=target)

    print(u'Text: {}'.format(text))
    print(u'Translation: {}'.format(translation['translatedText']))
    # [END translate_quickstart]


if __name__ == '__main__':
    run_quickstart()