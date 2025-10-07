import pymysql


# Inventory System with MySQL database integration      
class Inventory:
    # Initialize the inventory system and connect to the database
    def __init__(self, host='localhost', user='root', password='', database='inventory_db'):
        self.Connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.create_table()
    
    # Create the prodcuts table if it doesn't exist
    def create_table(self):
        try:
            # Using "with" statement to ensure the connection is properly managed
            with self.Connection as cursor():
                cursor = self.Connection.cursor()                   
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
                self.Connection.commit()
        except pymysql.MySQLError as e:
            print(f"❌ Error creating table: {e}")


    # Create a new item in the inventory
    def create_item(self, item_name, price, quantity):
        # Store item in local dictionary
        with self.Connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)",
                (item_name, price, quantity)
            )
            result = cursor.fetchone()
            if result:
                cursor.execute("" \
                "UPDATE products SET name = %s, price = %s, quantity = %s WHERE id = %s",
                (item_name, price, quantity, result[0])
                )

    # Retrieve an item from the inventory
    def get_item(self, item_name):
        # Fetch item from the database
        with self.Connection.cursor() as cursor:
            cursor.execute("SELECT * FROM products WHERE name = %s", (item_name,))
            item = cursor.fetchone()
            if item:
                print(f"📦 {item_name}: preço = {item[2]}, quantidade = {item[3]}")
            else:
                print(f"❌ Item '{item_name}' não encontrado.")    

    # List all item in the inventory
    def list_items(self):
        # Fetch all items from the database
        with self.Connection.cursor() as cursor:
            cursor.execute("SELECT * FROM products")
            rows = cursor.fetchall()
        if not rows:
            print("📭 Nenhum item no inventário.")      
        else:
            print("🗂️ Itens no inventário:")        
            for row in rows:
                print(f"{row[1]} → Preço: {row[2]}, Quantidade: {row[3]}")
                print(10 * "-----")

    def remove_item(self, item_name, quantity):
        if item_name in self.Products and self.Products[item_name]['quantity'] >= quantity:
            self.Products[item_name]['quantity'] -= quantity
            if self.Products[item_name]['quantity'] == 0:
                del self.Products[item_name]
        
        with self.Connection.cursor() as cursor:        
            cursor.execute("SELECT * FROM products WHERE name = %s", (item_name,))
            resul = cursor.fetchone()
            if resul:
                if resul[0] <= quantity:
                    cursor.execute("DELETE FROM products WHERE name = %s", (item_name,))
                else:
                    cursor.execute("UPDATE products SET quantity = quantity - %s WHERE name = %s",(quantity, item_name))
                self.Connection.commit()        
                print(f"✅ Removido {quantity} de '{item_name}'.")
            else:
                print(f"❌ Item '{item_name}' não encontrado.")

    def close(self):
        self.Connection.close()
    



    

