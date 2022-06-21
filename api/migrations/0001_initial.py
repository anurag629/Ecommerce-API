import email
from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="anurag",
                          email="akvermaav629@gmail.com",
                          is_staff=True,
                          is_superuser=True,
                          phone="80520277789",
                          gender="Male")

        user.set_password("12345678")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
