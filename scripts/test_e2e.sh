#!/bin/bash
# scripts/test_e2e.sh

set -e

PROJECT_ROOT=$(pwd)
PSQL_BIN="/opt/homebrew/opt/postgresql@15/bin/psql"
CREATEDB_BIN="/opt/homebrew/opt/postgresql@15/bin/createdb"
DROPDB_BIN="/opt/homebrew/opt/postgresql@15/bin/dropdb"

TEST_DB_NAME="testdb_$(date +%s)"
DB_USER="martin"

# 1. Create a clean test database
echo "🚀 Creating transient PostgreSQL database: $TEST_DB_NAME..."
$CREATEDB_BIN $TEST_DB_NAME

# 2. Setup environment variables for the test
export DATABASE_URL="postgresql+psycopg://$DB_USER@localhost:5432/$TEST_DB_NAME"

# 3. Initialize the database
echo "🛠️ Initializing database schema..."
cd backend
source ../.venv-fastapi/bin/activate
# Run as module to handle relative imports
python3 -m app.database.init

# 4. Start the app in the background
echo "🏃 Starting FastAPI app..."
python3 -m app.main &
APP_PID=$!

# Wait for app to start
sleep 3

# 5. Run a test request
echo "🧪 Running end-to-end test..."
RESPONSE=$(curl -s http://localhost:5001/api/status)
echo "Response: $RESPONSE"

if [[ $RESPONSE == *"status\":\"online\""* ]] && [[ $RESPONSE == *"source\":\"database\""* ]]; then
  echo "✅ Test Passed!"
  EXIT_CODE=0
else
  echo "❌ Test Failed!"
  EXIT_CODE=1
fi

# 6. Teardown
echo "🧹 Cleaning up..."
kill $APP_PID || true
$DROPDB_BIN $TEST_DB_NAME

exit $EXIT_CODE
