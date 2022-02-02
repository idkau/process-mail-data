class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

total = 0

f = open("output.txt", "r")
lines = f.readlines()

for line in lines:
    #print(line.strip())
    value = int(line.strip())
    total += value

f.close()
# Get total mail for 30 days
monthly_mail = total * 10
daily_outbound_mail = int(monthly_mail / 30)
count_for_loss = int(monthly_mail - (monthly_mail * .15))
#Format and convert to strings
daily_outbound_mail = "{:,}".format(daily_outbound_mail)
monthly_mail = "{:,}".format(monthly_mail)
count_for_loss = "{:,}".format(count_for_loss)

# Make pretty output to terminal

print("\n------------------------------------------")
print(f"{bcolors.BOLD}{bcolors.OKGREEN}        Managed VPS Email Stats{bcolors.ENDC}")
print("------------------------------------------")
print(f"{bcolors.OKBLUE}Total mail for 30 days: {bcolors.ENDC}" + f"         {bcolors.BOLD}" + monthly_mail + f"{bcolors.ENDC}")
print(f"{bcolors.OKBLUE}Daily outbound mail average: {bcolors.ENDC}" +  f"       {bcolors.BOLD}" + daily_outbound_mail + f"{bcolors.ENDC}")
print(f"{bcolors.OKBLUE}Monthly with possible 15% churn: {bcolors.ENDC}" + f"{bcolors.BOLD}" + count_for_loss + f"{bcolors.ENDC}")
print("------------------------------------------")
