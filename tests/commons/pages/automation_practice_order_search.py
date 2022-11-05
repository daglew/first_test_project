class Xpath:
    ADD_TO_CART_BUTTON = "//span[.='Add to cart']"
    PICTURE = "//img[@alt='Faded Short Sleeve T-shirts']"
    PROCEED_TO_CHECKOUT = "//a[@title='Proceed to checkout']/span"
    SEARCH_BUTTON = "//button[@name='submit_search']"


class Ids:
    INPUT_SEARCH = "search_query_top"


def picture_with_text(picture_text):
    return f"//div[@class='product-image-container']//img[@alt='{picture_text}']"
