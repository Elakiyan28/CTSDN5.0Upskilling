def salary_range(salaries: list[int]) -> tuple[int, int]:
    if not salaries:
        raise ValueError("Salary list cannot be empty")
    return min(salaries), max(salaries)

low, high = salary_range([50000, 75000, 62000, 95000])
print(f"Lowest: {low}, Highest: {high}")
