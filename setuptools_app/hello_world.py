import os
from jinja2 import Template


class HelloWorld(object):
    def hello(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        contents_file = open(os.path.join(current_dir, 'contents/hello'))

        template = Template(contents_file.read())
        print template.render()
