class Product:
    id: int
    title: str
    price: float
    count: int
    category: int

    def __init__(self, *args, **kwargs):
        mainn = 'id title price count category'
        for i in range(len(args)):
            exec(f'self.{mainn[i]} = {args[i]}')
        for k, v in kwargs:
            exec(f'self{k} = {v}')

    def __bool__(self):
        """
        Проверяет есть ли товар в наличии
        """
        return True if self.count > 0 else False


    def __len__(self):
        return self.count
