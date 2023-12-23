# Generated by Django 4.2.7 on 2023-12-06 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0002_alter_certificate_document_scan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.supplier', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='contractmedicine',
            name='medicine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.medicine', verbose_name='Препарат'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='facility',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.medicalfacility', verbose_name='Учреждение'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.medicinegroup', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='legal_entity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.legalentity', verbose_name='Юридическое лицо'),
        ),
        migrations.AlterField(
            model_name='order',
            name='physical_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.physicalperson', verbose_name='Физическое лицо'),
        ),
        migrations.AlterField(
            model_name='order',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Продавец'),
        ),
        migrations.AlterField(
            model_name='ordercomposition',
            name='medicine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.medicine', verbose_name='Препарат'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.contract', verbose_name='Договор'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.supplier', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='receiptitem',
            name='medicine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.medicine', verbose_name='Препарат'),
        ),
    ]
