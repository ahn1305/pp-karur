# Generated by Django 3.0.8 on 2022-06-12 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lb', '0003_auto_20220612_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cia_1_Result_Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_examination', models.CharField(blank=True, default='dd/mm/yyyy', max_length=200)),
                ('name_of_the_examination', models.CharField(blank=True, max_length=200)),
                ('total_number_of_students', models.IntegerField(blank=True, default=None)),
                ('no_of_students_appeared', models.IntegerField(blank=True, default=None)),
                ('no_of_students_passed', models.IntegerField(blank=True, default=None)),
                ('no_pf_students_failed', models.IntegerField(blank=True, default=None)),
                ('percentage_of_pass', models.CharField(blank=True, max_length=200)),
                ('no_of_students_below_40', models.IntegerField(blank=True, default=None)),
                ('no_of_students_below_40_60', models.IntegerField(blank=True, default=None)),
                ('no_of_students_below_60_75', models.IntegerField(blank=True, default=None)),
                ('no_of_students_below_75_100', models.IntegerField(blank=True, default=None)),
                ('related_with', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lb.LogBook')),
            ],
        ),
        migrations.CreateModel(
            name='university_Result_Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_examination', models.CharField(blank=True, default='dd/mm/yyyy', max_length=200)),
                ('name_of_the_examination', models.CharField(blank=True, max_length=200)),
                ('year', models.CharField(blank=True, max_length=200)),
                ('no_of_students_appeared', models.IntegerField(blank=True, default=None)),
                ('no_of_students_passed', models.IntegerField(blank=True, default=None)),
                ('no_pf_students_failed', models.IntegerField(blank=True, default=None)),
                ('percentage_of_pass', models.CharField(blank=True, max_length=200)),
                ('percentage_of_fail', models.CharField(blank=True, max_length=200)),
                ('higher_mark', models.CharField(blank=True, max_length=200)),
                ('faculty_handled', models.CharField(blank=True, max_length=200)),
                ('no_of_students_below_40', models.IntegerField(blank=True, default=None)),
                ('no_of_students_below_40_60', models.IntegerField(blank=True, default=None)),
                ('no_of_students_below_60_75', models.IntegerField(blank=True, default=None)),
                ('no_of_students_below_75_100', models.IntegerField(blank=True, default=None)),
                ('department', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lb.Department')),
                ('related_with', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lb.LogBook')),
            ],
        ),
        migrations.CreateModel(
            name='StudentParticulars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField(default=1)),
                ('Reg_No', models.CharField(max_length=200)),
                ('Name', models.CharField(max_length=200)),
                ('CIA_1', models.IntegerField(default=None)),
                ('retest_for_cia', models.IntegerField(blank=True, default=None)),
                ('CIA_2', models.IntegerField(default=None)),
                ('retest_for_cia2', models.IntegerField(blank=True, default=None)),
                ('modelexam', models.IntegerField(default=None)),
                ('CIA_1_AVG', models.IntegerField(default=None)),
                ('CIA_2_AVG', models.IntegerField(default=None)),
                ('Assignments', models.IntegerField(default=None)),
                ('Seminar', models.IntegerField(default=None)),
                ('Attendance', models.IntegerField(default=None)),
                ('InternalMarks', models.IntegerField(default=None)),
                ('related_with', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lb.LogBook')),
            ],
        ),
        migrations.CreateModel(
            name='RemedialForUniversity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField(blank=True, default=None)),
                ('reg_no', models.CharField(blank=True, max_length=200)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('date', models.CharField(default='dd/mm/yyyy', max_length=200)),
                ('related_with', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lb.LogBook')),
            ],
        ),
        migrations.CreateModel(
            name='RemedialForModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField(blank=True, default=None)),
                ('reg_no', models.CharField(blank=True, max_length=200)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('date', models.CharField(default='dd/mm/yyyy', max_length=200)),
                ('related_with', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lb.LogBook')),
            ],
        ),
        migrations.CreateModel(
            name='RemedialForCIA_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField(blank=True, default=None)),
                ('reg_no', models.CharField(blank=True, max_length=200)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('date', models.CharField(default='dd/mm/yyyy', max_length=200)),
                ('related_with', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lb.LogBook')),
            ],
        ),
        migrations.CreateModel(
            name='RemedialForCIA_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField(blank=True, default=None)),
                ('reg_no', models.CharField(blank=True, max_length=200)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('date', models.CharField(default='dd/mm/yyyy', max_length=200)),
                ('related_with', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lb.LogBook')),
            ],
        ),
        migrations.CreateModel(
            name='Model_Result_Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_examination', models.CharField(blank=True, max_length=200)),
                ('date_of_examination', models.CharField(blank=True, default='dd/mm/yyyy', max_length=200)),
                ('total_number_of_students', models.IntegerField(blank=True, default=None)),
                ('no_of_students_appeared', models.IntegerField(blank=True, default=None)),
                ('no_of_students_passed', models.IntegerField(blank=True, default=None)),
                ('no_pf_students_failed', models.IntegerField(blank=True, default=None)),
                ('percentage_of_pass', models.CharField(blank=True, max_length=200)),
                ('no_of_students_below_40', models.IntegerField(blank=True, default=None)),
                ('no_of_students_below_40_60', models.IntegerField(blank=True, default=None)),
                ('no_of_students_below_60_75', models.IntegerField(blank=True, default=None)),
                ('no_of_students_below_75_100', models.IntegerField(blank=True, default=None)),
                ('related_with', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lb.LogBook')),
            ],
        ),
        migrations.CreateModel(
            name='CorrectiveAndPreventiveUniversity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_for_failure', models.TextField(blank=True, max_length=300)),
                ('corrective_action', models.TextField(blank=True, max_length=300)),
                ('coaching_detials', models.TextField(blank=True, max_length=300)),
                ('coaching_detials_for_advance_learners', models.TextField(blank=True, max_length=300)),
                ('exam_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lb.Cia_1_Result_Analysis')),
                ('related_with', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lb.LogBook')),
            ],
        ),
        migrations.CreateModel(
            name='CorrectiveAndPreventiveModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_for_failure', models.TextField(blank=True, max_length=300)),
                ('corrective_action', models.TextField(blank=True, max_length=300)),
                ('coaching_detials', models.TextField(blank=True, max_length=300)),
                ('coaching_detials_for_advance_learners', models.TextField(blank=True, max_length=300)),
                ('exam_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lb.Cia_1_Result_Analysis')),
                ('related_with', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lb.LogBook')),
            ],
        ),
        migrations.CreateModel(
            name='CorrectiveAndPreventiveCIA_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_for_failure', models.TextField(blank=True, max_length=300)),
                ('corrective_action', models.TextField(blank=True, max_length=300)),
                ('coaching_detials', models.TextField(blank=True, max_length=300)),
                ('coaching_detials_for_advance_learners', models.TextField(blank=True, max_length=300)),
                ('exam_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lb.Cia_1_Result_Analysis')),
                ('related_with', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lb.LogBook')),
            ],
        ),
        migrations.CreateModel(
            name='CorrectiveAndPreventiveCIA_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_for_failure', models.TextField(blank=True, max_length=300)),
                ('corrective_action', models.TextField(blank=True, max_length=300)),
                ('coaching_detials', models.TextField(blank=True, max_length=300)),
                ('coaching_detials_for_advance_learners', models.TextField(blank=True, max_length=300)),
                ('exam_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lb.Cia_1_Result_Analysis')),
                ('related_with', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lb.LogBook')),
            ],
        ),
        migrations.CreateModel(
            name='Cia_2_Result_Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_examination', models.CharField(blank=True, default='dd/mm/yyyy', max_length=200)),
                ('name_of_the_examination', models.CharField(blank=True, max_length=200)),
                ('total_number_of_students', models.IntegerField(blank=True, default=None)),
                ('no_of_students_appeared', models.IntegerField(blank=True, default=None)),
                ('no_of_students_passed', models.IntegerField(blank=True, default=None)),
                ('no_pf_students_failed', models.IntegerField(blank=True, default=None)),
                ('percentage_of_pass', models.CharField(blank=True, max_length=200)),
                ('no_of_students_below_40', models.IntegerField(blank=True, default=None)),
                ('no_of_students_below_40_60', models.IntegerField(blank=True, default=None)),
                ('no_of_students_below_60_75', models.IntegerField(blank=True, default=None)),
                ('no_of_students_below_75_100', models.IntegerField(blank=True, default=None)),
                ('related_with', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lb.LogBook')),
            ],
        ),
    ]
