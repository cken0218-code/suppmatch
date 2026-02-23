"""
Basic Usage Example for Composio Wrapper

This example demonstrates basic initialization and tool usage.
"""

import os
from dotenv import load_dotenv
from composio_wrapper import ComposioWrapper, ComposioConfig

# Load environment variables
load_dotenv()


def main():
    # Get API key from environment
    api_key = os.getenv("COMPOSIO_API_KEY")
    if not api_key:
        print("Error: COMPOSIO_API_KEY not set")
        print("Get your key from: https://platform.composio.dev/settings")
        return
    
    # Initialize the wrapper
    config = ComposioConfig(api_key=api_key)
    wrapper = ComposioWrapper(config)
    
    # Define a user ID (can be any string that uniquely identifies the user)
    user_id = "demo_user"
    
    print(f"Creating session for user: {user_id}")
    
    try:
        # Create a session
        session = wrapper.create_session(user_id)
        print(f"✅ Session created successfully")
        
        # Get available tools
        tools = wrapper.get_tools(user_id)
        print(f"✅ Available tools: {len(tools)}")
        
        # List first 10 tools
        print("\nFirst 10 available tools:")
        for i, tool in enumerate(tools[:10], 1):
            print(f"  {i}. {tool.name}")
        
        if len(tools) > 10:
            print(f"  ... and {len(tools) - 10} more")
            
        # List all available tools with descriptions
        print("\n--- All Available Tools ---")
        tool_list = wrapper.list_available_tools(user_id)
        for tool in tool_list:
            print(f"\n{tool['name']}")
            if tool.get('description'):
                print(f"  {tool['description']}")
                
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
