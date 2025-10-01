#!/usr/bin/env python3
"""
Script to create sample CSV data for testing the Investor Portal Dashboard
"""

import csv
from datetime import datetime, timedelta
import random

def create_sample_data():
    # Generate dates for the last 12 months
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    
    # Create monthly dates
    dates = []
    current = start_date
    while current <= end_date:
        # Move to end of month
        if current.month == 12:
            next_month = current.replace(year=current.year + 1, month=1, day=1)
        else:
            next_month = current.replace(month=current.month + 1, day=1)
        dates.append(current.strftime('%Y-%m-%d'))
        current = next_month
    
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
        vault_avg_return = round(random.uniform(5.0, 12.0), 2)
        modena_avg_cost = round(random.uniform(8.0, 15.0), 2)
        funds_in = random.randint(200000, 500000)
        funds_out = random.randint(150000, 400000)
        accrued_interest = random.randint(5000, 15000)
        bonuses = random.randint(2000, 8000)
        circlewise = random.randint(1000, 5000)
        influencers = random.randint(500, 3000)
        
        data.append([
            date,
            vault_assets,
            assets_pool,
            vault_avg_return,
            modena_avg_cost,
            funds_in,
            funds_out,
            accrued_interest,
            bonuses,
            circlewise,
            influencers
        ])
    
    return data

if __name__ == "__main__":
    # Create sample data
    data = create_sample_data()
    
    # Headers
    headers = [
        'Date',
        'Vault Assets',
        'Assets Pool', 
        'Vault avg return (%)',
        'Modena avg cost (%)',
        'Funds in',
        'Funds out',
        'Accrued Interest',
        'Bonuses',
        'Circlewise',
        'Influencers (Direct)'
    ]
    
    # Save to CSV file
    output_file = '/workspace/sample_dashboard_data.csv'
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(data)
    
    print(f"Sample data created: {output_file}")
    print(f"Data rows: {len(data)}")
    print("\nFirst few rows:")
    print(headers)
    for row in data[:3]:
        print(row)
    print("\nLast few rows:")
    for row in data[-3:]:
        print(row)