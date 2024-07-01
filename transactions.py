transactions = [10.1, 22.0, 32.2, 17.8, 55.0]
transactions.sort

minimum = transactions[0]
maximum = transactions[4]
total = 0

for transaction in transactions:
    if transaction <= 11:
        print(f"The smallest transaction was {minimum}")
    elif transaction >= 50:
        print(f"The largest transaction was {maximum}")

i = 0
while i < len(transactions):
    total += transactions[i] 
    i+= 1
print(f"The sum of all the transaction is {total:.2f}")