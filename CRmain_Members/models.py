from django.db import models
from django_countries.fields import CountryField
from multi_email_field.fields import MultiEmailField
from phone_field import PhoneField

# Create your models here.


class crossroadmember(models.Model):
    STATE_CHOICES =(("NA", "NA"),("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
    DISTRICT_CHOICES =(("NA", "NA"),("Bengaluru", "Bengaluru"),("Chennai", "Chennai"),("Delhi", "Delhi"),("Dharwad", "Dharwad"),("Dimapur", "Dimapur"),("Imphal","Imphal"),("Ernakulam","Ernakulam"),
        ("Kolkata", "Kolkata"),("Mumbai", "Mumbai"),("Mysore", "Mysore"), ("Nagpur", "Nagpur"),("Pune", "Pune"),
        ("Shillong", "Shillong"),("Visakhapatnam", "Visakhapatnam"),
        ("Vellore","Vellore"),("Chittoor", "Chittoor"))
    
    #timothy_CHOICES = (("True", "Yes"),("False","No") )
    salutation =(("Mr","Mr"), ("Mrs","Mrs"), ("Ms","Ms"), ("Master","Master"))
    status = (("Covenant Member","Covenant Member"), ("Regular Visitor","Regular Visitor"), ("left","left"))
    id = models.AutoField(primary_key=True,)
    status = models.CharField(max_length=100, null=True, choices=status)
    date_joined = models.DateField(null=True)
    salutation = models.CharField(max_length=100, null=True,  choices=salutation)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(upload_to ='media/profile_pic/', null=True, blank=True)
    country_of_Citizenship = CountryField(null=True, blank_label='(select country)')
    state = models.CharField(max_length=200, null=True,  choices = STATE_CHOICES)
    district = models.CharField(max_length=200, null=True,  choices = DISTRICT_CHOICES)
    pin_code = models.IntegerField(null=True,)
    email = MultiEmailField(blank=True, default='', null=True,help_text='email')
    phone =  PhoneField(blank=True, default='', null=True,help_text='Contact phone number')
    Note = models.TextField(blank=True, null=True,)

     

class newvisitor(models.Model):
    STATE_CHOICES =(("NA", "NA"),("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
    DISTRICT_CHOICES =(("NA", "NA"),("Bengaluru", "Bengaluru"),("Chennai", "Chennai"),("Delhi", "Delhi"),("Dharwad", "Dharwad"),("Dimapur", "Dimapur"),("Imphal","Imphal"),("Ernakulam","Ernakulam"),
        ("Kolkata", "Kolkata"),("Mumbai", "Mumbai"),("Mysore", "Mysore"), ("Nagpur", "Nagpur"),("Pune", "Pune"),
        ("Shillong", "Shillong"),("Visakhapatnam", "Visakhapatnam"),
        ("Vellore","Vellore"),("Chittoor", "Chittoor"))
    #timothy_CHOICES = (("True", "Yes"),("False","No") )
    salutation =(("Mr","Mr"), ("Mrs","Mrs"), ("Ms","Ms"), ("Master","Master"), ("NA","NA"))
    status = (("New Visitor","New Visitor"), ("0","0"))
    how = (("God","God"),("Friend","Friend"),("Google","Google"), ("NA","NA"))
    connect = (("NA","NA"),("Would like to talk","Would like to talk"),("Exploring faith","Exploring faith"),
        ("Would like a visit","Would like a visit"), ("Interested in membership","Interested in membership"), 
        ("New to this area","New to this area"), ("Put on mailing list","Put on mailing list") )
    id = models.AutoField(primary_key=True,)
    status = models.CharField(max_length=100, null=True, choices=status)
    date_visited = models.DateField(null=True)
    salutation = models.CharField(max_length=100, null=True,  choices=salutation)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    country_of_Citizenship = CountryField(null=True, blank_label='(select country)')
    state = models.CharField(max_length=200, null=True,  choices = STATE_CHOICES)
    district = models.CharField(max_length=200, null=True,  choices = DISTRICT_CHOICES)
    location= models.CharField(max_length=100, null=True, blank=True)
    pin_code = models.IntegerField(null=True,)
    email = MultiEmailField(blank=True, default='', null=True,help_text='email')
    phone =  PhoneField(blank=True, default='', null=True,help_text='Contact phone number')
    How_did_you_know_about_us = models.CharField(max_length=100, null=True, choices=how)
    choices = models.CharField(max_length=100, null=True, choices=connect)
    Note = models.TextField(blank=True, null=True,)

   
class NewChurches(models.Model):
    DISTRICT_CHOICES =(("NA", "NA"),("Bengaluru", "Bengaluru"),("Chandigarh", "Chandigarh"),("Chennai", "Chennai"),("Delhi", "Delhi"),("Dharwad", "Dharwad"),("Dimapur", "Dimapur"),("Imphal","Imphal"),("Ernakulam","Ernakulam"),
        ("Kolkata", "Kolkata"),("Mumbai", "Mumbai"),("Mysore", "Mysore"), ("Nagpur", "Nagpur"),("Pune", "Pune"),
        ("Shillong", "Shillong"),("Katmandu", "Katmandu"),("Visakhapatnam", "Visakhapatnam"),("Vellore","Vellore"),("Chittoor", "Chittoor"))
    status = (("Alive","Alive"), ("Defunct","Defunct"))

    id =models.AutoField(primary_key=True,)
    status = models.CharField(max_length=100, null=True, choices=status)
    country = CountryField(null=True, blank_label='(select country)')
    city = models.CharField(max_length=200, null=True,  choices = DISTRICT_CHOICES)
    location= models.CharField(max_length=100, null=True, blank=True)
    pin_code = models.IntegerField(null=True,)
    Planter = models.CharField(max_length=100, null=True, blank=True)
    email = MultiEmailField(blank=True, default='', null=True,help_text='email')
    phone =  PhoneField(blank=True, default='', null=True,help_text='Contact phone number')
    Year_Established = models.DateField(null=True)
    Summary = models.TextField(blank=True, null=True,)
    image = models.ImageField(upload_to ='media/profile_pic/', null=True, blank=True)


class Intern(models.Model):
    STATE_CHOICES =(("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
    DISTRICT_CHOICES =(("NA", "NA"),("Bengaluru", "Bengaluru"),("Chandigarh", "Chandigarh"),("Chennai", "Chennai"),("Delhi", "Delhi"),("Dharwad", "Dharwad"),("Dimapur", "Dimapur"),("Imphal","Imphal"),("Ernakulam","Ernakulam"),
        ("Kolkata", "Kolkata"),("Mumbai", "Mumbai"),("Mysore", "Mysore"), ("Nagpur", "Nagpur"),("Pune", "Pune"),
        ("Shillong", "Shillong"),("Katmandu", "Katmandu"),("Visakhapatnam", "Visakhapatnam"),("Vellore","Vellore"),("Chittoor", "Chittoor"))
    Marriage_CHOICES = (("Married", "Married"),("Unmarried","Unmarried") )
    Spouse_CHOICES = (("True", "Yes"),("False","No"), ("NA","NA")  )
    Physical_CHOICES = (("Good", "Good"),("Poor","Poor") )
    Education_CHOICES = (("Regular", "Regular"),("correspondence","correspondence") )
    theological_CHOICES = (("Regular", "Regular"),("correspondence","correspondence"), ("NA","NA") )
    training_CHOICES = (("True", "Yes"),("False","No") )
    church_CHOICES = (("True", "Yes"),("False","No") )
    ordain_CHOICES = (("True", "Yes"),("False","No") )
    status = (("Active","Active"), ("Disqualified","Disqualified"))

    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100, null=True, choices=status)
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True,)
    end_date = models.DateField(auto_now_add=False, null=True, auto_now=False, blank=True,)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(upload_to ='media/profile_pic/', null=True, blank=True)
    summary = models.TextField(blank=True)
    country_of_Citizenship = CountryField(blank_label='(select country)')
    state = models.CharField(max_length=200,   choices = STATE_CHOICES)
    district = models.CharField(max_length=200,   choices = DISTRICT_CHOICES)
    pin_code = models.IntegerField()
    Marital_Status = models.CharField(max_length=200,   choices = Marriage_CHOICES)
    Name_of_Spouse = models.CharField(max_length=100, null=True, blank=True)
    Years_of_Marriage = models.IntegerField()
    Is_Spouse_Christian = models.CharField(max_length=200,   choices = Spouse_CHOICES)
    No_of_Children = models.IntegerField()
    General_Physical_Health =  models.CharField(max_length=200, choices = Physical_CHOICES)
    If_Poor_please_explain  = models.TextField(blank=True)
    education_qualification_training = models.CharField(max_length=200,  choices = Education_CHOICES)
    theological_qualification = models.CharField(max_length=200, choices = theological_CHOICES)
    Name_of_the_college_Seminary = models.CharField(max_length=100, null=True, blank=True)
    Place = models.CharField(max_length=100, null=True, blank=True)
    year_of_graduation = models.IntegerField()
    are_you_already_engaged_in_any_other_training_program = models.CharField(max_length=200,  choices = training_CHOICES)
    If_yes_please_explain  = models.TextField(blank=True)
    are_you_involved_in_any_church_and_or_ministry_activity = models.CharField(max_length=200,  choices = church_CHOICES)
    If_yes_please_explain  = models.TextField(blank=True)
    are_you_ordained_or_licensed_pastor = models.CharField(max_length=200, choices = ordain_CHOICES)
    by_whom = models.CharField(max_length=100, null=True, blank=True)
    Church_or_Denominational_Membership = models.CharField(max_length=100, null=True, blank=True)
    Name_of_the_church = models.CharField(max_length=100, null=True, blank=True)
    Denomination = models.CharField(max_length=100, null=True, blank=True)
    Head_of_your_denomination_Mentor_name = models.CharField(max_length=100, null=True, blank=True)
    were_would_you_like_to_plant_a_church_and_why = models.TextField(blank=True)
    Briefly_describe_your_Salvation_experience = models.TextField(blank=True)
    Mention_the_languages_you_speak_Read_Write = models.CharField(max_length=100, null=True, blank=True)
