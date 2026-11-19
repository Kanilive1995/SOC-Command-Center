print("==================================")
print("     SOC COMMAND CENTER")
print("==================================")

username = input("Enter your analyst username: ")
print("Welcome to the command center, ", username)

security_status = "Monitoring"
critical_count = 0
analyst_score = 0

print("System Status: ", security_status)

security_alerts = ["Critical", "High", "Medium", "Low"]
resolved_list = []
unresolved_list = []

def calculate_score(severity):
    if severity.lower() == "critical":
        return 10
    elif severity.lower() == "high":
        return 7
    elif severity.lower() == "medium":
        return 5
    elif severity.lower() == "low":
        return 2
    else:
        return 0


# security_alerts.append("High")
total_alerts = len(security_alerts)

for alert in security_alerts:
    if alert.lower() == "critical":
        critical_count += 1
        print("Critical: Immediate investigation required!:")

    elif alert.lower() == "high":
        print("High: Investigate this alert soon.")

    elif alert.lower() == "medium":
        print("Medium: monitor this activity.")

    elif alert.lower() == "low":
        print("Low: No immediate action required.")

    decision = input("Resolve this alert? (yes/no): ").lower().strip()
    if decision == "yes":
        resolved_list.append(alert)
        analyst_score += calculate_score(alert)
        print("Alerts marked resolved.")
    else:
        unresolved_list.append(alert)
        print("Alerts remain unresolved.")

resolved_alerts = len(resolved_list)
unresolved_alerts = len(unresolved_list)

print("Resolved Alerts:", resolved_alerts)
print("Unresolved Alerts:", unresolved_alerts)
print("Unresolved Alert Details:")
for alert in unresolved_list:
    print("-", alert)



remaining_alerts = total_alerts - resolved_alerts

print("Critical Alerts: ", critical_count)
print("Total Alerts: ", total_alerts)
print("Remaining Alerts: ", remaining_alerts)
print("Analyst Score: ", analyst_score)