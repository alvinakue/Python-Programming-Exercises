def calculate_monthly_payment(car_price, down_payment, loan_period_years, interest_rate):
    loan_amount = car_price - down_payment
    loan_period_months = loan_period_years * 12
    total_interest = interest_rate * loan_amount * loan_period_years
    monthly_payment = (loan_amount + total_interest) / loan_period_months
    return monthly_payment

def main():
    car_price = 90000
    minimum_down_payment_percentage = 0.10
    interest_rate = 0.027
    down_payment = float(input("Please enter your down payment: RM "))
    loan_period_years = int(input("Enter your loan period in years (1 to 9 years only): "))
    if down_payment >= car_price * minimum_down_payment_percentage:
        monthly_payment = calculate_monthly_payment(car_price, down_payment, loan_period_years, interest_rate)
        print(f"Your monthly payment is: RM {monthly_payment: .2f}")
    else:
        print("You are not eligible for the bank loan. Please check your down payment and loan period.")

if __name__ == "__main__":
    main()