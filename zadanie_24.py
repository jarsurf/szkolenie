def increment_factory(step):

    def wrapper(liczba):
        return liczba + step
    return wrapper

incr_by_3 = increment_factory(3)
print(incr_by_3(5))