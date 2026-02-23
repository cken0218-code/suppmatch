"""Google Sheets Integration Examples"""
from composio_wrapper import ComposioWrapper

wrapper = ComposioWrapper()

# Read data from a sheet
print("=== Reading Google Sheet ===")
data = wrapper.sheets_read(
    spreadsheet_id="abc123xyz",
    range_name="Data!A1:D10"
)
print("Sheet data:", data)

# Write data to a sheet
print("\n=== Writing to Google Sheet ===")
values = [
    ["Name", "Email", "Phone"],
    ["John Doe", "john@example.com", "555-1234"],
    ["Jane Smith", "jane@example.com", "555-5678"]
]
result = wrapper.sheets_write(
    spreadsheet_id="abc123xyz",
    range_name="Contacts!A1",
    values=values
)
print(f"Wrote {result['rows_written']} rows")
