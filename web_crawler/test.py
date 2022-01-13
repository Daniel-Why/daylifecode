from requests import Session


class ReadDocument(object):
    def __init__(self):
        self._text_url = 'https://image.pdflibr.com/crawler/blog/tencent_cloud_ip_range.txt'

    def read_text_document(self):
        init_session = Session()
        response = init_session.get(url=self._text_url)
        response.encoding = 'utf-8'
        print(response.text)


if __name__ == '__main__':
    ReadDocument().read_text_document()