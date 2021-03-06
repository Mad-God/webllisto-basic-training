# Generated by Django 3.1.4 on 2022-04-27 12:54

from django.db import migrations


class Migration(migrations.Migration):

    def mig_ops(self, schema_editor):
        Product = self.get_model("user", 'Post')
        for p in Product.objects.all():
            p.title = p.title.capitalize()
            p.save()
            
    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        # we perform the RunPython() operation that takes 2 parameters:
        # first is a function that defines what to do when this migration is performed
        # second is a function that defines what to do when this migration is reversed,
        # i.e, if a previous migrations file is migrated

        # the RunPython.noop specifies that nothing is to be done in the migration
        migrations.RunPython(mig_ops, migrations.RunPython.noop)
    ]
