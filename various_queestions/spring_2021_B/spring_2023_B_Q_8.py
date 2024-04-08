class Client:
    def __init__(self, address, persons, current, prev):
        self.address = address
        self.persons = persons
        self.current = current
        self.prev = prev

    def update_current(self, new_current):
        self.prev = self.current
        self.current = new_current

    def payment(self, rate1, rate2):
        usage = self.current - self.prev # חישוב צריכה
        roof_low_price = self.persons * 7 # חישוב תקרת הנחה
        if usage <= roof_low_price: # אם התקרה מעל הצריכה - כל הצריכה בתעריף מוזל
            return usage * rate1
        else:
            low_price_payment = roof_low_price * rate1 # חישוב תעריף מוזל
            high_price_payment = (usage - roof_low_price) * rate2 #חישוב תעריף יקר
            return low_price_payment + high_price_payment # מחזיר את כלל התשלום
        
c1 = Client("acd", 4, 35, 0)

def proposal(arr, num, rate1, rate2):
    sum = 0
    counter = 0
    for client in arr:
        if client.persons == num:
            counter += 1
            sum += client.payment(rate1, rate2)
    avg = sum / counter
    for client in arr:
        if client.payment(rate1, rate2) > avg:
            print(client.address)