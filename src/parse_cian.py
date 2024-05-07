import cianparser
import pandas as pd
import datetime
from dotenv import dotenv_values

config = dotenv_values(".env")
moscow_parser = cianparser.CianParser(location="Москва")


def main():
    n_rooms = 3
    data = moscow_parser.get_flats(
        deal_type="sale",
        rooms=(n_rooms,),
        with_saving_csv=False,
        additional_settings={
            "start_page": 1,
            "end_page": 50,
            "object_type": "secondary"
        })

    df = pd.DataFrame(data)
    t = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    df.to_csv(f'C:/Users/7ivan/PycharmProjects/pabd24/data/raw/{n_rooms}_{t}.csv')



if __name__ == '__main__':
    main()

