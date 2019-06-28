__author__ = 'gt88e'

from models.alert import Alert

alerts = Alert.all()

for alert in alerts:
    alert.load_item_price()
    print(f'Alert for {alert.name} price updated to {alert.item.price}" limit is {alert.price_limit}')
    alert.notify_if_price_reached()

if not alerts:
    print("No alerts have been created. Add an item and an alert to begin!")
