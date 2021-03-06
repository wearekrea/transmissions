# Generated by Django 3.1 on 2022-01-20 21:07

from django.db import migrations, models, OperationalError
import django.db.models.deletion


def set_applications(apps, schema_editor):
    Notification = apps.get_model("transmissions", "Notification")
    notifications_without_content_id = Notification.objects.filter(
        content_id__isnull=True
    )
    if notifications_without_content_id.exists():
        raise OperationalError(
            "Can't migrate since there are `Notification.content_id`s being null. Their pks are {}".format(
                ", ".join([n.pk for n in notifications_without_content_id])
            )
        )
    notifications_without_content_type = Notification.objects.filter(
        content_type__isnull=True
    )
    if notifications_without_content_type.exists():
        raise OperationalError(
            "Can't migrate since there are `Notification.content_type`s being null. Their pks are {}".format(
                ", ".join([n.pk for n in notifications_without_content_type])
            )
        )
    for notification in Notification.objects.all():
        notification.application_type = notification.content_type
        notification.application_id = notification.content_id
        notification.save()


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("transmissions", "0004_auto_20161027_1149"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="application_id",
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="notification",
            name="application_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                null=True,
                blank=True,
                related_name="notifications_for_application",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.RunPython(set_applications),
        migrations.AlterField(
            model_name="notification",
            name="application_id",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="notification",
            name="application_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="notifications_for_application",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="content_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="notifications_for_content",
                to="contenttypes.contenttype",
            ),
        ),
    ]
