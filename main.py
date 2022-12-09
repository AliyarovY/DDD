import json
import os


class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """
    __data_file = None

    def __init__(self, df):
        self.__data_file = df
        self.__connect()

    def __connect(self):
        with open(f'{self.__data_file}', 'w+') as file:
            file.close()


    def insert(self, data):

        with open (self.__data_file, 'a') as datafile:
            datafile.write(data)


    def select(self, query):
        key = None
        value = None
        for k, v in query:
            key = k
            value = v

        with open(df) as ff:
            file = json.load(self.df)
            return [x for x in file if key in x and x[key] == value]



    def delete(self, query):
        """
        Удаление записей из файла, которые соответствуют запрос,
        как в методе select
        """

        with open(self.__data_file, 'r') as json_file:
            data = json.load(json_file)

            for k in data[query.keys()]:
                if data[k] == query.values():
                    del data[k]

        os.remove(self.__data_file)

        with open(self.__data_file, 'w') as fw:
            json.dump(data, fw)



if __name__ == '__main__':
    df = Connector('df.json')

    data_for_file = {'id': 1, 'title': 'tet'}

    df.insert(data_for_file)
    data_from_file = df.select(dict())
    assert data_from_file == [data_for_file]

    df.delete(dict())
    data_from_file = df.select(dict())
    assert data_from_file == []