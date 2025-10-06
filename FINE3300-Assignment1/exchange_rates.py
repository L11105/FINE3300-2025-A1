class ExchangeRates:
    def __init__(self, filename):
        self.filename = filename
        self.rate = self.get_latest_rate()

    def get_latest_rate(self):
        # Read the CSV file and get the last USD/CAD rate
        with open(self.filename, 'r') as file:      #with statement, no need to close file. open file, (file, mode), r - read
            lines = file.readlines()
            last_line = lines[-1]  # Get last row
            values = last_line.split(',')
            usd_cad_index = 25  # USD/CAD is at position 25 in the header
            return float(values[usd_cad_index])

    def convert(self, amount, from_currency, to_currency):
        if from_currency.upper() == 'USD' and to_currency.upper() == 'CAD':
            return amount * self.rate
        elif from_currency.upper() == 'CAD' and to_currency.upper() == 'USD':
            return amount / self.rate
        else:
            return amount


print("=== Currency Exchange Calculator ===")
exchange = ExchangeRates('BankOfCanadaExchangeRates.csv')

print(f"Current USD/CAD rate: {exchange.rate:.4f}")
print()

amount = float(input("Enter amount to convert: "))
from_curr = input("Convert from (USD/CAD): ")
to_curr = input("Convert to (USD/CAD): ")

result = exchange.convert(amount, from_curr, to_curr)

print(f"\n{amount:,.2f} {from_curr.upper()} = {result:,.2f} {to_curr.upper()}")