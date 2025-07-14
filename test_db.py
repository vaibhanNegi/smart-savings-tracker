from database import engine

try:
    with engine.connect() as conn:
        result = conn.execute("SELECT 1;")
        print("✅ Connection successful:", result.scalar())
except Exception as e:
    print("❌ Connection failed:", e)
