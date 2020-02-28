from django.db import models
from django.conf import settings


department_choices = (
    ('Finance', 'Finance'),
    ('Academics', 'Academics')
)
gender_choices = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others')
)
status_choices= (
    ('terminated', 'terminated'),
    ('current', 'current')
)
verification_choices= (
    ('verified', 'verified'),
    ('unverified', 'unverified')
    )

Maritalstatus_choices=(
    ('married', 'married'),
    ('unmarried', 'unmarried')
    )

nationality_choices=(
    ('Indian', 'Indian'),
    ('others', 'others')
    )
phy_choices=(
    ('Yes', 'Yes'),
    ('No', 'No')
    )



'''  Registered employee model Sahiti'''
class Employee(models.Model):
    empid = models.CharField(primary_key=True, max_length=100)
    name=models.CharField(max_length=50)
    email =models.EmailField(max_length=254)
    phone=models.BigIntegerField()
    dept = models.CharField(max_length=30, choices=department_choices)
    emp_status= models.CharField(max_length=30, choices=status_choices)
    supervisor=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    gender = models.CharField(max_length=30,choices=gender_choices)
    profile_status=models.CharField(max_length=50, choices=verification_choices)
    post=models.CharField(max_length=50)


    def __str__(self):
        return self.name

'''Employee  BioData model of the employee Sahiti'''
class EmployeeBioData(models.Model):
    emp = models.OneToOneField(Employee,on_delete = models.CASCADE,primary_key = True)
    dob = models.DateField()
    marital_status=models.CharField(max_length=30, choices=Maritalstatus_choices)
    nationality=models.CharField(max_length=30, choices=nationality_choices)
    physically_challenged=models.CharField(max_length=30, choices=phy_choices)
    category = models.CharField(max_length=25,
                                choices=[
                                    ('GEN', 'General'),
                                    ('SC', 'SC'),
                                    ('ST', 'ST'),
                                    ('OBC-CL', 'OBC Creamy Layer'),
                                    ('OBC-NCL', 'OBC Non Creamy Layer'),
                                    ('GEN-PWD', 'General Person with disabilties'),
                                    ('OBC-CL-PWD', 'OBC Creamy Layer Person with disabilites'),
                                    ('OBC-NCL-PWD', 'OBC Non Creamy Layer Person with disabilites'),
                                    ('SC-PWD', 'SC person with disabilites'),
                                    ('ST-PWD', 'ST person with disabilites'),
                                ],
                                )
    reservation = models.CharField(max_length=25,
                                   choices=[
                                       ('GEN', 'General'),
                                       ('SC', 'SC'),
                                       ('ST', 'ST'),
                                       ('OBC-NCL', 'OBC Non Creamy Layer'),
                                       ('PWD', 'General Person with disabilties'),
                                       ('SERVICE', 'Ex-Service Man'),
                                       ('GEN-ECO', 'General Category Economically Weaker Sections'),
                                   ],
                                   null=True,
                                   blank=True,
                                   )
    current_address = models.TextField()
    permanent_address = models.TextField()

    def __str__(self):
        return str(self.emp.name)


''' Salary Details model of the employee Sahiti'''
class EmployeeBank_Salary_Details(models.Model):
    emp= models.OneToOneField(Employee,on_delete = models.CASCADE,primary_key = True,related_name='Professional_details')
    acc_name=models.CharField(max_length=50)
    ifsc_code=models.CharField(max_length=11)
    acc_num=models.BigIntegerField()

    def __str__(self):
        return str(self.emp.name)


''' Employee Academic Details model  Sahiti'''
class EmployeeAcademic_Details(models.Model):
    emp = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='academic_detail')
    degree = models.CharField(max_length=200)
    area_of_qualification = models.CharField(max_length=200)
    category_of_university = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    status = models.CharField(max_length=200,
                              choices=[
                                  ('Completed', 'Completed'),
                                  ('ResultAwaited', 'ResultAwaited'),
                                  ('FinalAwaited', 'FinalAwaited'),
                                  ('Ongoing', 'Ongoing'),
                              ],
                              )
    year_of_passing = models.IntegerField()
    percentage = models.IntegerField()
    photo=models.ImageField()

    def __str__(self):
        return str(self.emp.name)

''' Employee research Details model  Sahiti'''
class EmployeeResearch_Details(models.Model):
    emp = models.ForeignKey(Employee,
                                  on_delete=models.CASCADE,
                                  related_name='teaching_and_research_detail',
                                  )
    research_title = models.CharField(max_length=200)
    Awards=models.TextField(max_length=200)
    publishion_date=models.DateField(max_length=200)


    def __str__(self):
        return str(self.emp.name)


''' Employee  ProfessionDetails model  Sahiti'''
class EmployeeProfession_Details(models.Model):
    '''Model for professional details of applicant'''
    emp = models.ForeignKey(Employee,
                                on_delete=models.CASCADE,
                                related_name='professional_detail',
                )
    organisation = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    from_year = models.IntegerField()
    to_year = models.IntegerField()
    role = models.CharField(max_length=250)
    pay_scale = models.IntegerField()
    emoluments = models.IntegerField()

    def __str__(self):
        return str(self.emp.name)