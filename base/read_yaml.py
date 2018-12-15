import os

import yaml


class ReadYaml():
    def __init__(self,filename):
        self.filename = os.getcwd()+os.sep+"data"+os.sep+filename
        # self.filename = filename
        # path = os.path.dirname(__file__)
        # self.filename = path+os.sep+filename

    def read_yaml(self):
        with open(self.filename,"r",encoding="utf-8") as f:
            return yaml.load(f)
            # print(yaml.load(f))


if __name__ == '__main__':
    ReadYaml("../data/data_login_01.yaml").read_yaml()
