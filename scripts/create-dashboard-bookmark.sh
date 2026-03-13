#!/bin/bash
# Create Dashboard Bookmark
# Created: 2026-03-13

WORKSPACE=~/.openclaw/workspace
BOOKMARK_FILE=~/Desktop/Ken\ AI\ Dashboard.webloc

# Create .webloc file (macOS bookmark)
cat > "$BOOKMARK_FILE" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>URL</key>
    <string>file://$WORKSPACE/dashboard.html</string>
</dict>
</plist>
EOF

echo "✅ Desktop bookmark created: $BOOKMARK_FILE"
echo ""
echo "🖱️ Double-click to open Dashboard!"
