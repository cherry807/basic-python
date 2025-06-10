def convert_usd_to_inr(usd, rate=83.1):
    return usd * rate

usd = float(input("Enter amount in USD: "))
print("INR:", convert_usd_to_inr(usd))
