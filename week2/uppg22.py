'''Detta ger en kort introduktion till dekoratorer och deras användning. Skapa en enkel decorator timer som mäter exekveringstiden för en funktion:

    Implementera decorator timer.
    Använd time modulen för att mäta tiden.
    Applicera dekoratorn på några funktioner med olika exekveringstider.
    Forska lite på nätet hur dekoratorer fungerar och deras användningsområden.
'''
import time
import functools

def timer(func):
    @functools.wraps(func)
    def exekveterings(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        stop_time = time.time()
        exekveteringstid = stop_time - start_time
        print(f"{func.__name__} took {exekveteringstid:.4f} sec to run")

        return result
    
    return exekveterings

@timer
def sleeping():
    time.sleep(2)
    print("Slow sleep function done")

sleeping()

