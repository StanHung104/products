products = []
total = 0
total = float(total)
while True:
    name = input('請輸入商品名稱：')
    if name == 'q': #quit
        break
    price = input('請輸入價格： ')
    products.append([name, price])
print(products)
for p in products:
    p[1] = float(p[1])
    print('商品', p[0], '價格為', p[1])
    total += p[1]
print('商品總價為： ',total )