#Payment options:
    #1. Monthly payments:                    12 payments/year
    #2. Semi-monthly payments:               24 payments/year
    #3. Bi-weekly payments:                  26 payments/year
    #4. Weekly payments:                     52 payments/year
    #5. Accelerated Bi-weekly payments:      26 payments/year. the payment is equal to half the monthly amount
    #6. Accelerated Weekly payments:         52 payments/year. the payment is equal to one-quarter of the monthly amount


#Design a class, "MortgagePayment", to compute all the payment options
class MortgagePayment:
    # initialization: interest rate and amortization period
    def __init__(self, interest_rate, amortization_years):
        self.rate = interest_rate/100
        self.years = amortization_years

    # implement a method/function, "Present Value of Annuity factor"
    def pva_factor(self, r, n):
        if r == 0:
            return n
        return (1 - (1 + r) ** (-n)) / r

    #implement a method/function, "payment
    def payments(self, principal):
        # Convert semi-annual rate to effective annual rate since fixed rate mortgages are quoted as semiannually compounded rates
        # EAR = (1 + APR / k) ** k -1
        EAR = (1 + self.rate / 2) ** 2 - 1

        #equivalent n-period effective rate = (1 +EAR) ** (1/n) - 1
        # MONTHLY
        monthly_rate = (1 + EAR) ** (1/12) - 1
        monthly_periods = self.years * 12
        monthly_payment = principal / self.pva_factor(monthly_rate, monthly_periods)

        # SEMI-MONTHLY
        semi_monthly_rate = (1 + EAR) ** (1/24) - 1
        semi_monthly_periods = self.years * 24
        semi_monthly_payment = principal / self.pva_factor(semi_monthly_rate, semi_monthly_periods)

        # BI-WEEKLY
        bi_weekly_rate = (1 + EAR) ** (1/26) - 1
        bi_weekly_periods = self.years * 26
        bi_weekly_payment = principal / self.pva_factor(bi_weekly_rate, bi_weekly_periods)

        # WEEKLY
        weekly_rate = (1 + EAR) ** (1/52) - 1
        weekly_periods = self.years * 52
        weekly_payment = principal / self.pva_factor(weekly_rate, weekly_periods)

        # ACCELERATED PAYMENTS (based on monthly payment)
        rapid_bi_weekly_payment= monthly_payment / 2
        rapid_weekly_payment = monthly_payment / 4

        return(
            round(monthly_payment, 2),
            round(semi_monthly_payment, 2),
            round(bi_weekly_payment, 2),
            round(weekly_payment, 2),
            round(rapid_bi_weekly_payment, 2),
            round(rapid_weekly_payment, 2)
        )

# Collect relevant data
print("=== Mortgage Payments Calculator ===")
principal = float(input("Enter the principal amount (i.e., 100000): $"))
rate = float(input("Enter the interest rate (i.e., 5.5): "))
years = int(input("Enter the amortization period in years (i.e., 25): "))

#Calculate and display results
mortgage = MortgagePayment(rate, years)
results = mortgage.payments(principal)

print("\n--- Payment Results ---")
print(f"Monthly: ${results[0]:,.2f}")
print(f"Semi-monthly: ${results[1]:,.2f}")
print(f"Bi-weekly: ${results[2]:,.2f}")
print(f"Weekly: ${results[3]:,.2f}")
print(f"Rapid Bi-weekly: ${results[4]:,.2f}")
print(f"Rapid Weekly: ${results[5]:,.2f}")







