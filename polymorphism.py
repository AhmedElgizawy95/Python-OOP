class Animal:
    def producesound(self):
        pass

class Dog(Animal):
    def producesound(self):
        return "Woof!"
    


class Cat(Animal):
    def producesound(self):
        return "Meow!"




if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    print(f"Dog says: {dog.producesound()}")
    print(f"Cat says: {cat.producesound()}")