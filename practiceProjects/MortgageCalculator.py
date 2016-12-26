principal = 500000
payment = 2684.11
rate = 0.05
total_paid  = 0

extra_payment = 1000
extra_payment_start_month = 1
extra_payment_end_month = 60
month = 0



out = open('schedule.txt', 'w')
print('{:>10s} {:>10s} {:>10s}'.format('Month', 'Interest', 'Principal'), file=out)

while principal > 0:
    month += 1
    interest = principal * (rate/12)
    if month <= 60:
        principal = principal + interest - (payment + extra_payment)
    else:
        principal = principal + interest - payment
    total_paid += payment
    print('{:>10d} {:>10.2f} {:>10.2f}'.format(month,interest,principal), file=out)

out.close()


print('Total paid:', total_paid)