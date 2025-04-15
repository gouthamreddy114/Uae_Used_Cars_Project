def insert_into_db(df, conn):
    cursor = conn.cursor()
    insert_query = """
        INSERT INTO used_cars (Make, Model, Manufacture_year, Price, Mileage, Fuel_type, Transmission, Color, Location, About)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    data_to_insert = [
        (
            row['Make'],
            row['Model'],
            int(row['Manufacture_Year']),
            float(row['Price']),
            int(row['Mileage']),
            row['Fuel_Type'],
            row['Transmission'],
            row['Color'],
            row['Location'],
            row['About']
        )
        for _, row in df.iterrows()
    ]

    cursor.executemany(insert_query, data_to_insert)
    conn.commit()
    cursor.close()
    print("Data inserted successfully into the database.")
