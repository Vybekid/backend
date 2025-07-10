class UIElement: 
    def __init__(self, name, x, y):
        self.name = name 
        self.x = x
        self.y = y 
        print(f"'{self.name}' created at (X={self.x}, Y={self.y})")

    def move_to(self, new_x, new_y): 

        self.x + new_x 
        self.y = new_y 
        print(f" -> Moved '{self.name}' to (X={self.x}, Y={self.y})")

flower_large_image = UIElement("flower image", x=25, y=479)
lady_picture = UIElement("Lady Picture", x=260, y=401)

print("\n Starting move operation")

flower_large_image.move_to(new_x=67, new_y=383)

lady_picture.move_to(new_x=300, new_y=129)


