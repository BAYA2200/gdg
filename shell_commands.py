from employee.models import *

emp_1 = Employee.objects.create(position='Chief', salary=1000000, work_experince=15, name='BAya', birth_year=2004)
emp_2 = Employee.objects.create(postion='manager', salary=35000, work_experince=10, name='Aman', birth_year=1999)
emp_3 = Employee.objects.create(position='Worker', salary=20000, work_experince=3, name='Max', birth_year=2000)
emp_4 = Employee.objects.create(position='Secretary', salary=50000, work_experince=7, name='Alia', birth_year=2003)

pass_1 = Passport.objects.create(inn=200, employee=emp_1, id_card=23432)
pass_2 = Passport.objects.create(inn=211, employee=emp_2, id_card=24965)
pass_3 = Passport.objects.create(inn=212, employee=emp_3, id_card=35325)
pass_4 = Passport.objects.create(inn=122, employee=emp_4, id_card=67345)


to_delete_employee = Employee.objects.get(id=4)
to_delete_employee.delete()


workproject = WorkProject.objects.create(project_name='My_app')
workproject.members.set([emp_1, emp_2, emp_3, emp_4], through_defaults={'date_joined': '2022-08-20'})

to_delete_employee = Employee.objects.get(id=3)
to_delete_employee.delete()

emp_5 = Employee.objects.create(position='Manager', salary=15000, work_experince=15, name='Arlen', birth_year=2004)

c1 = Client.objects.create(address='Isanova', phone_number=1222, name='Ivan', birth_year=2000)
c2 = Client.objects.create(address='Bokonbaeva', phone_number=1242, name='SERGEY', birth_year=2000)

c3 = VIPClient.objects.create(vip_status_start='2022.08.07',donation_amount=100000, address='Isanova', phone_number=222222)

delete_1 = Client.objects.get(id=1)
delete_1.delete()

a = Employee.objects.all()

for p in Passport.objects.all():
    print(p.inn)
    print(p.employee)
    print(p.id_card)

b = Membership.objects.all()
for i in Membership.objects.all():
    print(i.work_project)
    print(i.employee)
    print(i.date_joined)

for i in Client.objects.all():
    print(i.address)
    print(i.phone_number)

d = VIPClient.objects.all()
