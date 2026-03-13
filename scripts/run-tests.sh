#!/bin/bash
# Automated Test Suite
# Created: 2026-03-13
# Purpose: Run automated tests for all systems

TESTS_PASSED=0
TESTS_FAILED=0
TESTS_TOTAL=0

echo "🧪 OpenClaw Automated Test Suite"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Timestamp: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# Function to run test
run_test() {
  local test_name=$1
  local test_command=$2

  echo "Testing: $test_name"
  TESTS_TOTAL=$((TESTS_TOTAL + 1))

  if eval "$test_command" > /dev/null 2>&1; then
    echo "  ✅ PASS"
    TESTS_PASSED=$((TESTS_PASSED + 1))
    return 0
  else
    echo "  ❌ FAIL"
    TESTS_FAILED=$((TESTS_FAILED + 1))
    return 1
  fi
}

# Function to run test with output
run_test_verbose() {
  local test_name=$1
  local test_command=$2

  echo "Testing: $test_name"
  TESTS_TOTAL=$((TESTS_TOTAL + 1))

  OUTPUT=$(eval "$test_command" 2>&1)
  EXIT_CODE=$?

  if [ $EXIT_CODE -eq 0 ]; then
    echo "  ✅ PASS"
    TESTS_PASSED=$((TESTS_PASSED + 1))
    return 0
  else
    echo "  ❌ FAIL"
    echo "  Error: $OUTPUT"
    TESTS_FAILED=$((TESTS_FAILED + 1))
    return 1
  fi
}

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📁 Memory System Tests"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

run_test "Memory directory exists" \
  "test -d ~/.openclaw/workspace/memory"

run_test "Identity compact file exists" \
  "test -f ~/.openclaw/workspace/memory/identity-compact.md"

run_test "L1-daily directory exists" \
  "test -d ~/.openclaw/workspace/memory/L1-daily"

run_test "Today's log exists" \
  "test -f ~/.openclaw/workspace/memory/L1-daily/$(date +%Y-%m-%d).md"

run_test "User patterns file exists" \
  "test -f ~/.openclaw/workspace/memory/user-patterns.md"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📝 Configuration Tests"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

run_test "OpenClaw config exists" \
  "test -f ~/.openclaw/openclaw.json"

run_test "AGENTS.md exists" \
  "test -f ~/.openclaw/workspace/AGENTS.md"

run_test "SOUL.md exists" \
  "test -f ~/.openclaw/workspace/SOUL.md"

run_test "USER.md exists" \
  "test -f ~/.openclaw/workspace/USER.md"

run_test "HEARTBEAT.md exists" \
  "test -f ~/.openclaw/workspace/HEARTBEAT.md"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🤖 Skills Tests"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

run_test "Skills directory exists" \
  "test -d ~/.openclaw/workspace/skills"

run_test "self-improving-agent installed" \
  "test -d ~/.openclaw/workspace/skills/self-improving-agent"

run_test "self-improving-agent SKILL.md exists" \
  "test -f ~/.openclaw/workspace/skills/self-improving-agent/SKILL.md"

run_test "youtube-agent exists" \
  "test -d ~/.openclaw/workspace/skills/youtube-agent"

run_test "stock-agent exists" \
  "test -d ~/.openclaw/workspace/skills/stock-agent"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🛠️ Scripts Tests"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

run_test "Scripts directory exists" \
  "test -d ~/.openclaw/workspace/scripts"

run_test "check-system-health.sh exists" \
  "test -f ~/.openclaw/workspace/scripts/check-system-health.sh"

run_test "check-system-health.sh is executable" \
  "test -x ~/.openclaw/workspace/scripts/check-system-health.sh"

run_test "generate-daily-summary.sh exists" \
  "test -f ~/.openclaw/workspace/scripts/generate-daily-summary.sh"

run_test "track-token-usage.py exists" \
  "test -f ~/.openclaw/workspace/scripts/track-token-usage.py"

run_test "check-api-health.sh exists" \
  "test -f ~/.openclaw/workspace/scripts/check-api-health.sh"

run_test "visualize-token-usage.py exists" \
  "test -f ~/.openclaw/workspace/scripts/visualize-token-usage.py"

run_test "monitor-agent-performance.py exists" \
  "test -f ~/.openclaw/workspace/scripts/monitor-agent-performance.py"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔌 System Integration Tests"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

run_test "Gateway is running" \
  "pgrep -f openclaw-gateway > /dev/null"

run_test "Git repository is clean" \
  "cd ~/.openclaw/workspace && git diff-index --quiet HEAD --"

run_test "Python 3 is available" \
  "command -v python3 > /dev/null"

run_test "Node is available" \
  "command -v node > /dev/null"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎨 Script Functionality Tests"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

run_test_verbose "check-system-health.sh runs" \
  "~/.openclaw/workspace/scripts/check-system-health.sh > /dev/null"

run_test_verbose "generate-daily-summary.sh runs" \
  "~/.openclaw/workspace/scripts/generate-daily-summary.sh > /dev/null"

run_test_verbose "track-token-usage.py runs" \
  "python3 ~/.openclaw/workspace/scripts/track-token-usage.py 1 > /dev/null"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 Test Results"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

echo ""
echo "Total Tests:  $TESTS_TOTAL"
echo "Passed:       $TESTS_PASSED ✅"
echo "Failed:       $TESTS_FAILED ❌"
echo ""

if [ $TESTS_FAILED -eq 0 ]; then
  echo "🎉 All tests passed!"
  EXIT_CODE=0
else
  echo "⚠️ Some tests failed. Please check above for details."
  EXIT_CODE=1
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Test suite complete"
echo ""

# Save test results
TEST_LOG=~/.openclaw/workspace/memory/test-results-$(date +%Y-%m-%d).txt
{
  echo "Test Results - $(date '+%Y-%m-%d %H:%M:%S')"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "Total: $TESTS_TOTAL"
  echo "Passed: $TESTS_PASSED"
  echo "Failed: $TESTS_FAILED"
  echo ""
  if [ $TESTS_FAILED -eq 0 ]; then
    echo "Status: ✅ All tests passed"
  else
    echo "Status: ❌ Some tests failed"
  fi
} > "$TEST_LOG"

echo "Test log saved to: $TEST_LOG"

exit $EXIT_CODE
