"""
Slack Integration Example for Composio Wrapper

This example demonstrates Slack-related tool usage.
Note: You need to connect Slack in your Composio dashboard first.
"""

import os
from dotenv import load_dotenv
from composio_wrapper import ComposioWrapper, ComposioConfig

# Load environment variables
load_dotenv()


def main():
    api_key = os.getenv("COMPOSIO_API_KEY")
    if not api_key:
        print("Error: COMPOSIO_API_KEY not set")
        return
    
    config = ComposioConfig(api_key=api_key)
    wrapper = ComposioWrapper(config)
    
    user_id = "slack_demo_user"
    
    print("=== Slack Integration Demo ===\n")
    
    try:
        # Create session
        session = wrapper.create_session(user_id)
        print("✅ Session created\n")
        
        # Example 1: List channels
        print("1. Listing Slack channels...")
        result = wrapper.execute_tool(
            user_id=user_id,
            tool_name="slack_list_channels",
            params={}
        )
        
        if result.success:
            channels = result.data.get('channels', [])
            print(f"   ✅ Found {len(channels)} channels:")
            for channel in channels[:5]:
                print(f"   - #{channel.get('name')} (ID: {channel.get('id')})")
        else:
            print(f"   ❌ Error: {result.error}")
            print("   Note: Make sure Slack is connected in Composio dashboard")
            
        print()
        
        # Example 2: Send a message
        print("2. Sending a message to #general...")
        result = wrapper.execute_tool(
            user_id=user_id,
            tool_name="slack_send_message",
            params={
                "channel": "#general",
                "text": "Hello from Composio Wrapper! 🤖"
            }
        )
        
        if result.success:
            print("   ✅ Message sent successfully!")
            print(f"   Message ID: {result.data.get('ts')}")
        else:
            print(f"   ❌ Error: {result.error}")
            
        print()
        
        # Example 3: Create a channel (optional)
        print("3. Creating a new channel...")
        result = wrapper.execute_tool(
            user_id=user_id,
            tool_name="slack_create_channel",
            params={
                "name": "composio-test-channel",
                "description": "Test channel created by Composio wrapper"
            }
        )
        
        if result.success:
            channel = result.data
            print(f"   ✅ Created channel: #{channel.get('name')}")
            print(f"   Channel ID: {channel.get('id')}")
        else:
            print(f"   ❌ Error: {result.error}")
            print("   (Channel might already exist)")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
