# import argparse
# import logging
# import os
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from joblib import dump
#
# logger = logging.getLogger(__name__)
# logging.basicConfig(
#     filename='log/train_model.log',
#     encoding='utf-8',
#     level=logging.DEBUG,
#     format='%(asctime)s %(message)s')
#
# TRAIN_DATA = 'data/proc/train.csv'
# MODEL_SAVE_DIR = 'models'
# MODEL_SAVE_PATH = os.path.join(MODEL_SAVE_DIR, 'linear_regression_v01.joblib')
# GITIGNORE_FILE = '.gitignore'
#
#
# def main(args):
#     # Создание папки для сохранения модели, если она не существует
#     if not os.path.exists(MODEL_SAVE_DIR):
#         os.makedirs(MODEL_SAVE_DIR)
#
#     df_train = pd.read_csv(TRAIN_DATA)
#     x_train = df_train[['total_meters']]
#     y_train = df_train['price']
#
#     linear_model = LinearRegression()
#     linear_model.fit(x_train, y_train)
#     dump(linear_model, args.model)
#     logger.info(f'Saved to {args.model}')
#
#     # Создание файла .gitignore
#     with open(GITIGNORE_FILE, 'w') as f:
#         f.write('.joblib\n')
#
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-m', '--model',
#                         help='Model save path',
#                         default=MODEL_SAVE_PATH)
#     args = parser.parse_args()
#     main(args)
import argparse
import logging
import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from joblib import dump

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='log/train_model.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s')

TRAIN_DATA = 'data/proc/train.csv'
MODEL_SAVE_DIR = 'models'
MODEL_SAVE_PATH = os.path.join(MODEL_SAVE_DIR, 'linear_regression_v02.joblib')
GITIGNORE_FILE = '.gitignore'


def main(args):
    # Создание папки для сохранения модели, если она не существует
    if not os.path.exists(MODEL_SAVE_DIR):
        os.makedirs(MODEL_SAVE_DIR)

    df_train = pd.read_csv(TRAIN_DATA)

    # Добавление новых фичей
    features = ['total_meters', 'floor', 'floors_count', 'rooms_count', 'price_per_month']
    df_train.fillna(0, inplace=True)  # Заполнение пропущенных значений нулями или другими значениями

    x_train = df_train[features]
    y_train = df_train['price']

    linear_model = LinearRegression()
    linear_model.fit(x_train, y_train)
    dump(linear_model, args.model)
    logger.info(f'Saved to {args.model}')

    # Создание файла .gitignore
    with open(GITIGNORE_FILE, 'w') as f:
        f.write('.joblib\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--model',
                        help='Model save path',
                        default=MODEL_SAVE_PATH)
    args = parser.parse_args()
    main(args)
