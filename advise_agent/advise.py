import os

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from sklearn.preprocessing import LabelEncoder, MinMaxScaler

from cw6.settings import BASE_DIR
TRAIN_FILE = os.path.join(BASE_DIR, 'advise_agent', "cw-train-2.csv")


class Advise:
    def __init__(self):
        self.X = None
        self.Y = None
        self.le = LabelEncoder()
        self.scaler = MinMaxScaler()
        self.model = RandomForestClassifier()

    def __convert(self, file_train):
        data = pd.read_csv(file_train)

        data.drop(columns=['he_short'], inplace=True)   # for plots

        mapping = {"Брестская": 1, "Бресткая": 1, "Витебская": 2, "Гомельская": 3, "Гродненская": 4,
                   "Минск": 5, "Минская": 6, "Могилевская": 7, "Могилёвская": 7}
        data['region'].replace(mapping, inplace=True)

        data.fillna(0, inplace=True)

        data = data.sample(frac=1)

        data['he'] = self.le.fit_transform(data['he'])

        self.X = data.drop(['he'], axis=1)
        self.Y = data['he']

        self.X = self.features_engineering(self.X)

    def features_engineering(self, x):
        mapping = {"Брестская": 1, "Бресткая": 1, "Брестcкая": 1, "Витебская": 2, "Гомельская": 3, "Гродненская": 4,
                    "Минск": 5, "Минская": 6, "Могилевская": 7, "Могилёвская": 7, "Не важно": 0}
        x['region'].replace(mapping, inplace=True)
        x.fillna(0, inplace=True)

        x['journ-int_com'] = x['journ'] + x['int_com']
        x['lingo-teach-psy'] = x['lingo'] + x['teach'] + x['psy']

        x['it-math'] = x['it'] + x['math']
        x['it-design'] = x['it'] + x['design']
        x['math-physics'] = x['math'] + x['physics']
        x['phys_cult-tourism'] = x['phys_cult'] + x['turism']
        x['ss-lingo-hist-journ'] = x['ss'] + x['lingo'] + x['hist'] + x['journ']
        x['phys_cult-bio'] = x['phys_cult'] + x['bio']
        x['chem-forest'] = x['chem'] + x['forest']
        x['journ-ss-lingo'] = x['journ'] + x['ss'] + x['lingo']

        x.drop(columns=['journ', 'int_com',
                        'lingo', 'teach', 'psy',
                        'it', 'math',
                        'design',
                        'physics',
                        'phys_cult', 'turism',
                        'ss',
                        'hist',
                        'bio',
                        'chem', 'forest'],
               inplace=True)

        x = np.array(x)

        return x

    def teach(self):
        self.__convert(TRAIN_FILE)
        self.model.fit(self.X, self.Y)

    def advise(self, user_input):
        self.teach()

        user_input = pd.DataFrame(user_input)
        user_input = np.array(self.features_engineering(user_input))
        prediction = self.model.predict(user_input)
        prediction = self.le.inverse_transform(prediction)

        accuracy = accuracy_score(self.Y, self.model.predict(self.X))

        return round(100 * accuracy, ndigits=2), prediction[0]


