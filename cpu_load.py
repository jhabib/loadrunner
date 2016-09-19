import numpy as np
import xgboost as xgb
import tarfile
import pandas as pd
from sklearn.grid_search import GridSearchCV
from optparse import OptionParser


def eat_cpu(data_path):
    tar = tarfile.open(data_path, "r:gz")
    for name in tar.getnames():
        if name == "pizza_request_dataset/pizza_request_dataset.json":
            member = tar.getmember(name)
            f = tar.extractfile(member)
            if f is not None:
                json_data = f.read()

    pizza_df = pd.read_json(json_data)
    pizza_df = np.asarray(pizza_df)
    X, y = pizza_df[:, [2, 3, 4, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 25, 26, 27, 28]], pizza_df[:, 23]
    y = np.asarray(y, dtype=int)

    while True:
        print 'running grid search...'
        params_ = {
            'n_estimators': [1000, 2500, 5000],
            'learning_rate': [0.05, 0.07, 0.10],
            'max_depth': np.arange(5, 35, 10),
        }
        gbm = xgb.XGBClassifier(objective='binary:logistic', seed=0)
        gsc = GridSearchCV(gbm, params_, cv=10, verbose=1, scoring='roc_auc', n_jobs=-1)
        gsc.fit(X, y)


if __name__ == '__main__':
    p = OptionParser(usage="usage: %prog [options] input", version="%prog 1.0")
    p.add_option('-i', '--input',
                 dest='input_file_path',
                 default='pizza.tar.gz')

    opts, rem = p.parse_args()

    eat_cpu(opts.input_file_path)

