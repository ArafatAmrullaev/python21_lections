import json
def create_product(id_:int, price:int, name:str):
    product = {'id':id_, 'price': price, 'name': name}
    with open('db.json', 'r+') as file:
        json_data = json.load(file)
        json.dump(product, file)
create_product(3, 28, 'chips')
create_product(1, 45, 'snickers')