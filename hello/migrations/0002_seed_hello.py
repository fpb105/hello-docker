from django.db import migrations


def seed(apps, schema_editor):
    Message = apps.get_model("hello", "Message")
    Message.objects.get_or_create(text="hello world")


def unseed(apps, schema_editor):
    Message = apps.get_model("hello", "Message")
    Message.objects.filter(text="hello world").delete()


class Migration(migrations.Migration):
    dependencies = [("hello", "0001_initial")]
    operations = [migrations.RunPython(seed, unseed)]