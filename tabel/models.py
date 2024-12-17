from django.db import models
from datetime import timedelta
from django.utils.timezone import now

class Rang(models.Model):

    name = models.CharField(max_length=50, unique=True, 
                            blank=False, null=False, 
                            verbose_name='Должность')
    
    is_admin = models.BooleanField(default=False,
                            verbose_name='Права админа')

    class Meta:
        db_table = 'rang'
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name
    


class Depart(models.Model):

    name = models.CharField(max_length=250, unique=True, 
                            blank=False, null=False, 
                            verbose_name='Департамент')
    
    parent = models.ForeignKey('self', on_delete=models.CASCADE, 
                               null=True, blank=True, 
                               related_name='children', verbose_name='Родитель')

    class Meta:
        db_table = 'depart'
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'

    def __str__(self):
        return self.name



class Employee(models.Model):

    tab = models.IntegerField(primary_key=True, unique=True, 
                              blank=False, null=False, db_index=True,
                              verbose_name='Табельный номер')
    
    fio = models.CharField(max_length=250, blank=False, null=False, verbose_name='ФИО')
    
    depart = models.ForeignKey(to=Depart, on_delete=models.CASCADE, 
                               blank=False, null=False, 
                               verbose_name='Департамент')
    
    adname = models.CharField(max_length=50, blank=False, null=False,
                              db_index=True, verbose_name='Фамилия и инициалы')

    class Meta:
        db_table = 'employee'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.adname
    


class EmployeeAccounting(models.Model):

    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE,
                            blank=False, null=False, 
                            verbose_name='Сотрудник')
    
    employment_date = models.DateField(default=now, verbose_name='Дата приема')
    dismissal_date = models.DateField(blank=True, null=True, verbose_name='Дата увольнения')

    def dismiss(self):
        self.dismissal_date = now().date()
        self.save()

    class Meta:
        db_table = 'employee_accounting'
        verbose_name = 'Учет сотрудника'
        verbose_name_plural = 'Учет сотрудников'

    def __str__(self):
        return f'{self.employee} {self.employment_date} {self.dismissal_date}'



class Vacation(models.Model):

    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE,
                            blank=False, null=False, 
                            verbose_name='Сотрудник')
    
    start_date = models.DateField(default=now, verbose_name='Дата начала')
    end_date = models.DateField(blank=True, null=True, verbose_name='Дата окончания')

    def calculate_vacation_end(self, days):
        self.end_date = self.start_date + timedelta(days=days)
        self.save()

    class Meta:
        db_table = 'vacation'
        verbose_name = 'Учет отпуска'
        verbose_name_plural = 'Учет отпусков'

    def __str__(self):
        return f'{self.employee} {self.start_date} {self.end_date}'
    


class Tabel(models.Model):

    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE,
                            blank=False, null=False, 
                            verbose_name='Сотрудник')
    
    date = models.DateField(default=now, verbose_name='Дата')
    type = models.CharField(max_length=6, blank=False, null=False, verbose_name='Буквенное обозначение')

    class Meta:
        db_table = 'tabel'
        verbose_name = 'Табель'
        verbose_name_plural = 'Табели'

    def __str__(self):
        return f'{self.employee} {self.date} {self.type}'