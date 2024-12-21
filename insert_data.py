import pandas as pd
from models import db, Product, Discography
from app import app

def insert_data_from_excel():
    # Load the Excel file
    excel_file = 'purple_dreams.xlsx'

    # Read Product data from the first sheet
    product_df = pd.read_excel(excel_file, sheet_name='Product')
    # Insert Product data into the Product table
    with app.app_context():
        if not Product.query.first():
            for index, row in product_df.iterrows():
                product = Product(
                    name=row['name'],
                    price=row['price'],
                    image=row['image']
                )
                db.session.add(product)
            db.session.commit()
            print("Products added from Excel!")

        # Read Discography data from the second sheet
        discography_df = pd.read_excel(excel_file, sheet_name='Discography')
        # Insert Discography data into the Discography table
        if not Discography.query.first():
            for index, row in discography_df.iterrows():
                # Ensure duration is stored as a string (e.g., "3:21")
                duration_str = str(row['duration'])  # Converts time object or any other format to string
                discography = Discography(
                    artist=row['artist'],
                    album_name=row['album_name'],
                    song_name=row['song_name'],
                    release_date=row['release_date'],  # Ensure YYYY-MM-DD format
                    duration=duration_str  # Store as a string
                )
                db.session.add(discography)
            db.session.commit()
            print("Discography added from Excel!")

# Run the function to insert the data
insert_data_from_excel()
