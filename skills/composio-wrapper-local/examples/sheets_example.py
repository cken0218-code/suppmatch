"""
Google Sheets Integration Example for Composio Wrapper

This example demonstrates Google Sheets-related tool usage.
Note: You need to connect Google Sheets in your Composio dashboard first.
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
    
    user_id = "sheets_demo_user"
    
    print("=== Google Sheets Integration Demo ===\n")
    
    try:
        # Create session
        session = wrapper.create_session(user_id)
        print("✅ Session created\n")
        
        # Example 1: Create a new spreadsheet
        print("1. Creating a new spreadsheet...")
        result = wrapper.execute_tool(
            user_id=user_id,
            tool_name="googlesheets_create_spreadsheet",
            params={
                "title": "Composio Demo Sheet",
                "sheet_title": "Demo Sheet"
            }
        )
        
        if result.success:
            spreadsheet_id = result.data.get('spreadsheet_id')
            print(f"   ✅ Created spreadsheet: {spreadsheet_id}")
        else:
            print(f"   ❌ Error: {result.error}")
            print("   Note: Make sure Google Sheets is connected in Composio dashboard")
            return
            
        print()
        
        # Example 2: Write some data
        print("2. Writing data to spreadsheet...")
        
        # First, add headers
        result = wrapper.execute_tool(
            user_id=user_id,
            tool_name="googlesheets_update_spreadsheet",
            params={
                "spreadsheet_id": spreadsheet_id,
                "sheet_range": "Demo Sheet!A1:D1",
                "values": [["Name", "Email", "Role", "Status"]]
            }
        )
        
        if result.success:
            print("   ✅ Added headers")
        else:
            print(f"   ❌ Error: {result.error}")
        
        # Add some data rows
        result = wrapper.execute_tool(
            user_id=user_id,
            tool_name="googlesheets_append_rows",
            params={
                "spreadsheet_id": spreadsheet_id,
                "sheet_title": "Demo Sheet",
                "values": [
                    ["John Doe", "john@example.com", "Admin", "Active"],
                    ["Jane Smith", "jane@example.com", "User", "Active"],
                    ["Bob Wilson", "bob@example.com", "User", "Inactive"]
                ]
            }
        )
        
        if result.success:
            print("   ✅ Added 3 data rows")
        else:
            print(f"   ❌ Error: {result.error}")
            
        print()
        
        # Example 3: Read the data back
        print("3. Reading data from spreadsheet...")
        result = wrapper.execute_tool(
            user_id=user_id,
            tool_name="googlesheets_read_spreadsheet",
            params={
                "spreadsheet_id": spreadsheet_id,
                "sheet_range": "Demo Sheet!A1:D4"
            }
        )
        
        if result.success:
            data = result.data.get('values', [])
            print(f"   ✅ Read {len(data)} rows:")
            for row in data:
                print(f"   - {' | '.join(row)}")
        else:
            print(f"   ❌ Error: {result.error}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
