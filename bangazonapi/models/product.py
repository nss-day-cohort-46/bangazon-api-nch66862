from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE
from .customer import Customer
from .productcategory import ProductCategory
from .orderproduct import OrderProduct
from .productrating import ProductRating
from .validators import validate_price

class Product(SafeDeleteModel):

    _safedelete_policy = SOFT_DELETE
    name = models.CharField(max_length=50,)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, related_name='products')
    price = models.FloatField(validators=[validate_price],)
    description = models.CharField(max_length=255,)
    quantity = models.IntegerField(validators=[MinValueValidator(0)],)
    created_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING, related_name='products')
    location = models.CharField(max_length=50,)
    image_path = models.ImageField(
        upload_to='products', height_field=None,
        width_field=None, max_length=None, null=True)
    liked = models.ManyToManyField(Customer, related_name="CustomerLikes")

    @property
    def number_sold(self):
        """number_sold property of a product

        Returns:
            int -- Number items on completed orders
        """
        sold = OrderProduct.objects.filter(product=self, order__payment_type__isnull=False).count()
        return sold

    @property
    def can_be_rated(self):
        """can_be_rated property, which will be calculated per user

        Returns:
            boolean -- If the user can rate the product or not
        """
        return self.__can_be_rated

    @can_be_rated.setter
    def can_be_rated(self, value):
        self.__can_be_rated = value

    @property
    def average_rating(self):
        """Average rating calculated attribute for each product

        Returns:
            number -- The average rating for the product
        """
        ratings = ProductRating.objects.filter(product=self)
        total_rating = 0
        try:
            for rating in ratings:
                total_rating += rating.rating
            avg = total_rating / len(ratings)
            return avg
        except ZeroDivisionError:
            return "No Ratings"

    @property
    def is_liked(self):
        return self.__is_liked

    @is_liked.setter
    def is_liked(self, value):
        self.__is_liked = value

    class Meta:
        verbose_name = ("product")
        verbose_name_plural = ("products")
