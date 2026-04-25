import random
import pandas as pd
from datetime import datetime, timedelta
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def generate_transactions(n=1000):
    logger.info(f"Generating {n} transactions")
    data = []

    for i in range(n):
        data.append({
            "txn_id": i,
            "account_id": random.randint(1000, 1100),
            "amount": round(random.uniform(100, 200000), 2),
            "transaction_type": random.choice(["DEBIT", "CREDIT"]),
            "location": random.choice(["India", "US", "UK"]),
            "timestamp": datetime.now() - timedelta(minutes=random.randint(0, 10000)),
            "is_fraud": 1 if random.random() < 0.05 else 0
        })

    df = pd.DataFrame(data)
    logger.info(f"Generated {len(df)} transactions successfully")
    return df