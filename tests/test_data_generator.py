import pytest
import pandas as pd
from src.ingestion.data_generator import generate_transactions


def test_generate_transactions():
    df = generate_transactions(100)
    assert len(df) == 100
    assert 'txn_id' in df.columns
    assert 'account_id' in df.columns
    assert 'amount' in df.columns
    assert 'transaction_type' in df.columns
    assert 'location' in df.columns
    assert 'timestamp' in df.columns
    assert 'is_fraud' in df.columns
    assert df['txn_id'].is_unique
    assert df['amount'].min() >= 100
    assert df['amount'].max() <= 200000
    assert df['transaction_type'].isin(['DEBIT', 'CREDIT']).all()
    assert df['location'].isin(['India', 'US', 'UK']).all()
    assert df['is_fraud'].isin([0, 1]).all()


def test_generate_transactions_fraud_rate():
    df = generate_transactions(10000)
    fraud_rate = df['is_fraud'].mean()
    assert 0.03 <= fraud_rate <= 0.07  # Approximate 5% fraud rate