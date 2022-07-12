withdraw = int(input("Withdraw $: "))
notes = 50
counter = 0
while True:

    if withdraw >= notes:
        withdraw -= notes
        counter += 1
    else:
        if counter > 0:
            print(f"Get {counter} notes of $:{notes:.2f}")

        if notes == 50:
            notes = 20
        elif notes == 20:
            notes = 10
        elif notes == 10:
            notes = 1
        counter = 0
        if withdraw == 0:
            break
