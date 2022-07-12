def vote(year_of_birth_user):
    """ This function gets the system date with lib datetime and calculates the birth year the user entered
    :param year_of_birth_user:
    :return: Year current
    """
    import datetime
    date_current = datetime.datetime.now()
    year_current = date_current.year - year_of_birth_user

    if year_current < 16:
        print(f"{year_current} year old")
        print("Denied vote")
    if year_current < 16:
        print(f"{year_current} year old")
        print("Denied vote")
    if 16 <= year_current < 18:
        print(f"{year_current} year old")
        print("Factuative vote")
    if year_current > 70:
        print(f"{year_current} year old")
        print(f"Factuative vote")
    if 18 <= year_current <= 70:
        print(f"{year_current} year old")
        print("Mandatory vote")


year_of_birth_input = int(input("Year: "))
vote(year_of_birth_input)


