from django.contrib import admin
from .models import Usuario, Portafolio, Activo, Inversion, Transaccion

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'pais', 'saldo_disponible', 'fecha_registro')
    list_filter = ('pais', 'fecha_registro')
    search_fields = ('nombre', 'apellido', 'email')

@admin.register(Portafolio)
class PortafolioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'usuario', 'valor_total', 'riesgo', 'fecha_creacion')
    list_filter = ('riesgo', 'fecha_creacion')

@admin.register(Activo)
class ActivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'simbolo', 'tipo', 'precio_actual', 'mercado', 'volatilidad')
    list_filter = ('tipo', 'mercado')
    search_fields = ('nombre', 'simbolo')

@admin.register(Inversion)
class InversionAdmin(admin.ModelAdmin):
    list_display = ('portafolio', 'activo', 'cantidad', 'precio_compra', 'inversion_inicial', 'valor_actual', 'ganancia_perdida')
    list_filter = ('portafolio', 'activo', 'fecha')
    search_fields = ('portafolio__nombre', 'activo__nombre')
    
    def inversion_inicial(self, obj):
        return f"${obj.inversion_inicial:.2f}"
    inversion_inicial.admin_order_field = 'precio_compra'  # ← CORREGIDO: era 'inversion_inversal'
    
    def valor_actual(self, obj):
        return f"${obj.valor_actual:.2f}"
    
    def ganancia_perdida(self, obj):
        return f"${obj.ganancia_perdida:.2f}"
    
@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo_transaccion', 'monto', 'cantidad', 'fecha')
    list_filter = ('tipo_transaccion', 'fecha')
    search_fields = ('usuario__nombre', 'usuario__apellido')
    date_hierarchy = 'fecha'