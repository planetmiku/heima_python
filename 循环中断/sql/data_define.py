class Record():

    def __init__(self,order_date,order_id,money,province):
        self.order_date = order_date
        self.order_id = order_id
        self.money = money
        self.province = province
    def __str__(self):
        return f'{self.order_date},{self.order_id},{self.money},{self.province}'