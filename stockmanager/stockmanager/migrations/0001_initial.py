# Generated by Django 5.0 on 2023-12-22 22:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('ClienteID', models.AutoField(primary_key=True, serialize=False)),
                ('Imagen', models.CharField(max_length=255)),
                ('Nombre', models.CharField(max_length=255)),
                ('Apellido', models.CharField(max_length=255)),
                ('CorreoElectronico', models.CharField(max_length=255)),
                ('Direccion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('CompraID', models.AutoField(primary_key=True, serialize=False)),
                ('FechaCompra', models.DateTimeField()),
                ('Total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('ProductoID', models.AutoField(primary_key=True, serialize=False)),
                ('Imagen', models.CharField(max_length=255)),
                ('Nombre', models.CharField(max_length=255)),
                ('Descripcion', models.TextField()),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('ProveedorID', models.AutoField(primary_key=True, serialize=False)),
                ('Imagen', models.CharField(max_length=255)),
                ('Nombre', models.CharField(max_length=255)),
                ('Contacto', models.CharField(max_length=255)),
                ('CorreoElectronico', models.CharField(max_length=255)),
                ('Telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DetallesCompras',
            fields=[
                ('DetalleCompraID', models.AutoField(primary_key=True, serialize=False)),
                ('Cantidad', models.IntegerField()),
                ('PrecioUnitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('CompraID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockmanager.compras')),
                ('ProductoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockmanager.productos')),
            ],
        ),
        migrations.AddField(
            model_name='compras',
            name='ProveedorID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockmanager.proveedores'),
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('VentaID', models.AutoField(primary_key=True, serialize=False)),
                ('FechaVenta', models.DateTimeField()),
                ('Total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ClienteID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockmanager.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='DetallesVentas',
            fields=[
                ('DetalleVentaID', models.AutoField(primary_key=True, serialize=False)),
                ('Cantidad', models.IntegerField()),
                ('PrecioUnitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ProductoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockmanager.productos')),
                ('VentaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockmanager.ventas')),
            ],
        ),
    ]
