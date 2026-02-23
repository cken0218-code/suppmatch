#!/bin/bash

# Multi-Agent Dispatcher
# Usage: ./dispatcher.sh [task]

TASK="$1"

if [ -z "$TASK" ]; then
    echo "Usage: ./dispatcher.sh <task>"
    echo "Example: ./dispatcher.sh 'Research: 最新的AI trends'"
    exit 1
fi

# Extract action type
if [[ "$TASK" == Research:* ]]; then
    echo "→ Routing to Researcher (MiniMax)..."
    # Call researcher agent
elif [[ "$TASK" == Build:* ]]; then
    echo "→ Routing to Engineer (GLM-5)..."
    # Call engineer agent
elif [[ "$TASK" == Review:* ]]; then
    echo "→ Routing to Reviewer (MiniMax)..."
    # Call reviewer agent
else
    echo "→ Handling directly (GLM-5)..."
    # Handle directly
fi

echo ""
echo "Task: $TASK"
