def net_salary(salary: float, tax_rate: float) -> float:
    if salary <= 0 or not (0 <= tax_rate <= 1):
        raise ValueError("Invalid salary or tax rate")
    return round(salary * (1 - tax_rate), 2)

print("Net Salary after tax:", net_salary(75000.5, 0.18))
