import pyotp
import time

def generate_totp_passcode(secret_key):
    
    totp = pyotp.TOTP(secret_key)
    return totp.now()

print("┌──────────────────────────────────────────────┐")
print("|   ____      _                _         _     |")
print("|  / ___|   _| |__   ___ _ __ / \\   _ __| | _  |")
print("| | |  | | | |  _ \\ / _ \\ '__/ _ \\ |  __| |/ / |")
print("| | |__| |_| | |_) |  __/ | / ___ \\| |  |   <  |")
print("|  \\____\\__, |_ __/ \\___|_|/_/   \\_\\_|  |_|\\_\\ |")
print("|       |___/   CPM & PSM Development Training |")
print("|                               TOTP Generator |")
print("└──────────────────────────────────────────────┘")
secret_key = input(" Enter your Athena Secret Key: ")
print("┌─────────────────────────────────────────────────┐")

try:
    while True:
        
        current_time = int(time.time())
        generated_passcode = generate_totp_passcode(secret_key)
        print(f"| Generated TOTP Passcode: {generated_passcode} (refreshing...) |")
        time_to_sleep = 30 - (current_time % 30)
        time.sleep(time_to_sleep)

except KeyboardInterrupt:
    print("| TOTP generation interrupted.                    |")
    print("└─────────────────────────────────────────────────┘")
