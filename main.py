print("==================================")
print("     SOC COMMAND CENTER")
print("==================================")

username = input("Enter your analyst username: ")
print("Welcome to the command center, ", username)

alert_count = 5
security_status = "Monitoring"
critical_alerts = 2

print("System Status: ", security_status)
print("Total Alerts: ", alert_count)
print("Critical Alerts: ", critical_alerts)

total_alerts = 5
resolved_alerts = 2

remaining_alerts = total_alerts - resolved_alerts

print("Total Alerts :" , total_alerts)
print("Resolved Alerts:", resolved_alerts)
print("Remaining Alerts:", remaining_alerts)

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

