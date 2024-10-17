from booking.booking import Booking

with Booking() as bot:
    bot.open_website()
    bot.change_currency(currency='EUR')
    bot.select_place_togo(place='New York')
    bot.select_dates(check_in_date='2024-10-17', check_out_date='2024-10-30')
    bot.select_confs(adults=2, rooms=2, children=2, age=f"{2} years old")
    print("Exiting...")