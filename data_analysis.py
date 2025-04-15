def analyze_data(df):
    print("\n" + "="*50)
    print("1. SUMMARY STATISTICS & KEY METRICS")
    print("="*50)
    print(df[['Price', 'Mileage', 'Manufacture_Year']].describe())

    print("\nTotal Unique Brands:", df['Make'].nunique())
    print("Total Unique Models:", df['Model'].nunique())
    print("Most Common Transmission Type:", df['Transmission'].mode()[0])
    print("Most Common Fuel Type:", df['Fuel_Type'].mode()[0])

    print("\n" + "="*50)
    print("2. TOP 10 MOST LISTED CAR MODELS")
    print("="*50)
    top_models = df.groupby(['Make', 'Model']).size().sort_values(ascending=False).head(10)
    print(top_models)

    print("\n" + "="*50)
    print("3. BEST RESALE VALUE CARS (Lowest Price-to-Mileage Ratio)")
    print("="*50)
    df['Resale_Value_Score'] = df['Price'] / df['Mileage']
    best_resale_value = df[df['Mileage'] > 0].sort_values(by='Resale_Value_Score').head(10)
    print(best_resale_value[['Make', 'Model', 'Price', 'Mileage', 'Resale_Value_Score']])

    print("\n" + "="*50)
    print("4. MARKET TRENDS & BUYER PREFERENCES")
    print("="*50)
    trans_dist = df['Transmission'].value_counts()
    fuel_dist = df['Fuel_Type'].value_counts()

    print("\nTransmission Type Distribution:")
    print(trans_dist)

    print("\nFuel Type Distribution:")
    print(fuel_dist)

    return top_models, trans_dist, fuel_dist
