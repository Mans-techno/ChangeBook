from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('changebook', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(model_name='book', name='status'),
        migrations.AddField(model_name='book', name='is_available', field=models.BooleanField(default=True)),
        migrations.AlterUniqueTogether(name='review', unique_together=set()),
        migrations.RenameField(model_name='review', old_name='target', new_name='user'),
        migrations.RemoveField(model_name='review', name='created_at'),
    ]
