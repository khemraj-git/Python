import time


print("====countdown timer===")
print("count down from your chosen seconds")

while True:
    seconds = int(input(f"enter seconds to countdown from: "))
    print()
    print(f"starting countdown from {seconds} second")
    for i in range(seconds,0,-1):
        print(f"{i} seconds remaining...")
        time.sleep(1)
        i+=1
    print(f"countdown complete")
    print()
    choice = input("start another countdown? (yes/no): ")

    if choice.lower() != "yes":
        print("thanks for using the countdown timer!")
        break

