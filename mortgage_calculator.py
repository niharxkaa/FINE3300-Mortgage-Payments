# FINE 3300 - Assignment 1
# Mortgage Payment Calculator

def mortgage_payments(principal, rate, amortization):
    """
    Calculates mortgage payments for different payment frequencies.

    Parameters:
        principal (float): Loan amount.
        rate (float): Quoted annual interest rate (as percentage, e.g., 5.5 for 5.5%).
        amortization (int): Amortization period in years.

    Returns:
        tuple: Monthly, Semi-Monthly, Bi-Weekly, Weekly, Rapid Bi-Weekly, and Rapid Weekly payments.
    """
    # Convert rate from percentage to decimal
    rate = rate / 100

    # Number of payments for different schedules
    n_monthly = amortization * 12
    n_semi_monthly = amortization * 24
    n_bi_weekly = amortization * 26
    n_weekly = amortization * 52

    # Compute periodic interest rates
    r_monthly = (1 + rate / 2) ** (2 / 12) - 1
    r_semi_monthly = (1 + rate / 2) ** (2 / 24) - 1
    r_bi_weekly = (1 + rate / 2) ** (2 / 26) - 1
    r_weekly = (1 + rate / 2) ** (2 / 52) - 1

    # Present Value of Annuity Factor (PVA)
    def pva(r, n):
        return (1 - (1 + r) ** -n) / r

    # Calculate mortgage payments for each frequency
    monthly = principal / pva(r_monthly, n_monthly)
    semi_monthly = principal / pva(r_semi_monthly, n_semi_monthly)
    bi_weekly = principal / pva(r_bi_weekly, n_bi_weekly)
    weekly = principal / pva(r_weekly, n_weekly)
    
    # Accelerated payment schedules
    rapid_bi_weekly = monthly / 2
    rapid_weekly = monthly / 4

    return round(monthly, 2), round(semi_monthly, 2), round(bi_weekly, 2), round(weekly, 2), round(rapid_bi_weekly, 2), round(rapid_weekly, 2)

# Prompt user for input
principal = float(input("Enter the loan amount (principal): "))
rate = float(input("Enter the quoted annual interest rate (as %): "))
amortization = int(input("Enter the amortization period (in years): "))

# Compute payments using the function
payments = mortgage_payments(principal, rate, amortization)

# Display formatted results
print(f"\nMonthly Payment: ${payments[0]:,.2f}")
print(f"Semi-monthly Payment: ${payments[1]:,.2f}")
print(f"Bi-weekly Payment: ${payments[2]:,.2f}")
print(f"Weekly Payment: ${payments[3]:,.2f}")
print(f"Rapid Bi-weekly Payment: ${payments[4]:,.2f}")
print(f"Rapid Weekly Payment: ${payments[5]:,.2f}")