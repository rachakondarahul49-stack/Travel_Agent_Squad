from calculator import calculate_total

def estimate_budget(flight, hotel, activities, budget):
    total = calculate_total(flight, hotel, activities)

    if total > budget:
        return {
            "flight": flight,
            "hotel": hotel,
            "activities": activities,
            "total_cost": total,
            "budget": budget,
            "status": "OVER_BUDGET",
            "over_by": total - budget
        }

    return {
        "flight": flight,
        "hotel": hotel,
        "activities": activities,
        "total_cost": total,
        "budget": budget,
        "status": "WITHIN_BUDGET",
        "remaining": budget - total
    }
