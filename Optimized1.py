from typing import List, Dict  # Type hints for clarity and better code documentation
from products import dao  # Importing data access object (DAO) for database interaction


class Product:
    """
    Represents a product with attributes such as ID, name, description, cost, and quantity.
    """

    def _init_(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        """
        Initialize a Product instance.

        Args:
            id (int): Unique identifier for the product.
            name (str): Name of the product.
            description (str): Description of the product.
            cost (float): Cost of the product.
            qty (int): Quantity of the product in stock (default is 0).
        """
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: Dict) -> 'Product':
        """
        Load a Product instance from a dictionary.

        Args:
            data (Dict): Dictionary containing product data.

        Returns:
            Product: A Product instance created from the dictionary.
        """
        # Using .get ensures missing keys won't raise errors, and default values are applied.
        return Product(
            id=data.get('id'),
            name=data.get('name'),
            description=data.get('description'),
            cost=data.get('cost'),
            qty=data.get('qty', 0)  # Default quantity is 0 if not provided
        )


def list_products() -> List[Product]:
    """
    Retrieve and return a list of all products.

    Returns:
        List[Product]: A list of Product instances.
    """
    # Retrieve raw product data from the database using the DAO
    products_data = dao.list_products()

    # Convert raw data dictionaries to Product instances using list comprehension
    return [Product.load(product) for product in products_data]


def get_product(product_id: int) -> Product:
    """
    Retrieve and return a single product by its ID.

    Args:
        product_id (int): The ID of the product to retrieve.

    Returns:
        Product: The retrieved Product instance.
    """
    # Fetch product data by ID and convert it to a Product instance
    product_data = dao.get_product(product_id)
    return Product.load(product_data)


def add_product(product: Dict):
    """
    Add a new product to the database.

    Args:
        product (Dict): A dictionary containing product details.
    """
    # Pass the product data dictionary directly to the DAO for database insertion
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """
    Update the quantity of a product. Raises an error if the quantity is negative.

    Args:
        product_id (int): The ID of the product to update.
        qty (int): The new quantity for the product.

    Raises:
        ValueError: If the provided quantity is negative.
    """
    # Validation to ensure the quantity is not negative
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    
    # Update the product quantity in the database
    dao.update_qty(product_id, qty)