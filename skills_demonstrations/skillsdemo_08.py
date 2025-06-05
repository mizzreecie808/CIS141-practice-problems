# Module 08 - Skills Demonstration
# buy - Cabbage Seeds, Turnip Seeds, Strawberry Seeds

buy_cabbage = "Cabbage Seeds"
buy_turnip = "Turnip Seeds"
buy_strawberry = "Strawberry Seeds"

import shop
# view shop's inventory
shop.view_inventory()

# buy 2 items
shop.buy_item(buy_cabbage, 2)
shop.buy_item(buy_strawberry, 4)

# restock an item
shop.restock_item(buy_turnip, 100)

# view updated inventory
shop.view_inventory()
