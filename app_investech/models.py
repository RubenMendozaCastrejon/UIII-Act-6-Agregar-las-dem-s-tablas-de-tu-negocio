from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    pais = models.CharField(max_length=50)
    saldo_disponible = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Portafolio(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="portafolios")
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    valor_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    riesgo = models.CharField(max_length=50, choices=[('bajo', 'Bajo'), ('medio', 'Medio'), ('alto', 'Alto')])
    activos = models.ManyToManyField('Activo', related_name="portafolios")

    def __str__(self):
        return f"{self.nombre} ({self.usuario.nombre})"

class Activo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=[
        ('accion', 'Acción'),
        ('bono', 'Bono'),
        ('cripto', 'Criptomoneda'),
        ('fondo', 'Fondo de inversión'),
        ('otro', 'Otro'),
    ])
    simbolo = models.CharField(max_length=10)
    precio_actual = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    mercado = models.CharField(max_length=100)
    volatilidad = models.DecimalField(max_digits=5, decimal_places=2, help_text="Porcentaje de volatilidad")

    def __str__(self):
        return f"{self.nombre} ({self.simbolo})"
    
class Inversion(models.Model):
    portafolio = models.ForeignKey('Portafolio', on_delete=models.CASCADE, related_name='inversiones')
    activo = models.ForeignKey('Activo', on_delete=models.CASCADE, related_name='inversiones')
    cantidad = models.DecimalField(max_digits=12, decimal_places=4)
    precio_compra = models.DecimalField(max_digits=12, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inversión en {self.activo.nombre} ({self.portafolio.nombre})"
    
    def valor_actual(self):
        return self.cantidad * self.activo.precio_actual
    
    def ganancia_perdida(self):
        return (self.activo.precio_actual - self.precio_compra) * self.cantidad
    
class Transaccion(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='transacciones')
    tipo_transaccion = models.CharField(max_length=50, choices=[
        ('deposito', 'Depósito'),
        ('retiro', 'Retiro'),
        ('compra', 'Compra'),
        ('venta', 'Venta'),
        ('transferencia', 'Transferencia'),
    ])
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)

    def __str__(self):
        return f"{self.tipo_transaccion.capitalize()} - {self.usuario.nombre} (${self.monto})"
    
    @property
    def icono_tipo(self):
        iconos = {
            'deposito': 'fa-arrow-down text-success',
            'retiro': 'fa-arrow-up text-danger',
            'compra': 'fa-shopping-cart text-info',
            'venta': 'fa-money-bill-wave text-warning',
            'transferencia': 'fa-exchange-alt text-primary'
        }
        return iconos.get(self.tipo_transaccion, 'fa-exchange-alt')
    
    @property
    def color_tipo(self):
        colores = {
            'deposito': 'success',
            'retiro': 'danger',
            'compra': 'info',
            'venta': 'warning',
            'transferencia': 'primary'
        }
        return colores.get(self.tipo_transaccion, 'secondary')