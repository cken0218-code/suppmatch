"""Slack Integration Examples"""
from composio_wrapper import ComposioWrapper

wrapper = ComposioWrapper()

# Send a simple message
print("=== Sending Slack Message ===")
result = wrapper.slack_send_message(
    channel="#notifications",
    message="🚀 Deployment completed successfully!"
)
print(f"Message sent: {result['success']}")

# Send formatted message
print("\n=== Sending Formatted Message ===")
message = """
*Daily Report*
- Tasks completed: 5
- In progress: 3
- Blocked: 1
"""
wrapper.slack_send_message(
    channel="#daily-updates",
    message=message
)
print("Formatted message sent!")
