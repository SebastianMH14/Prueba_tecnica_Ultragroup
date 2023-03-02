# Generated by Django 4.1.7 on 2023-03-02 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_booking', '0002_passenger_emerygencycontact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='Document_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='Document_type',
            field=models.CharField(choices=[('CC', 'Cedula de ciudadania'), ('CE', 'Cedula de extranjeria'), ('TI', 'Tarjeta de identidad'), ('PA', 'Pasaporte')], max_length=100),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_booking.hotel')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_booking.passenger')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_booking.room')),
            ],
        ),
    ]
