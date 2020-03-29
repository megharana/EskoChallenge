Question :

With the Indian government introducing private trains, several new companies are coming forward to establish private rail transportation services. RailIndia is one such new rail transportation company offering national rail transport in India with connections to several regional cities. RailIndia plans to offer travelers both direct trains and options with connecting trains. The company is developing an online portal to search for available trains between two cities and make reservations.
You are assigned to develop a search algorithm that lists the available trains from a city A to another city B. The algorithm must order the listing in price ascending order with the cheapest train on top. If there are multiple trains for the same cost, the train with lesser connections must be ordered higher. In case there are multiple trains with the same cost and the same number of connections, then they are ordered alphabetically.

The first line of the input contains the two cities for whom search is requested – the departure city and the arrival city, separated by a white-space.&nbsp; The city name will be no longer than 20 characters and will not contain any white-space characters.

The next N lines will contain the available trains and their costs. N will be &lt;= 50. Each line is a direct train starting with the departure city name, followed by the arrival city name, and lastly followed by the cost of that train (in Rupees) – all three separated by a white-space character.

The output is a list of M lines. Each line is one train listing. Each of the M lines start with the departure city name, followed by a sequence of connecting city names (if exists), then followed by the arrival city name, and lastly followed by the total cost of that option. All of them separated by a white-space character. When there are zero trains available, the output must contain a single line of text 




- Input:
Bangalore Hyderabad
Bangalore Hyderabad 10000
Bangalore Chennai 4000
Chennai Hyderabad 4000

- Output:
Bangalore Chennai Hyderabad 8000
Bangalore Hyderabad 10000