# Day Two😁😂😂😁😁


def solve(meal_cost, tip_percent, tax_percent):
    """
    this helps in fetching the cost of items(meals e.t.c), percentage tips (on meals) & tax (on meals)
    """
    tip = (meal_cost * 0.01) * tip_percent
    tax = (tax_percent * 0.01) * meal_cost

    total_cost = meal_cost + tip + tax
    print(round(total_cost))


if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
