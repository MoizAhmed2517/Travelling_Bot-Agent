from booking.booking import Booking

with Booking() as bot:
    bot.open_website()
    bot.change_currency(currency='BRL')
    bot.select_place_togo(place='New York')
    print("Exiting...")