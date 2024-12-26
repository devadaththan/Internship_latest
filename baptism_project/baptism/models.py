from django.db import models
from django.utils.timezone import now


from django.db import models
from django.utils.timezone import now

class Baptism(models.Model):
    basic_baptism_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(default=1)  # Ensure this is not nullable or defaulting to 1
    place_of_baptism = models.CharField(max_length=255)
    date_of_baptism = models.DateField()
    time_of_baptism = models.TimeField()
    child_name_first = models.CharField(max_length=255)
    child_name_second = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField()
    mother_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=15)
    email = models.EmailField()
    advanced_baptism_id = models.IntegerField(editable=False, null=True, blank=True)
    priest_id = models.IntegerField(default=1)
    created_time = models.DateTimeField(default=now)
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def save(self, *args, **kwargs):
        if not self.pk:  # Ensure this is only applied when creating a new object
            self.advanced_baptism_id = self.basic_baptism_id  # Assign advanced_baptism_id
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.child_name_first} {self.child_name_second} - {self.status}"




class ParishDetails(models.Model):
    parish_id = models.AutoField(primary_key=True)
    parent_parish_id = models.IntegerField(default=1)
    name_of_parish = models.CharField(max_length=255)
    place_of_parish = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField()
    contact_no = models.CharField(max_length=15)
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    created_time = models.DateTimeField(default=now)

    def __str__(self):
        return self.name_of_parish
    
from django.contrib.auth.models import User
from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class LoginDetails(models.Model):
    PRIEST = 'Priest'
    ADMIN = 'Admin'
    PUBLIC = 'Public'
    SECRETARY = 'Secretary'
    ROLE_CHOICES = [
        (PRIEST, 'Priest'),
        (ADMIN, 'Admin'),
        (PUBLIC, 'Public'),
        (SECRETARY, 'Secretary'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="logindetails")  # Automatically creates user_id field
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)  # Use ROLE_CHOICES here
    contact_no = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    parish_id = models.IntegerField(default=1)
    last_login = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username


    


    




class BaptismAdvanced(models.Model):
    advanced_baptism_id = models.AutoField(primary_key=True)
    basic_baptism_id = models.IntegerField()
    q_id = models.IntegerField()
    priest_id = models.IntegerField()
    question = models.TextField()
    QUESTION_CHOICES = [
        ('MULTIPLE', 'MULTIPLE'),
        ('MULTIPLE-SELECT','MULTIPLE-SELECT'),
        ('TEXT-AREA','TEXT-AREA')
    ]
    question_type = models.CharField(max_length=255,choices=QUESTION_CHOICES,default='MULTIPLE')
    compulsary = models.BooleanField()  # True for compulsary, False otherwise
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    created_time = models.DateTimeField(default=now)
    field_id = models.IntegerField()
    data_varchar = models.CharField(max_length=255)

    def __str__(self):
        return f"Advanced Baptism {self.advanced_baptism_id}"


class FieldTable(models.Model):
    field_id = models.AutoField(primary_key=True)
    order_no = models.IntegerField()
    TYPE_CHOICES = [
        ('READING', 'READING'),
        ('SONG','SONG'),
        ('PRAYER','PRAYER'),
        ('REMARKS','REMARKS'),
        ('AUTHORIZATION','AUTHORIZATION'),
        ('FINANCIAL','FINANCIAL'),
        ('SPECIAL SAINTS','SPECIAL SAINTS'),
    ]
    type = models.CharField(max_length=20,choices=TYPE_CHOICES,default='READING')
    data = models.TextField()
    QUESTION_CHOICES = [
        ('MULTIPLE', 'MULTIPLE'),
        ('MULTIPLE-SELECT','MULTIPLE-SELECT'),
        ('TEXT-AREA','TEXT-AREA'),
    ]
    choice = models.CharField(max_length=20,choices=QUESTION_CHOICES,default='MULTIPLE')
    q_id = models.IntegerField()
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    created_time = models.DateTimeField(default=now)

    def __str__(self):
        return f"Field {self.field_id}: {self.type} (Order {self.order_no})"
    





