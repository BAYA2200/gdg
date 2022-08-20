from django.db import models


# Create your models here.

class AbstractPerson(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def get_age(self):
        year = 2022 - self.birth_year.year
        return year


class Employee(AbstractPerson):
    position = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    work_experience = models.IntegerField()

    def save(self, *args, **kwargs):
        print(f'Поле position c {self.position} , salary {self.salary}, work_experience {self.work_experience} были сохранены ')


    def __str__(self):
        return self.position and self.salary


class Passport(models.Model):
    inn = models.IntegerField(max_length=100)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    id_card = models.CharField(max_length=100)

    def get_gender(self):
        first = int(self.inn[0])
        if first == 1:
            return 'Female'
        if first == 2:
            return 'Male'

    def save(self, *args, **kwargs):
        print(f'Поле inn c {self.inn} , employee {self.employee}, id_card {self.id_card} были сохранены ')


    def __str__(self):
        return f" инн {self.inn} ид карты {self.id_card}"


class WorkProject(models.Model):
    project_name = models.CharField(max_length=100)
    members = models.ManyToManyField(Employee, through='Membership')

    def save(self, *args, **kwargs):
        print(f'Поле project_name c {self.project_name} , members {self.members} были сохранены ')

    def __str__(self):
        return self.project_name


class Membership(models.Model):
    work_project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date_joined = models.DateField()

    def save(self, *args, **kwargs):
        print(f'Поле work_project c {self.work_project} , employee {self.employee}, date_joined {self.date_joined} были сохранены ')

    def __str__(self):
        return f'{self.employee} joined {self.work_project} on {self.date_joined}'


class Client(AbstractPerson):
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        print(f'Поле address c {self.address} , phone_number {self.phone_number}, были сохранены ')


class VIPClient(Client):
    vip_status_start = models.DateField()
    donation_amount = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        print(f'Поле vip_status_start c {self.vip_status_start} , donation_amount {self.donation_amount}, были сохранены ')

