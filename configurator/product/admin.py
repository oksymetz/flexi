from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'material_components', 'thickness')


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('id', 'material_id', 'width', 'height', 'length')


@admin.register(Instruction)
class InstructionAdmin(admin.ModelAdmin):
    list_display = ('id', 'steps')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'instruction_id')


@admin.register(ProductComponent)
class ProductComponentAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'component_id', 'quantity')

@admin.register(Draft)
class DraftAdmin(admin.ModelAdmin):
    list_display = ('id', 'body_height', 'stand_height', "sitting_height", "width", "length", "material_id", "product_id", "user_id")

