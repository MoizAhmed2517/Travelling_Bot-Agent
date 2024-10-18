from booking.booking import Booking
from booking.validations import get_valid_age

#Input mechanism

num_children = int(input("Enter the number of children: "))
ages_kwargs = {f'age_{i + 1}': get_valid_age(i + 1) for i in range(num_children)}

with Booking() as bot:
    bot.open_website()
    bot.change_currency(currency='EUR')
    bot.select_place_togo(place='New York')
    bot.select_dates(check_in_date='2024-10-17', check_out_date='2024-10-30')
    bot.select_confs(adults=4, rooms=2, children=num_children, **ages_kwargs)
    print("Exiting...")