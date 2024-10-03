'''Skapa ett linjediagram som visar temperaturdata för en vecka. 
    Som "data" räcker det t.ex. att skapa en lista med sju floats,
    en för varje dags medeltemperatur. 
    ex: [15.5, 16.0, 14.6, 11.9, 15.3, 16.2, 15.7] 
    Använd matplotlib för att:

    Plotta temperaturerna.
    Lägga till en titel och etiketter för x- och y-axlarna.
    Anpassa linjefärg och stil.
'''

import matplotlib.pyplot as plt
temp = [15.5, 16.0, 14.6, 11.9, 15.3, 16.2, 15.7]

plt.plot(temp, color='green', linestyle='--', label='temperatur')

plt.xlabel('x-Axis')
plt.ylabel('y-Axis')
plt.title('Median Temperature in Sweden')
plt.legend()

plt.show()

