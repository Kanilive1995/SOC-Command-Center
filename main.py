print("==================================")
print("     SOC COMMAND CENTER")
print("==================================")

username = input("Enter your analyst username: ")
print("Welcome to the command center, ", username)

security_status = "Monitoring"
critical_count = 0
resolved_alerts = 2

print("System Status: ", security_status)
print("Resolved Alerts:", resolved_alerts)

alert_severity = input("Enter your alert severity (Critical/High/Medium/Low): ").lower()

if alert_severity == "critical":
    print("CRITICAL: Immediate investigation required!")
elif alert_severity == "high":
    print("HIGH: Investigate this security alert soon")
elif alert_severity == "medium":
    print("MEDIUM: monitor this security alert activity")
elif alert_severity == "low":
    print("LOW: monitor this security alert activity")
else:
    print("Invalid alert severity.")

security_alerts = ["Critical", "High", "Medium", "Low", "Critical"]
security_alerts.append("High")
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

remaining_alerts = total_alerts - resolved_alerts

print("Critical Alerts: ", critical_count)
print("Total Alerts: ", total_alerts)
print("Remaining Alerts: ", remaining_alerts)

