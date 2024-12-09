from django.db import models

# Create your models here.
class Material(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    material_components = models.TextField()                           # Material components (long text)
    thickness = models.FloatField()                                    # Thickness as a float

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
