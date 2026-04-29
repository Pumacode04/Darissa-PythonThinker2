# ============================================================
# Step 1: Create the list
# ============================================================

daily_sales = [1205, 986, 1354, 10535, 15741, 11200,
               800, 13056, 952, 1100, 1025, 8574,
               14014, 9987, 1238, 1458, 7803, 900,
               13674, 14539, 13241, 10886, 7541, 8743,
               1482, 11523, 977, 12181, 8903, 1008, 1530]

# ============================================================
# Step 2: Find highest sales
# ============================================================
day = 0
highest = max(daily_sales)
lowest = min(daily_sales)
counter = 0
for i in daily_sales:
    if i == highest:
        day = counter
    else:
        counter += 1

# ============================================================
# Step 3: Find lowest sales
# ============================================================
day = 0
counter = 0
for i in daily_sales:
    if i == lowest:
        day = counter
    else:
        counter += 1

# ============================================================
# Step 4: Calculate average sales (round to 2 decimal places)
# ============================================================
total = 0
average = 0
length = len(daily_sales)
for i in daily_sales:
    total += i
average = total / length
average = round(average, 2)

# ============================================================
# Step 5: Print results in correct format
# ============================================================
print(f"{day + 1} August has the highest sales of ${highest}")
print(f"{day + 1} August has the lowest sales of ${lowest}")
print(f"Average daily sales for August is ${average}")
