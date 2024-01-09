swimming = int(input("Enter your time for swimming (in minute): "))
cycling = int(input("Enter your time cycling (in minute): "))
running = int(input("Enter your time running (in minute): "))

total_time = swimming + cycling + running
print("total time is: ",total_time)

if total_time > 0 and total_time <= 100:
 print("Within the qualifying time. Provincial Colours")
elif total_time >= 101 and total_time <= 105:
 print("Within 5 minutes of the qualifying time. Provincial Half Colours")
elif total_time >= 106 and total_time <= 110:
 print("Within 10 minutes of the qualifying time. Provincial Scroll")
else:
 print("More than 10 minutes off from the qualifying time. No award")




