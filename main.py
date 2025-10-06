from InventorySystem import Inventory
import os
import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',            
    database='inventory_db' 
)


try:
    with connection:
        cursor = connection.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS products (' 
                'id INT AUTO_INCREMENT PRIMARY KEY,'
                'name VARCHAR(255) NOT NULL,'
                'price DECIMAL(10, 2) NOT NULL,'
                'quantity INT NOT NULL'
            ')'
        )
        print("✅ Database and table ready")
        print(50 * "-----")
        print("📦 Welcome to Inventory System")

        connection.commit()

except pymysql.MySQLError as e:
    print(f"❌ Error connecting to database: {e}")






