def ft_count_harvest_recursive() -> None:
    def count_day(current: int, target: int) -> None:
        if current > target:
            return
        print(f"Day {current}")
        count_day(current + 1, target)

    days = int(input("Days until harvest: "))
    count_day(1, days)
    print("Harvest time!")
