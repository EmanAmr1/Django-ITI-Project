# Generated by Django 4.2.9 on 2024-02-04 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("category", "0002_alter_category_image"),
        ("product", "0002_alter_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="category.category",
            ),
        ),
    ]