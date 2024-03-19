# Generated by Django 5.0 on 2024-03-19 07:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('tasks', '0001_initial'),
        ('team', '0002_remove_teammodel_projects_remove_teammodel_tasks_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='role',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.RemoveField(
            model_name='employeeassign',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='employeeassign',
            name='task',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='user',
        ),
        migrations.RemoveField(
            model_name='taskmodel',
            name='user',
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='admin_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='team_name',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team.teammodel'),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='Cancel_reason',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.RemoveField(
            model_name='taskmodel',
            name='assigned_to',
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.category'),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='priority',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='status',
            field=models.CharField(blank=True, choices=[('Draft', 'Draft'), ('ONGOING', 'Ongoing'), ('ABANDON', 'Abandon'), ('COMPLETED', 'Completed')], max_length=20),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='EmployeeAssign',
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]
