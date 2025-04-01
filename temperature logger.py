days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
temps = {day: float(input(f"Enter temperature for {day}: ")) for day in days}

print("\nLogged Temperatures:")
for day, temp in temps.items():
    print(f"{day}: {temp}°C")

print("\nTemperature Summary:")
print(f"Average Temperature: {sum(temps.values()) / 7:.2f}°C")
print(f"Highest Temperature: {max(temps.values())}°C")
print(f"Lowest Temperature: {min(temps.values())}°C")
