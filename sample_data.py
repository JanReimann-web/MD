#!/usr/bin/env python3
"""
Script to create sample Excel data for testing the Investor Portal Dashboard
"""

import pandas as pd
from datetime import datetime, timedelta
import random

# Create sample data for the dashboard
def create_sample_data():
    # Generate dates for the last 12 months
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    dates = pd.date_range(start=start_date, end=end_date, freq='M')
    
    # Sample data structure based on the dashboard requirements
    data = []
    
    # Starting values
    vault_assets = 800000
    assets_pool = 650000
    
    for i, date in enumerate(dates):
        # Simulate some growth and volatility
        vault_assets += random.randint(-50000, 100000)
        assets_pool += random.randint(-40000, 80000)
        
        # Ensure values don't go negative
        vault_assets = max(vault_assets, 500000)
        assets_pool = max(assets_pool, 400000)
        
        # Generate other metrics
        vault_avg_return = random.uniform(5.0, 12.0)
        modena_avg_cost = random.uniform(8.0, 15.0)
        funds_in = random.randint(200000, 500000)
        funds_out = random.randint(150000, 400000)
        accrued_interest = random.randint(5000, 15000)
        bonuses = random.randint(2000, 8000)
        circlewise = random.randint(1000, 5000)
        influencers = random.randint(500, 3000)
        
        data.append({
            'Date': date.strftime('%Y-%m-%d'),
            'Vault Assets': vault_assets,
            'Assets Pool': assets_pool,
            'Vault avg return (%)': vault_avg_return,
            'Modena avg cost (%)': modena_avg_cost,
            'Funds in': funds_in,
            'Funds out': funds_out,
            'Accrued Interest': accrued_interest,
            'Bonuses': bonuses,
            'Circlewise': circlewise,
            'Influencers (Direct)': influencers
        })
    
    return pd.DataFrame(data)

if __name__ == "__main__":
    # Create sample data
    df = create_sample_data()
    
    # Save to Excel file
    output_file = '/workspace/sample_dashboard_data.xlsx'
    df.to_excel(output_file, index=False, sheet_name='Leht1')
    
    print(f"Sample data created: {output_file}")
    print(f"Data shape: {df.shape}")
    print("\nFirst few rows:")
    print(df.head())
    print("\nLast few rows:")
    print(df.tail())