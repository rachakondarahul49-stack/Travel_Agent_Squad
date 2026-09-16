from estimator import estimate_budget

result = estimate_budget(
    flight=10000,
    hotel=12000,
    activities=5000,
    budget=25000
)

print("Budget:", result["budget"])
print("Flight:", result["flight"])
print("Hotel:", result["hotel"])
print("Activities:", result["activities"])
print("Total Cost:", result["total_cost"])
print("Status:", result["status"])

if result["status"] == "OVER_BUDGET":
    print("Exceeded By:", result["over_by"])
else:
    print("Remaining:", result["remaining"])
