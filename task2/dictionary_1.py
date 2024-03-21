transactions = [
    ('Karapet', 'Karapetyan', 11000, 'aperitivo'),
    ('Karapet', 'Karapetyan', 13700, 'zangakbookstore'),
    ('Karapet', 'Karapetyan', 7200, 'aperitivo'),
    ('Karapet', 'Karapetyan', 10900, 'zangakbookstore'),
    ('Karapet', 'Karapetyan', 6200, 'sassupermarket'),
    ('Karapet', 'Karapetyan', 5000, 'sassupermarket'),
    ('Karapet', 'Karapetyan', 4500, 'aperitivo'),
    ('Karapet', 'Karapetyan', 2800, 'sassupermarket'),
    ('Karapet', 'Karapetyan', 9430, 'sassupermarket'),
    ('Karapet', 'Karapetyan', 1700, 'aperitivo'),
]


businesses = {}

for transaction in transactions:
    business = transaction[3]  
    amount = transaction[2]  

    if business in businesses:
        businesses[business] += amount
    else:
        businesses[business] = amount


max_spending_business = max(businesses, key=businesses.get)
print("Business with the highest spending:", max_spending_business)

