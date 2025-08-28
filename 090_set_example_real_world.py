# Email subscribers from two campaigns
campaign_A = {"Anand", "Bhanu", "Chandu"}
campaign_B = {"Anand", "Dinesh", "Ezhil"}

# Find users who subscribed to both
common_subscribers = campaign_A & campaign_B
print("Common subscriber(s):", common_subscribers)
print()

# All unique unique subscribers
all_subscribers = campaign_A | campaign_B
print("All subscriber(s):", all_subscribers)