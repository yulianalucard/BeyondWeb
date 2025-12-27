from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Producto, Categoria, bodega_ubicacion


@admin.register(Producto)
class ProductoAdmin(ImportExportModelAdmin):
    list_display = ('nombre_producto', 'categoria', 'valor_unitario', 'stock')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(bodega_ubicacion)
class Bodega_ubicacionAdmin(admin.ModelAdmin):
    pass

