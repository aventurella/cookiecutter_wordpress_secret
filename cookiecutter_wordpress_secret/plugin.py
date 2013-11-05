import requests
from cookiecutter.plugins import JinjaSimpleTag


class WordpressSecret(JinjaSimpleTag):
    tags = set(['wordpress_secret'])

    def tag_action(self, caller):
        r = requests\
            .get('https://api.wordpress.org/secret-key/1.1/salt/')

        return r.text
