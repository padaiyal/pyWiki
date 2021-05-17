from wiki.utils.time_it import time_it_in_milliseconds


@time_it_in_milliseconds
def convert_years_to_months_fail_late(years: int) -> int:
    if years > -1:
        return years * 12
    else:
        raise Exception("Years has to be a positive value.")


@time_it_in_milliseconds
def convert_years_to_months_fail_fast(years: int) -> int:
    if years < 0:
        raise Exception("Years has to be a positive value.")
    else:
        return years * 12


if __name__ == '__main__':
    years = -100
    n = 1000
    fail_late_duration = sum(convert_years_to_months_fail_late(years) for years in range(-n, -1))/n
    fail_fast_duration = sum(convert_years_to_months_fail_fast(years) for years in range(-n, -1))/n
    print(f"Average time taken on failing late {n} times: "
          f"{fail_late_duration} milliseconds.")
    print(f"Average time taken on failing fast {n} times: "
          f"{fail_fast_duration} milliseconds.")
