from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

def validate_range(value):
    if value < 0 or value > 200:
        raise ValidationError(f"Value must be between 0 and 200. Given: {value}")


# Create your models here.
class Material(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    material_components = models.TextField()                           # Material components (long text)
    thickness = models.FloatField(default=1.0)                                    # Thickness as a float

    def __str__(self):
        return self.name


class Component(models.Model):
    id = models.AutoField(primary_key=True)
    material_id = models.ForeignKey(
        Material,
        on_delete=models.CASCADE                              # Cascade delete related records
    )
    width = models.FloatField()
    height = models.FloatField()
    length = models.FloatField()

    def __str__(self):
        return f"Component {self.id} (Material: {self.material_id})"


class Instruction(models.Model):
    id = models.AutoField(primary_key=True)
    steps = models.TextField()

    def __str__(self):
        return f"Instruction {self.id}"


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    instruction_id = models.ForeignKey(
        Instruction,
        on_delete=models.SET_NULL,                        # Allows null if instruction is deleted
        null=True,                                         # Enables null values
        related_name='products_with_instruction'          # Optional: for reverse query
    )

    def __str__(self):
        return self.name


class ProductComponent(models.Model):
    product_id = models.ForeignKey(                      # Foreign Key to Product
        Product,                                    # Replace with the actual Product model name
        on_delete=models.CASCADE                      # Cascade delete
    )
    component_id = models.ForeignKey(                   # Foreign Key to Component
        Component,                                 # Replace with the actual Component model name
        on_delete=models.CASCADE                     # Cascade delete
    )
    quantity = models.PositiveIntegerField()         # Quantity as a positive integer

    def __str__(self):
        return f"{self.quantity} of Component {self.component_id} for Product {self.product_id}"


class Draft(models.Model):
    id = models.AutoField(primary_key=True)  # PK
    body_height = models.FloatField(null=True)             # Body height
    stand_height = models.FloatField()            # Stand height
    sitting_height = models.FloatField()
    width = models.FloatField()                   # Width
    length = models.FloatField()                  # Length
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE
    )                                             # FK to Material
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )                                             # FK to Product
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Draft {self.id}"

class Box(models.Model):
    id = models.AutoField(primary_key=True)
    box_height = models.FloatField(validators=[validate_range])
    box_length = models.FloatField(validators=[validate_range])
    box_depth =  models.FloatField(validators=[validate_range])

    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE
    )  # FK to Material
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )  # FK to Product
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Box {self.id}"


