import sqlite3

db_name = 'site_db'
conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
 
def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def create():
    open()

    do('''
        CREATE TABLE if not exists item (
        id INTEGER PRIMARY KEY,
        title VARCHAR,
        category VARCHAR,
        description VARCHAR,
        imgUrl VARCHAR
       )''')
    
    close()

def drop_table(table):
    open()
    do(f'DROP TABLE IF EXISTS {table}')

    create()

def add_item(title, description, imgUrl):
    open()
    cursor.execute('''INSERT INTO item (title, description, imgUrl) VALUES (?,?,?)''', [title, description, imgUrl])
    conn.commit()
    close()

def show(table):
    open()
    cursor.execute(f'SELECT * FROM {table}')
    print(cursor.fetchall())
    close()

def get_all_items():
    open()
    cursor.execute(f'SELECT * FROM item')
    return cursor.fetchall()

def get_items_by_id(id):
    open()
    cursor.execute(f'SELECT * FROM item WHERE item.id == ?', [id])
    return cursor.fetchall()

drop_table('item')
create()
add_item("Crazy bee",
         "A mix of jelly candies with fillings made with the addition of juices: cherry, orange, lemon, lime, pink grapefruit, red berries, strawberry. Bright, juicy jelly candy.The candy contains natural juices in its composition.",
        "https://roshenstores.com/Media/images/catalog/medium/1ee1f74e7309575f5b5e1c7180c431c2.png")
add_item("Peppinez candy",
         "Candy in the shape of a ball with a filling of cherry, apple, and blueberry flavors. This candy is the most sour in the assortment of candies.",
         "https://roshenstores.com/Media/images/catalog/big/36b783ff052b2bd1d41f5d19c106239c.png")
add_item("Bim Bom",
         "Transparent caramel in the form of a ball with a filling: pear, strawberry, pineapple and tutti-frutti.",
         "https://roshenstores.com/Media/images/catalog/big/b489ca0ced7b081e57a9ba835072abce.png")
add_item("Barberry",
         "Barberry-flavored candy drops. Candies are produced using a long-standing traditional technique.",
         "https://roshenstores.com/Media/images/catalog/big/c973ea4ce2db34470d61d4137f16bb50.png")
add_item("Eucalyptus-menthol",
         "Peppermint candy with natural menthol, eucalyptus oil, and a mint flavor.",
         "https://roshenstores.com/Media/images/catalog/big/87dec2ff69ecf0f3eea7b1029bac437c.png")
add_item("Jelly",
         "A mix of jelly candies based on pectin in fine crystallized sugar with flavors: pear, apple, orange, lemon, strawberry, and raspberry. Soft in texture, making it perfect for children. Contains natural fruit and berry juices.",
         "https://roshenstores.com/Media/images/catalog/big/f541c8334c5caf666001aab92b571909.png")
add_item("Candy Nut",
         "Soft caramel with peanuts, covered in a delicate glaze. If you place the candy in a cool place, the soft caramel will turn into a harder texture, typical of nougat.",
         "https://roshenstores.com/Media/images/catalog/big/816472364139ce8907cc1dd74385c046.png")
add_item("MontBlanc",
         "Tandem of milk chocolate with a delicate filling of coconut cream and almond.",
         "https://roshenstores.com/Media/images/catalog/big/625296d7447224117b3d641cfebcde97.png")
add_item("Granola",
         "Hello! Granola is a combination of rich dark chocolate coating and crunchy multigrain flakes. A delicious snack that provides an energy boost!",
         "https://roshenstores.com/Media/images/catalog/big/7e6bcadb87095350ebbc0b6f206e5f17.png")
add_item("Sour Belts",
         "Mixed jelly candies. Candies that are particularly popular among children: chewy candies based on gelatin. The candies themselves are bright and interesting. Only natural juice-based dyes are used. The candies do NOT stick together in the package thanks to the use of a powder produced in Germany, which has no analogues in Ukraine. The candy shell is coated with beeswax glaze, which allows the candy to maintain its necessary shape and shine",
         "https://roshenstores.com/Media/images/catalog/big/36c5bba50d5355b04836f4cf84c4e36e.png")
add_item("Banana Land",
         "Jelly candies made from foamed mass and banana-flavored jelly. Sweets that are particularly popular among children: chewy candies made from gelatin. The candies themselves are bright and interesting. The dyes used are exclusively based on natural juices. The candies DO NOT stick together in the package due to the use of powder produced in Germany, which has no analogues in Ukraine. The candy shell is coated with beeswax glaze, which allows the candy to maintain its necessary shape and shine.",
         "https://roshenstores.com/Media/images/catalog/big/ef26018a9e6e0eaa33fd44a9fe97de03.png")
add_item("Bonny-fruit",
         "Jelly candies based on pectin are made up of 25% juice. The mix includes candies with flavors and shapes: orange, grapefruit, lemon-lime. Each piece is coated with fine sugar crystals, giving the candy a sparkle.",
         "https://roshenstores.com/Media/images/catalog/big/ba2dd68cf24eb7d2f81003cd27d23c64.png")
add_item("",
         "",
         "")
add_item("",
         "",
         "")
add_item("",
         "",
         "")








show('item')
