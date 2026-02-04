from django.db import models
from decimal import Decimal
from django.utils import timezone
import string
import random
from django.contrib.auth.models import User

class Proveedor(models.Model):
    PAIS_CHOICES = [
        ('DO', 'República Dominicana'),
        ('US', 'Estados Unidos'),
        ('PR', 'Puerto Rico'),
        ('HT', 'Haití'),
        ('JM', 'Jamaica'),
        ('CU', 'Cuba'),
        ('CO', 'Colombia'),
        ('VE', 'Venezuela'),
        ('PA', 'Panamá'),
        ('CR', 'Costa Rica'),
        ('MX', 'México'),
        ('CN', 'China'),
        ('KR', 'Corea del Sur'),
        ('TW', 'Taiwán'),
        ('JP', 'Japón'),
    ]
    
    # CATEGORIA_CHOICES = [
    #     ('smartphones', 'Smartphones'),
    #     ('accesorios', 'Accesorios'),
    #     ('repuestos', 'Repuestos'),
    #     ('tablets', 'Tablets'),
    #     ('smartwatch', 'Smartwatch'),
    #     ('audio', 'Audio y Auriculares'),
    #     ('cargadores', 'Cargadores y Cables'),
    #     ('fundas', 'Fundas y Protectores'),
    # ]
    
    TERMINOS_PAGO_CHOICES = [
        ('contado', 'Contado'),
        ('15-dias', '15 días'),
        ('30-dias', '30 días'),
        ('45-dias', '45 días'),
        ('60-dias', '60 días'),
    ]
    
    nombre_empresa = models.CharField(max_length=100, verbose_name="Nombre de la Empresa")
    rnc = models.CharField(max_length=13, verbose_name="RNC")
    nombre_contacto = models.CharField(max_length=100, verbose_name="Nombre del Contacto")
    email = models.EmailField(verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    whatsapp = models.CharField(max_length=20, blank=True, null=True, verbose_name="WhatsApp")
    pais = models.CharField(max_length=2, choices=PAIS_CHOICES, default='DO', verbose_name="País")
    ciudad = models.CharField(max_length=50, verbose_name="Ciudad")
    # categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, verbose_name="Categoría de Productos")
    direccion = models.TextField(verbose_name="Dirección Completa", blank=True, null=True)
    terminos_pago = models.CharField(max_length=20, choices=TERMINOS_PAGO_CHOICES, blank=True, null=True, verbose_name="Términos de Pago")
    limite_credito = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, verbose_name="Límite de Crédito (RD$)")
    notas = models.TextField(blank=True, null=True, verbose_name="Notas Adicionales")
    activo = models.BooleanField(default=True, verbose_name="Suplidor Activo")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    ultima_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['nombre_empresa']

    def __str__(self):
        return self.nombre_empresa









class EntradaProducto(models.Model):
    MARCAS = (
    ('honda', 'Honda'),
    ('yamaha', 'Yamaha'),
    ('suzuki', 'Suzuki'),
    ('kawasaki', 'Kawasaki'),
    ('tvs', 'TVS'),
    ('hero', 'Hero'),
    ('loncin', 'Loncin'),
    ('kove', 'Kove'),
    ('x1000', 'X1000'),
    ('ktm', 'KTM'),
    ('bajaj', 'Bajaj'),
    ('otros', 'Otros'),
    )
    
    CAPACIDADES = (
        ('16', '16GB'),
        ('32', '32GB'),
        ('64', '64GB'),
        ('128', '128GB'),
        ('256', '256GB'),
        ('512', '512GB'),
        ('1t', '1TB'),
    )
    
    ESTADOS = (
        ('nuevo', 'Nuevo'),
        ('usado', 'Usado'),
        ('reacondicionado', 'Reacondicionado'),
        ('exhibicion', 'Exhibición'),
    )
    
    COLORES = (
        ('negro', 'Negro'),
        ('blanco', 'Blanco'),
        ('azul', 'Azul'),
        ('rojo', 'Rojo'),
        ('dorado', 'Dorado'),
        ('plateado', 'Plateado'),
        ('verde', 'Verde'),
        ('morado', 'Morado'),
        ('rosa', 'Rosa'),
        ('gris', 'Gris'),
        ('otros', 'Otros'),
    )
    
    # Código único para el producto
    codigo_producto = models.CharField(max_length=20, unique=True, editable=False)
    
    # Información de facturación
    numero_factura = models.CharField(max_length=50)
    fecha_entrada = models.DateField(default=timezone.now)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    
    # Información del producto
    nombre_producto = models.CharField(max_length=100)
    marca = models.CharField(max_length=20, choices=MARCAS)
    modelo = models.CharField(max_length=100)
    capacidad = models.CharField(max_length=10, choices=CAPACIDADES, blank=True, null=True)
    imei_serial = models.CharField(max_length=50, unique=True)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    color = models.CharField(max_length=20, choices=COLORES, blank=True, null=True)
    cantidad = models.PositiveIntegerField(default=1)
    cantidad_minima = models.PositiveIntegerField(default=2, verbose_name="Cantidad Mínima")
    
    # Información de costos
    costo_compra = models.DecimalField(max_digits=10, decimal_places=2)
    porcentaje_itbis = models.DecimalField(max_digits=5, decimal_places=2, default=18)
    monto_itbis = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    costo_venta = models.DecimalField(max_digits=10, decimal_places=2)
    margen_ganancia = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # Estado del producto
    activo = models.BooleanField(default=True, verbose_name="Activo")
    
    # Observaciones
    observaciones = models.TextField(blank=True, null=True)
    
    # Auditoría
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    es_producto_base = models.BooleanField(default=False, verbose_name="Es producto base")
    numero_maquina = models.CharField(max_length=50, blank=True, null=True, verbose_name="Número/Máquina")
    
    def save(self, *args, **kwargs):
        # Guardar cantidad anterior para el movimiento de stock
        cantidad_anterior = None
        if self.pk:
            cantidad_anterior = EntradaProducto.objects.get(pk=self.pk).cantidad
        
        # Generar código único si es un nuevo registro
        if not self.codigo_producto:
            # Generar código con formato: PROD-XXXXXX (6 dígitos aleatorios)
            random_digits = ''.join(random.choices(string.digits, k=6))
            self.codigo_producto = f"PROD-{random_digits}"
            
            # Verificar que el código no exista
            while EntradaProducto.objects.filter(codigo_producto=self.codigo_producto).exists():
                random_digits = ''.join(random.choices(string.digits, k=6))
                self.codigo_producto = f"PROD-{random_digits}"
        
        # Calcular montos automáticamente
        self.monto_itbis = (self.costo_compra * self.porcentaje_itbis) / 100
        self.costo_total = self.costo_compra + self.monto_itbis
        
        if self.costo_total > 0:
            self.margen_ganancia = ((self.costo_venta - self.costo_total) / self.costo_total) * 100
        
        super().save(*args, **kwargs)
        
        # Registrar movimiento de stock si la cantidad cambió
        if cantidad_anterior is not None and cantidad_anterior != self.cantidad:
            self.registrar_movimiento_stock(
                tipo_movimiento='ajuste',
                cantidad=abs(cantidad_anterior - self.cantidad),
                cantidad_anterior=cantidad_anterior,
                cantidad_nueva=self.cantidad,
                motivo="Ajuste manual de stock",
                usuario=kwargs.get('usuario')  # Se pasa desde la vista
            )
    
    def tiene_stock_suficiente(self, cantidad_solicitada):
        """Verifica si hay stock suficiente para la cantidad solicitada"""
        return self.cantidad >= cantidad_solicitada and self.activo
    
    def restar_stock(self, cantidad, usuario, motivo="Venta", referencia=None):
        """Resta cantidad del stock y registra el movimiento"""
        if not self.tiene_stock_suficiente(cantidad):
            return False
        
        cantidad_anterior = self.cantidad
        self.cantidad -= cantidad
        self.save(update_fields=['cantidad'])
        
        # Registrar movimiento de stock
        self.registrar_movimiento_stock(
            tipo_movimiento='venta',
            cantidad=cantidad,
            cantidad_anterior=cantidad_anterior,
            cantidad_nueva=self.cantidad,
            motivo=motivo,
            referencia=referencia,
            usuario=usuario
        )
        
        return True
    
    def sumar_stock(self, cantidad, usuario, motivo="Devolución", referencia=None):
        """Suma cantidad al stock y registra el movimiento"""
        cantidad_anterior = self.cantidad
        self.cantidad += cantidad
        self.save(update_fields=['cantidad'])
        
        # Registrar movimiento de stock
        self.registrar_movimiento_stock(
            tipo_movimiento='devolucion',
            cantidad=cantidad,
            cantidad_anterior=cantidad_anterior,
            cantidad_nueva=self.cantidad,
            motivo=motivo,
            referencia=referencia,
            usuario=usuario
        )
        
        return True
    
    def registrar_movimiento_stock(self, tipo_movimiento, cantidad, cantidad_anterior, 
                                  cantidad_nueva, motivo, usuario=None, referencia=None):
        """
        Registra un movimiento de stock para este producto
        Si el modelo MovimientoStock no existe, solo imprime en consola
        """
        try:
            # Intentar importar el modelo MovimientoStock
            from django.apps import apps
            MovimientoStock = apps.get_model('facturacion', 'MovimientoStock')
            
            MovimientoStock.objects.create(
                producto=self,
                tipo_movimiento=tipo_movimiento,
                cantidad=cantidad,
                cantidad_anterior=cantidad_anterior,
                cantidad_nueva=cantidad_nueva,
                motivo=motivo,
                usuario=usuario,
                referencia=referencia
            )
        except (LookupError, ImportError):
            # Si el modelo no existe, solo registrar en consola
            print(f"Movimiento de Stock - {self.nombre_producto}:")
            print(f"  Tipo: {tipo_movimiento}")
            print(f"  Cantidad: {cantidad}")
            print(f"  Anterior: {cantidad_anterior}, Nuevo: {cantidad_nueva}")
            print(f"  Motivo: {motivo}")
            print(f"  Referencia: {referencia}")
            print("-" * 50)
    
    def stock_bajo(self):
        """Verifica si el stock está por debajo del mínimo"""
        return self.cantidad <= self.cantidad_minima
    
    @property
    def estado_stock(self):
        """Devuelve el estado del stock"""
        if self.cantidad == 0:
            return "Agotado"
        elif self.stock_bajo():
            return "Bajo"
        else:
            return "Disponible"
    
    @property
    def clase_estado_stock(self):
        """Devuelve la clase CSS para el estado del stock"""
        if self.cantidad == 0:
            return "danger"
        elif self.stock_bajo():
            return "warning"
        else:
            return "success"
    
    def __str__(self):
        return f"{self.nombre_producto} - {self.codigo_producto}"
    
    class Meta:
        verbose_name = "Entrada de Producto"
        verbose_name_plural = "Entradas de Productos"
        ordering = ['-fecha_registro']



# class EntradaProducto(models.Model):
#     MARCAS = (
#         ('apple', 'Apple'),
#         ('samsung', 'Samsung'),
#         ('xiaomi', 'Xiaomi'),
#         ('huawei', 'Huawei'),
#         ('lg', 'LG'),
#         ('motorola', 'Motorola'),
#         ('nokia', 'Nokia'),
#         ('sony', 'Sony'),
#         ('google', 'Google'),
#         ('oneplus', 'OnePlus'),
#         ('oppo', 'Oppo'),
#         ('vivo', 'Vivo'),
#         ('realme', 'Realme'),
#         ('tecno', 'Tecno'),
#         ('infinix', 'Infinix'),
#         ('alcatel', 'Alcatel'),
#         ('zte', 'ZTE'),
#         ('otros', 'Otros'),
#     )
    
#     CAPACIDADES = (
#         ('16', '16GB'),
#         ('32', '32GB'),
#         ('64', '64GB'),
#         ('128', '128GB'),
#         ('256', '256GB'),
#         ('512', '512GB'),
#         ('1t', '1TB'),
#     )
    
#     ESTADOS = (
#         ('nuevo', 'Nuevo'),
#         ('usado', 'Usado'),
#         ('reacondicionado', 'Reacondicionado'),
#         ('exhibicion', 'Exhibición'),
#     )
    
#     COLORES = (
#         ('negro', 'Negro'),
#         ('blanco', 'Blanco'),
#         ('azul', 'Azul'),
#         ('rojo', 'Rojo'),
#         ('dorado', 'Dorado'),
#         ('plateado', 'Plateado'),
#         ('verde', 'Verde'),
#         ('morado', 'Morado'),
#         ('rosa', 'Rosa'),
#         ('gris', 'Gris'),
#         ('otros', 'Otros'),
#     )
    
#     # Código único para el producto
#     codigo_producto = models.CharField(max_length=20, unique=True, editable=False)
    
#     # Información de facturación
#     numero_factura = models.CharField(max_length=50)
#     fecha_entrada = models.DateField(default=timezone.now)
#     proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
#     ncf = models.CharField(max_length=20, blank=True, null=True)
    
#     # Información del producto
#     nombre_producto = models.CharField(max_length=100)
#     marca = models.CharField(max_length=20, choices=MARCAS)
#     modelo = models.CharField(max_length=100)
#     capacidad = models.CharField(max_length=10, choices=CAPACIDADES, blank=True, null=True)
#     imei_serial = models.CharField(max_length=50, unique=True)
#     estado = models.CharField(max_length=20, choices=ESTADOS)
#     color = models.CharField(max_length=20, choices=COLORES, blank=True, null=True)
#     cantidad = models.PositiveIntegerField(default=1)
    
#     # Información de costos
#     costo_compra = models.DecimalField(max_digits=10, decimal_places=2)
#     porcentaje_itbis = models.DecimalField(max_digits=5, decimal_places=2, default=18)
#     monto_itbis = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     costo_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     costo_venta = models.DecimalField(max_digits=10, decimal_places=2)
#     margen_ganancia = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
#     # Observaciones
#     observaciones = models.TextField(blank=True, null=True)
    
#     # Auditoría
#     fecha_registro = models.DateTimeField(auto_now_add=True)
#     fecha_actualizacion = models.DateTimeField(auto_now=True)
    
#     def save(self, *args, **kwargs):
#         # Generar código único si es un nuevo registro
#         if not self.codigo_producto:
#             # Generar código con formato: PROD-XXXXXX (6 dígitos aleatorios)
#             random_digits = ''.join(random.choices(string.digits, k=6))
#             self.codigo_producto = f"PROD-{random_digits}"
            
#             # Verificar que el código no exista
#             while EntradaProducto.objects.filter(codigo_producto=self.codigo_producto).exists():
#                 random_digits = ''.join(random.choices(string.digits, k=6))
#                 self.codigo_producto = f"PROD-{random_digits}"
        
#         # Calcular montos automáticamente
#         self.monto_itbis = (self.costo_compra * self.porcentaje_itbis) / 100
#         self.costo_total = self.costo_compra + self.monto_itbis
        
#         if self.costo_total > 0:
#             self.margen_ganancia = ((self.costo_venta - self.costo_total) / self.costo_total) * 100
        
#         super().save(*args, **kwargs)
    
#     def __str__(self):
#         return f"{self.nombre_producto} - {self.codigo_producto}"
    
#     class Meta:
#         verbose_name = "Entrada de Producto"
#         verbose_name_plural = "Entradas de Productos"





class Cliente(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Nombre Completo")
    identification_number = models.CharField(max_length=20, unique=True, verbose_name="Cédula/RIF")
    primary_phone = models.CharField(max_length=15, blank=True, verbose_name="Teléfono Principal")
    secondary_phone = models.CharField(max_length=15, blank=True, verbose_name="Teléfono Secundario")
    address = models.TextField(blank=True, verbose_name="Dirección")
    email = models.EmailField(blank=True, verbose_name="Correo Electrónico")
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Límite de Crédito")
    status = models.BooleanField(default=True, verbose_name="Estado Activo")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    
    class Meta:
        db_table = 'clientes'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return f"{self.full_name} - {self.identification_number}"
    



class Venta(models.Model):
    METODOS_PAGO = (
        ('contado', 'Contado'),
        ('credito', 'Crédito'),
    )
    
    FORMAS_PAGO = (
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia'),
    )
    
    # Información de la venta

    

    numero_factura = models.CharField(max_length=20, unique=True)
    fecha_venta = models.DateTimeField(default=timezone.now)
    vendedor = models.ForeignKey(User, on_delete=models.PROTECT)
    
    # Información del cliente
    cliente = models.ForeignKey('Cliente', on_delete=models.PROTECT, null=True, blank=True)
    cliente_nombre = models.CharField(max_length=100)
    cliente_documento = models.CharField(max_length=20)
    
    # Información de pago
    tipo_venta = models.CharField(max_length=10, choices=METODOS_PAGO)
    metodo_pago = models.CharField(max_length=15, choices=FORMAS_PAGO)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)
    descuento_porcentaje = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    descuento_monto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    montoinicial = models.DecimalField(max_digits=12, decimal_places=2)
    es_financiada = models.BooleanField(default=False)
    tasa_interes = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    plazo_meses = models.PositiveIntegerField(default=1)
    monto_financiado = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    interes_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    interes_mensual = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    cuota_mensual = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_con_interes = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_a_pagar = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    plazo_meses = models.IntegerField(default=1, verbose_name="Plazo en meses")
    
    # Para pagos en efectivo
    efectivo_recibido = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    cambio = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    # Estado
    completada = models.BooleanField(default=False)
    anulada = models.BooleanField(default=False)
    
    # Auditoría
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    anulada = models.BooleanField(default=False)
    motivo_anulacion = models.TextField(blank=True, null=True)
    fecha_anulacion = models.DateTimeField(blank=True, null=True)
    usuario_anulacion = models.ForeignKey(User, on_delete=models.PROTECT, 
                                         related_name='ventas_anuladas', 
                                         blank=True, null=True)

    
    
    def save(self, *args, **kwargs):
        if not self.numero_factura:
            # Generar número de factura único
            año = timezone.now().year
            ultima_venta = Venta.objects.filter(fecha_venta__year=año).order_by('-id').first()
            if ultima_venta and ultima_venta.numero_factura:
                try:
                    ultimo_numero = int(ultima_venta.numero_factura.split('-')[-1])
                    nuevo_numero = ultimo_numero + 1
                except (ValueError, IndexError):
                    nuevo_numero = 1
            else:
                nuevo_numero = 1
            self.numero_factura = f"F-{año}-{nuevo_numero:06d}"
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.numero_factura} - {self.cliente_nombre} - RD${self.total}"
    
    class Meta:
        db_table = 'ventas'  # Nombre explícito para la tabla
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ['-fecha_venta']


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey('EntradaProducto', on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.producto.nombre_producto} x {self.cantidad}"
    
    class Meta:
        db_table = 'detalles_venta'  # Nombre explícito para la tabla
        verbose_name = "Detalle de Venta"
        verbose_name_plural = "Detalles de Venta"

# En tu models.py, modifica la clase CuentaPorCobrar
class CuentaPorCobrar(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('vencida', 'Vencida'),
        ('pagada', 'Pagada'),
        ('parcial', 'Pago Parcial'),
        ('anulada', 'Anulada'),
    )

    venta = models.OneToOneField('Venta', on_delete=models.CASCADE, related_name='cuenta_por_cobrar')
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='cuentas_por_cobrar')
    monto_total = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Monto Total Original")
    monto_total_con_interes = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Monto Total con Interés", default=0)
    monto_pagado = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Monto Pagado")
    fecha_vencimiento = models.DateField(verbose_name="Fecha de Vencimiento")
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente')
    productos = models.TextField(verbose_name="Productos de la Venta", blank=True)
    observaciones = models.TextField(blank=True, verbose_name="Observaciones")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    anulada = models.BooleanField(default=False)
    fecha_anulacion = models.DateTimeField(null=True, blank=True)
    eliminada = models.BooleanField(default=False)
    fecha_eliminacion = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'cuentas_por_cobrar'
        verbose_name = 'Cuenta por Cobrar'
        verbose_name_plural = 'Cuentas por Cobrar'
        ordering = ['-fecha_creacion']
    
    def save(self, *args, **kwargs):
        if self.venta and hasattr(self.venta, 'total_con_interes'):
            self.monto_total_con_interes = self.venta.total_con_interes
        elif not self.monto_total_con_interes:
            self.monto_total_con_interes = self.monto_total
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Cuenta #{self.id} - {self.cliente.full_name} - {self.venta.numero_factura}"
    
    @property
    def saldo_pendiente(self):
        """Calcula el monto total pendiente de pago"""
        if self.anulada or self.eliminada:
            return Decimal('0.00')
        return self.monto_total - self.monto_pagado
    
    @property
    def esta_vencida(self):
        if self.anulada or self.eliminada:
            return False
        return timezone.now().date() > self.fecha_vencimiento and self.estado != 'pagada'
    
    def anular_cuenta(self):
        """Método para anular la cuenta"""
        self.anulada = True
        self.estado = 'anulada'
        self.fecha_anulacion = timezone.now()
        self.save()
    
    def eliminar_cuenta(self):
        """Método para eliminar (soft delete) la cuenta"""
        self.eliminada = True
        self.fecha_eliminacion = timezone.now()
        self.save()

    def rebajar_deuda(self, monto_rebaja, observaciones=""):
        """
        Método para rebajar (reducir) el MONTO TOTAL PENDIENTE de una cuenta
        
        La rebaja se aplica reduciendo el monto_total, lo que automáticamente
        reduce el saldo pendiente (monto_total - monto_pagado)
        """
        if self.anulada or self.eliminada:
            raise ValueError("No se puede rebajar una cuenta anulada o eliminada")
        
        if monto_rebaja <= 0:
            raise ValueError("El monto de rebaja debe ser mayor a 0")
        
        # Calcular el monto total pendiente actual
        monto_pendiente_actual = self.monto_total - self.monto_pagado
        
        # Verificar que no se rebaje más de lo pendiente
        if monto_rebaja > monto_pendiente_actual:
            raise ValueError(f"No se puede rebajar más del saldo pendiente: RD$ {monto_pendiente_actual}")
        
        # Guardar el monto total original antes de la rebaja
        monto_total_anterior = self.monto_total
        
        # Calcular el nuevo monto total después de la rebaja
        # La rebaja reduce el monto total, manteniendo el monto_pagado igual
        nuevo_monto_total = self.monto_total - monto_rebaja
        
        # Asegurarse de que el nuevo monto total no sea menor que el monto pagado
        if nuevo_monto_total < self.monto_pagado:
            # Si ocurre esto, ajustamos el monto_pagado al nuevo monto_total
            self.monto_pagado = nuevo_monto_total
        
        # Actualizar el monto total
        self.monto_total = nuevo_monto_total
        
        # Recalcular el estado basado en el nuevo saldo pendiente
        nuevo_saldo_pendiente = self.monto_total - self.monto_pagado
        
        if nuevo_saldo_pendiente <= 0:
            self.estado = 'pagada'
            # Ajustar para que no haya saldo pendiente negativo
            self.monto_pagado = self.monto_total
        elif self.monto_pagado > 0:
            self.estado = 'parcial'
        else:
            self.estado = 'pendiente'
        
        # Guardar los cambios en la cuenta
        self.save()
        
        # Crear un registro de la rebaja
        rebaja = RebajaDeuda(
            cuenta=self,
            monto_rebaja=monto_rebaja,
            monto_anterior=monto_total_anterior,
            monto_nuevo=nuevo_monto_total,
            observaciones=observaciones,
            usuario=User.objects.first()  # En producción usarías request.user
        )
        rebaja.save()
        
        return rebaja


class RebajaDeuda(models.Model):
    cuenta = models.ForeignKey('CuentaPorCobrar', on_delete=models.CASCADE, related_name='rebajas')
    monto_rebaja = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Monto Rebajado")
    monto_anterior = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Monto Total Anterior")
    monto_nuevo = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Monto Total Nuevo")
    observaciones = models.TextField(blank=True, verbose_name="Observaciones de la Rebaja")
    fecha_rebaja = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        db_table = 'rebajas_deuda'
        verbose_name = 'Rebaja de Deuda'
        verbose_name_plural = 'Rebajas de Deuda'
        ordering = ['-fecha_rebaja']
    
    def __str__(self):
        return f"Rebaja #{self.id} - Cuenta #{self.cuenta.id} - RD${self.monto_rebaja}"
class PagoCuentaPorCobrar(models.Model):
    METODOS_PAGO = (
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia'),
    )
    
    cuenta = models.ForeignKey('CuentaPorCobrar', on_delete=models.CASCADE, related_name='pagos')
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto del Pago")
    metodo_pago = models.CharField(max_length=15, choices=METODOS_PAGO, verbose_name="Método de Pago")
    referencia = models.CharField(max_length=50, blank=True, verbose_name="Referencia/Número de Transacción")
    fecha_pago = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Pago")
    observaciones = models.TextField(blank=True, verbose_name="Observaciones")
    fecha_registro = models.DateTimeField(auto_now_add=True)
    anulado = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'pagos_cuentas_por_cobrar'
        verbose_name = 'Pago de Cuenta por Cobrar'
        verbose_name_plural = 'Pagos de Cuentas por Cobrar'
        ordering = ['-fecha_pago']
    
    def __str__(self):
        return f"Pago #{self.id} - {self.cuenta} - RD${self.monto}"


class ComprobantePago(models.Model):
    TIPOS_COMPROBANTE = (
        ('recibo', 'Recibo'),
        ('factura', 'Factura'),
        ('comprobante', 'Comprobante'),
    )
    
    pago = models.OneToOneField('PagoCuentaPorCobrar', on_delete=models.CASCADE, related_name='comprobante')
    cuenta = models.ForeignKey('CuentaPorCobrar', on_delete=models.CASCADE, related_name='comprobantes')
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='comprobantes_pago')
    numero_comprobante = models.CharField(max_length=20, unique=True, verbose_name="Número de Comprobante")
    tipo_comprobante = models.CharField(max_length=15, choices=TIPOS_COMPROBANTE, default='recibo')
    fecha_emision = models.DateTimeField(default=timezone.now)
    contenido = models.TextField(blank=True, verbose_name="Contenido del Comprobante")
    
    class Meta:
        db_table = 'comprobantes_pago'
        verbose_name = 'Comprobante de Pago'
        verbose_name_plural = 'Comprobantes de Pago'
        ordering = ['-fecha_emision']
    
    def save(self, *args, **kwargs):
        if not self.numero_comprobante:
            # Generar número de comprobante automáticamente
            last_comprobante = ComprobantePago.objects.order_by('-id').first()
            last_number = int(last_comprobante.numero_comprobante.split('-')[-1]) if last_comprobante else 0
            self.numero_comprobante = f"COMP-{last_number + 1:06d}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Comprobante {self.numero_comprobante} - {self.cliente.full_name}"



# Modelo para control de caja
class Caja(models.Model):
    ESTADO_CHOICES = (
        ('abierta', 'Abierta'),
        ('cerrada', 'Cerrada'),
    )
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_apertura = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField(null=True, blank=True)
    monto_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    monto_final = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='abierta')
    observaciones = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'caja'
        verbose_name = 'Caja'
        verbose_name_plural = 'Cajas'
    
    def __str__(self):
        return f"Caja {self.id} - {self.usuario.username} - {self.fecha_apertura.strftime('%Y-%m-%d')}"







class MovimientoStock(models.Model):
    TIPOS_MOVIMIENTO = (
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
        ('ajuste', 'Ajuste'),
        ('venta', 'Venta'),
        ('devolucion', 'Devolución'),
    )
    
    producto = models.ForeignKey(EntradaProducto, on_delete=models.CASCADE, related_name='movimientos')
    fecha_movimiento = models.DateTimeField(auto_now_add=True)
    tipo_movimiento = models.CharField(max_length=20, choices=TIPOS_MOVIMIENTO)
    cantidad = models.IntegerField()
    cantidad_anterior = models.IntegerField()
    cantidad_nueva = models.IntegerField()
    motivo = models.CharField(max_length=200)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    referencia = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        db_table = 'movimientos_stock'
        ordering = ['-fecha_movimiento']
    
    def __str__(self):
        return f"{self.producto} - {self.tipo_movimiento} - {self.cantidad}"
    


    # Añade este modelo a tu models.py
class CierreCaja(models.Model):
    caja = models.ForeignKey(Caja, on_delete=models.CASCADE)
    monto_efectivo_real = models.DecimalField(max_digits=10, decimal_places=2)
    monto_tarjeta_real = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_esperado = models.DecimalField(max_digits=10, decimal_places=2)
    diferencia = models.DecimalField(max_digits=10, decimal_places=2)
    observaciones = models.TextField(blank=True, null=True)
    fecha_cierre = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'cierre_caja'
        verbose_name = 'Cierre de Caja'
        verbose_name_plural = 'Cierres de Caja'
    
    def __str__(self):
        return f"Cierre {self.id} - {self.caja.usuario.username} - {self.fecha_cierre.strftime('%Y-%m-%d')}"
    









class Devolucion(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.PROTECT)
    producto = models.ForeignKey(EntradaProducto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    motivo = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True, null=True)
    fecha_devolucion = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"Devolución #{self.id} - {self.venta.numero_factura}"





class ComprobantePago(models.Model):
    TIPOS_COMPROBANTE = (
        ('recibo', 'Recibo de Pago'),
        ('comprobante', 'Comprobante de Pago'),
        ('descuento', 'Comprobante de Descuento'),  # NUEVA OPCIÓN
    )
    
    numero_comprobante = models.CharField(max_length=20, unique=True, verbose_name="Número de Comprobante")
    pago = models.OneToOneField('PagoCuentaPorCobrar', on_delete=models.CASCADE, related_name='comprobante')
    cuenta = models.ForeignKey('CuentaPorCobrar', on_delete=models.CASCADE, related_name='comprobantes')
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='comprobantes_pago')
    tipo_comprobante = models.CharField(max_length=15, choices=TIPOS_COMPROBANTE, default='recibo')
    fecha_emision = models.DateTimeField(default=timezone.now)
    anulado = models.BooleanField(default=False)
    fecha_anulacion = models.DateTimeField(null=True, blank=True)
    motivo_anulacion = models.TextField(null=True, blank=True)
    usuario_anulacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='comprobantes_anulados')
    
    class Meta:
        db_table = 'comprobantes_pago'
        verbose_name = 'Comprobante de Pago'
        verbose_name_plural = 'Comprobantes de Pago'
        ordering = ['-fecha_emision']
    
    def save(self, *args, **kwargs):
        if not self.numero_comprobante:
            # Generar número de comprobante único
            año = timezone.now().year
            ultimo_comprobante = ComprobantePago.objects.filter(fecha_emision__year=año).order_by('-id').first()
            if ultimo_comprobante and ultimo_comprobante.numero_comprobante:
                try:
                    ultimo_numero = int(ultimo_comprobante.numero_comprobante.split('-')[-1])
                    nuevo_numero = ultimo_numero + 1
                except (ValueError, IndexError):
                    nuevo_numero = 1
            else:
                nuevo_numero = 1
            self.numero_comprobante = f"CP-{año}-{nuevo_numero:06d}"
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Comprobante {self.numero_comprobante} - {self.cliente.full_name} - RD${self.pago.monto}"
    




