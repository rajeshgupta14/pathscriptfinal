from __future__ import unicode_literals
from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _
from myapp.models import Project,Client,User,Product
from datetime import datetime    




#KYC FORMS
class Article(models.Model):
    typecomp = (
              
             ('proprietary','Proprietary'), 
             ('partnership','Partnership'),
             ('llp','LLP'),
             ('private_ltd','Private Ltd'),
             ('limited','Limited'),
             ('privately_held','Private held'),
             ('publically_traded','Publically traded')
             )
    typeactiv = (
              
             ('manufacturing','Manufacturing'), 
             ('services','Services'),
             ('retail','Retail'),
             ('distribution','Distribution'),
             ('job works oem','Job works oem'),
             ('r and d','R and D'),
             )
    
    company_name=models.ForeignKey(Client,blank=True,null=True)
    version=models.IntegerField(blank=True,default=1)
    founding_date=models.DateField(blank=True,null=True)
    headquarter_location=CountryField(blank=True,null=True)
    areas_served=models.CharField(max_length=400,blank=True,null=True)
    no_of_employees=models.CharField(max_length=400,blank=True,null=True)
    type_of_company=models.CharField(max_length=42,choices=typecomp,blank=True,null=True)
    type_of_industry=models.CharField(max_length=42,blank=True,null=True)
    type_of_activity=models.CharField(max_length=400,choices=typeactiv,blank=True,null=True)
    warehouse_addresses=models.TextField(blank=True,null=True)
    factory_addresses=models.TextField(blank=True,null=True)
    number_of_owners_and_officers=models.CharField(max_length=400,blank=True,null=True)
    officers_and_roles=models.TextField(blank=True,null=True)
    registered_address=models.CharField(max_length=700,blank=True,null=True)
    telephone=models.CharField(max_length=400,blank=True,null=True)
    email=models.CharField(max_length=400,blank=True,null=True)
    website=models.CharField(max_length=400,blank=True,null=True)
    upload_Doc1=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc2=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc3=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc4=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc5=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc6=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc7=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc8=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc9=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc10=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc11=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc12=models.FileField(upload_to="media",blank=True,null=True)
    services_opted=models.ManyToManyField(Product,blank=True)
    notes=models.TextField(blank=True,null=True)
    
    class Meta:
        verbose_name = _("KYC Form")
        verbose_name_plural = _("KYC Forms")
    
    
    def __str__(self):
       return str(self.company_name)
#BRANCH FORMS
class Branch(models.Model):
    
    company_name=models.ForeignKey(Client,blank=True,null=True)
    branch_name=models.CharField(max_length=400,blank=True,null=True)
    branch_founding_date=models.DateField(blank=True,null=True)
    branch_location=models.CharField(max_length=400,blank=True,null=True)
    areas_served_by_branch=models.CharField(max_length=400,blank=True,null=True)
    no_of_employees_in_branch=models.CharField(max_length=400,blank=True,null=True)
    type_of_business_by_branch=models.CharField(max_length=400,blank=True,null=True)
    number_of_owners_and_officers_in_branch=models.CharField(max_length=400,blank=True,null=True)
    officers_and_roles_in_branch=models.TextField(blank=True,null=True)
    branch_registered_address=models.CharField(max_length=700,blank=True,null=True)
    branch_telephone=models.CharField(max_length=400,blank=True,null=True)
    branch_email=models.CharField(max_length=400,blank=True,null=True)
    branch_website=models.CharField(max_length=400,blank=True,null=True)
    upload_Doc1=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc2=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc3=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc4=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc5=models.FileField(upload_to="media",blank=True,null=True)
    
    class Meta:
        verbose_name = _("Branch Form")
        verbose_name_plural = _("Branch Forms")
    def __str__(self):
       return self.branch_name
#SUBSIDIARY FORMS
class Subsidiary(models.Model):
    
    company_name=models.ForeignKey(Client,blank=True,null=True)
    subsidiary_name=models.CharField(max_length=400,blank=True,null=True)
    subsidiary_founding_date=models.DateField(blank=True,null=True)
    subsidiary_location=models.CharField(max_length=400,blank=True,null=True)
    areas_served_by_subsidiary=models.CharField(max_length=400,blank=True,null=True)
    no_of_employees_in_subsidiary=models.CharField(max_length=400,blank=True,null=True)
    type_of_business_by_subsidiary=models.CharField(max_length=400,blank=True,null=True)
    subsidiary_warehouse_addresses=models.TextField(blank=True,null=True)
    subsidiary_factory_addresses=models.TextField(blank=True,null=True)
    number_of_owners_and_officers_in_subsidiary=models.CharField(max_length=400,blank=True,null=True)
    officers_and_roles_in_subsidiary=models.TextField(blank=True,null=True)
    subsidiary_registered_address=models.CharField(max_length=700,blank=True,null=True)
    subsidiary_telephone=models.CharField(max_length=400,blank=True,null=True)
    subsidiary_email=models.CharField(max_length=400,blank=True,null=True)
    subsidiary_website=models.CharField(max_length=400,blank=True,null=True)
    upload_Doc1=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc2=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc3=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc4=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc5=models.FileField(upload_to="media",blank=True,null=True)
    
    class Meta:
        verbose_name = _("Subsidiary Form")
        verbose_name_plural = _("Subsidiary Forms")
    def __str__(self):
       return self.subsidiary_name
#RELATED COMPANY FORMS
class Relatedcompany(models.Model):
    
    company_name=models.ForeignKey(Client,blank=True,null=True)
    related_company_name=models.CharField(max_length=40,blank=True,null=True)
    relation=models.TextField(blank=True,null=True)
    related_company_registered_address=models.CharField(max_length=700,blank=True,null=True)
    related_company_telephone=models.CharField(max_length=400,blank=True,null=True)
    related_company_email=models.CharField(max_length=400,blank=True,null=True)
    related_company_website=models.CharField(max_length=400,blank=True,null=True)
    upload_Doc1=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc2=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc3=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc4=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc5=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc6=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc7=models.FileField(upload_to="media",blank=True,null=True)
    
    class Meta:
        verbose_name = _("Related Company Form")
        verbose_name_plural = _("Related Company Forms")
    def __str__(self):
       return self.related_company_name
#BG CHECK FORMS
class Backgroundcheck(models.Model):
    
    company_name=models.ForeignKey(Client,blank=True,null=True)
    version=models.IntegerField(blank=True,default=1)
    form_name=models.CharField(max_length=200,blank=True,null=True)
    rOC_Certificates=models.BooleanField(default=False)
    c1=models.ForeignKey(User,verbose_name="Currently With",related_name="c1",blank=True,null=True)
    mOA=models.BooleanField(default=False)
    c2=models.ForeignKey(User,verbose_name="Currently With",related_name="c2",blank=True,null=True)
    current_List_of_Directors_including_Photo_ID=models.BooleanField(default=False)
    c3=models.ForeignKey(User,verbose_name="Currently With",related_name="c3",blank=True,null=True)
    term_Sheets=models.BooleanField(default=False)
    c4=models.ForeignKey(User,verbose_name="Currently With",related_name="c4",blank=True,null=True)
    current_Bankers_and_Auditors_and_Company_Secretary=models.BooleanField(default=False)
    c5=models.ForeignKey(User,verbose_name="Currently With",related_name="c5",blank=True,null=True)
    sales_Tax_Registration_Certificate=models.BooleanField(default=False)
    c6=models.ForeignKey(User,verbose_name="Currently With",related_name="c6",blank=True,null=True)
    last_Filed_Sales_Tax_Certificate=models.BooleanField(default=False)
    c7=models.ForeignKey(User,verbose_name="Currently With",related_name="c7",blank=True,null=True)
    municipal_Certificate=models.BooleanField(default=False)
    c8=models.ForeignKey(User,verbose_name="Currently With",related_name="c8",blank=True,null=True)
    last_2_years_Audited_Books_of_Accounts=models.BooleanField(default=False)
    c9=models.ForeignKey(User,verbose_name="Currently With",related_name="c9",blank=True,null=True)
    last_Paid_Tax_Receipt=models.BooleanField(default=False)
    c10=models.ForeignKey(User,verbose_name="Currently With",related_name="c10",blank=True,null=True)
    employee_List_Statement=models.BooleanField(default=False)
    c11=models.ForeignKey(User,verbose_name="Currently With",related_name="c11",blank=True,null=True)
    last_Provident_Fund_Receipt=models.BooleanField(default=False)
    c12=models.ForeignKey(User,verbose_name="Currently With",related_name="c12",blank=True,null=True)
    list_of_Competitors=models.BooleanField(default=False)
    c13=models.ForeignKey(User,verbose_name="Currently With",related_name="c13",blank=True,null=True)
  
   
    class Meta:
        verbose_name = _("BGCheck Form")
        verbose_name_plural = _("BGCheck Forms")
    
    def __unicode__(self):
       return self.form_name

#BG CHECK LOGS    
class Backgroundcheckb(models.Model):
    
    company_name=models.ForeignKey(Client,blank=True,null=True)
    form_name=models.CharField(max_length=200,blank=True,null=True)
    version=models.IntegerField(blank=True,default=1)
    user=models.CharField(max_length=200,blank=True,null=True)
    date=models.DateTimeField(default=datetime.now())
    rOC_Certificates=models.BooleanField(default=False)
    c1=models.ForeignKey(User,verbose_name="Currently With",related_name="ca",blank=True,null=True) #C1,C2..Cn -> "currently with" field ( reason why it is named as C1,C2..Cn is because two db fiels cannot have same names)
    mOA=models.BooleanField(default=False)
    c2=models.ForeignKey(User,verbose_name="Currently With",related_name="cb",blank=True,null=True)
    current_List_of_Directors_including_Photo_ID=models.BooleanField(default=False)
    c3=models.ForeignKey(User,verbose_name="Currently With",related_name="cc",blank=True,null=True)
    term_Sheets=models.BooleanField(default=False)
    c4=models.ForeignKey(User,verbose_name="Currently With",related_name="cd",blank=True,null=True)
    current_Bankers_and_Auditors_and_Company_Secretary=models.BooleanField(default=False)
    c5=models.ForeignKey(User,verbose_name="Currently With",related_name="ce",blank=True,null=True)
    sales_Tax_Registration_Certificate=models.BooleanField(default=False)
    c6=models.ForeignKey(User,verbose_name="Currently With",related_name="cf",blank=True,null=True)
    last_Filed_Sales_Tax_Certificate=models.BooleanField(default=False)
    c7=models.ForeignKey(User,verbose_name="Currently With",related_name="cg",blank=True,null=True)
    municipal_Certificate=models.BooleanField(default=False)
    c8=models.ForeignKey(User,verbose_name="Currently With",related_name="ch",blank=True,null=True)
    last_2_years_Audited_Books_of_Accounts=models.BooleanField(default=False)
    c9=models.ForeignKey(User,verbose_name="Currently With",related_name="ci",blank=True,null=True)
    last_Paid_Tax_Receipt=models.BooleanField(default=False)
    c10=models.ForeignKey(User,verbose_name="Currently With",related_name="cj",blank=True,null=True)
    employee_List_Statement=models.BooleanField(default=False)
    c11=models.ForeignKey(User,verbose_name="Currently With",related_name="ck1",blank=True,null=True)
    last_Provident_Fund_Receipt=models.BooleanField(default=False)
    c12=models.ForeignKey(User,verbose_name="Currently With",related_name="cl2",blank=True,null=True)
    list_of_Competitors=models.BooleanField(default=False)
    c13=models.ForeignKey(User,verbose_name="Currently With",related_name="cm3",blank=True,null=True)
   
    
    # c14=models.ForeignKey(User,verbose_name="Currently With",related_name="cn4",blank=True,null=True)
    class Meta:
        verbose_name = _("BGCheck Log")
        #verbose_name_plural = _("BGCheck Forms")
    
   
    def __unicode__(self):
       return self.form_name

    
    
#Duediligence Forms - Temporary    
class Duediligence(models.Model):
    
    
    
      
    stagechoices = (
            ( 'start_up','Start up'),
            ( 'growing','Growing'),               
            ('matured','Matured' )
            )

    typecomp = (
              
             ('proprietary','Proprietary'), 
             ('partnership','Partnership'),
             ('llp','LLP'),
             ('private_ltd','Private Ltd'),
             ('limited','Limited'),
             ('privately_held','Private held'),
             ('publically_traded','Publically traded')
             )


    company_name=models.ForeignKey(Client,blank=True,null=True)
    project = models.ForeignKey(Project,to_field='id',blank=True)
    form_name=models.CharField(max_length=11,blank=True,null=True)
    #company_name=models.ForeignKey(Client,blank=True,null=True)
    upload_Doc1=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc2=models.FileField(upload_to="media",blank=True,null=True)
    version=models.IntegerField(blank=True,default=1)
    date=models.DateField(blank=True,null=True)
    please_select_the_growth_stage_of_your_company=models.CharField(max_length=30,choices=stagechoices,blank=True,null=True)
    please_tick_the_type_of_company=models.CharField(max_length=12,choices=typecomp,blank=True,null=True)
    stock_exchange=models.CharField(max_length=50,blank=True,null=True)
    ticker_ID = models.CharField(max_length=20,blank=True,null=True)
    what_is_the_key_need_you_are_providing_for_your_customer =models.TextField(max_length=600,blank=True,null=True)
    evidences_that_show_need_stated_above_for_customer_is_fulfilled=models.TextField(max_length=600,blank=True,null=True)
    what_are_some_of_the_aspects_you_are_facing_a_challenge_with=models.TextField(max_length=600,blank=True,null=True)
    
    def __unicode__(self):
       return self.form_name

    class Meta:
        verbose_name = _("Duediligence - Temporary Form")
        verbose_name_plural = _("Duediligence - Temporary Forms")
    
    
    

#Duediligence - Permanent
class Duediligencep(models.Model):
    
    
    
      
    stagechoices = (
            ( 'start_up','Start up'),
            ( 'growing','Growing'),               
            ('matured','Matured' )
            )

    typecomp = (
              
             ('proprietary','Proprietary'), 
             ('partnership','Partnership'),
             ('llp','LLP'),
             ('private_ltd','Private Ltd'),
             ('limited','Limited'),
             ('privately_held','Private held'),
             ('publically_traded','Publically traded')
             )


    company_name=models.ForeignKey(Client,blank=True,null=True)
    project = models.ForeignKey(Project,blank=True)
    form_name=models.CharField(max_length=200,blank=True,null=True)
    upload_Doc1=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc2=models.FileField(upload_to="media",blank=True,null=True)
    #company_name=models.ForeignKey(Client,blank=True,null=True)
    #upload_XSLX=models.FileField(upload_to="media",blank=True,null=True)
    #upload_IMG=models.FileField(upload_to="media",blank=True,null=True)
    version=models.IntegerField(blank=True,default=1)
    date=models.DateField(blank=True,null=True)
    please_select_the_growth_stage_of_your_company=models.CharField(max_length=30,choices=stagechoices,blank=True,null=True)
    please_tick_the_type_of_company=models.CharField(max_length=12,choices=typecomp,blank=True,null=True)
    stock_exchange=models.CharField(max_length=50,blank=True,null=True)
    ticker_ID = models.CharField(max_length=20,blank=True,null=True)
    what_is_the_key_need_you_are_providing_for_your_customer =models.TextField(max_length=600,blank=True,null=True)
    evidences_that_show_need_stated_above_for_customer_is_fulfilled=models.TextField(max_length=600,blank=True,null=True)
    what_are_some_of_the_aspects_you_are_facing_a_challenge_with=models.TextField(max_length=600,blank=True,null=True)

    class Meta:
        verbose_name = _("Duediligence - Permanent Form")
        verbose_name_plural = _("Duediligence - Permanent Forms")
        
        
    def __unicode__(self):
       return self.form_name

    
    













#Script Forms - Temporary
    
class Script(models.Model):

      
    stagechoices = (
            ( 'start_up','Start up'),
            ( 'growing','Growing'),               
            ('matured','Matured' )
            )

    typecomp = (
              
             ('proprietary','Proprietary'), 
             ('partnership','Partnership'),
             ('llp','LLP'),
             ('private_ltd','Private Ltd'),
             ('limited','Limited'),
             ('privately_held','Private held'),
             ('publically_traded','Publically traded')
             )


    company_name=models.ForeignKey(Client,blank=True,null=True)
    project = models.ForeignKey(Project,blank=True)
    form_name=models.CharField(max_length=200,blank=True,null=True)
    upload_Doc1=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc2=models.FileField(upload_to="media",blank=True,null=True)
    version=models.IntegerField(blank=True,default=1)
    date=models.DateField(blank=True,null=True)
    please_select_the_growth_stage_of_your_company=models.CharField(max_length=30,choices=stagechoices,blank=True,null=True)
    please_tick_the_type_of_company=models.CharField(max_length=12,choices=typecomp,blank=True,null=True)
    stock_exchange=models.CharField(max_length=50,blank=True,null=True)
    ticker_ID = models.CharField(max_length=20,blank=True,null=True)
    what_is_the_idea_you_are_looking_to_implement=models.TextField(blank=True,null=True)
    why_do_you_think_that_the_idea_should_be_implemented=models.TextField(blank=True,null=True)
    was_this_idea_previously_executed_and_if_yes_state_the_method=models.TextField(blank=True,null=True)
    reasons_for_failure_of_previous_implementation_methods=models.TextField(blank=True,null=True)
    other_methods_of_implementation_that_you_would_suggest=models.TextField(blank=True,null=True)
    is_the_level_of_implementation_generic_or_specific=models.TextField(blank=True,null=True)
    deadline_by_which_you_need_the_idea_to_be_implemented=models.TextField(blank=True,null=True)
    
    
    class Meta:
        verbose_name = _("Script&Control - Temporary Form")
        verbose_name_plural = _("Script&Control - Temporary Forms")
    
    def __unicode__(self):
       return self.form_name

    #Script Forms - Permanent
    
class Scriptp(models.Model):

      
    stagechoices = (
            ( 'start_up','Start up'),
            ( 'growing','Growing'),               
            ('matured','Matured' )
            )

    typecomp = (
              
             ('proprietary','Proprietary'), 
             ('partnership','Partnership'),
             ('llp','LLP'),
             ('private_ltd','Private Ltd'),
             ('limited','Limited'),
             ('privately_held','Private held'),
             ('publically_traded','Publically traded')
             )


    company_name=models.ForeignKey(Client,blank=True,null=True)
    project = models.ForeignKey(Project,blank=True)
    form_name=models.CharField(max_length=200,blank=True,null=True)
    upload_Doc1=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc2=models.FileField(upload_to="media",blank=True,null=True)
    version=models.IntegerField(blank=True,default=1)
    date=models.DateField(blank=True,null=True)
    please_select_the_growth_stage_of_your_company=models.CharField(max_length=30,choices=stagechoices,blank=True,null=True)
    please_tick_the_type_of_company=models.CharField(max_length=12,choices=typecomp,blank=True,null=True)
    stock_exchange=models.CharField(max_length=50,blank=True,null=True)
    ticker_ID = models.CharField(max_length=20,blank=True,null=True)
    what_is_the_idea_you_are_looking_to_implement=models.TextField(blank=True,null=True)
    why_do_you_think_that_the_idea_should_be_implemented=models.TextField(blank=True,null=True)
    was_this_idea_previously_executed_and_if_yes_state_the_method=models.TextField(blank=True,null=True)
    reasons_for_failure_of_previous_implementation_methods=models.TextField(blank=True,null=True)
    other_methods_of_implementation_that_you_would_suggest=models.TextField(blank=True,null=True)
    is_the_level_of_implementation_generic_or_specific=models.TextField(blank=True,null=True)
    deadline_by_which_you_need_the_idea_to_be_implemented=models.TextField(blank=True,null=True)
    
    class Meta:
        verbose_name = _("Script&Control - Permanent Form")
        verbose_name_plural = _("Script&Control - Permanent Forms")
    def __unicode__(self):
       return self.form_name

    
    #Strategy Forms - Temporary
class Strategy(models.Model):

      
    stagechoices = (
            ( 'start_up','Start up'),
            ( 'growing','Growing'),               
            ('matured','Matured' )
            )

    typecomp = (
              
             ('proprietary','Proprietary'), 
             ('partnership','Partnership'),
             ('llp','LLP'),
             ('private_ltd','Private Ltd'),
             ('limited','Limited'),
             ('privately_held','Private held'),
             ('publically_traded','Publically traded')
             )


    company_name=models.ForeignKey(Client,blank=True,null=True)
    project = models.ForeignKey(Project,blank=True)
    form_name=models.CharField(max_length=200,blank=True,null=True)
    upload_Doc1=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc2=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc3=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc4=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc5=models.FileField(upload_to="media",blank=True,null=True)
    version=models.IntegerField(blank=True,default=1)
    date=models.DateField(blank=True,null=True)
    please_select_the_growth_stage_of_your_company=models.CharField(max_length=30,choices=stagechoices,blank=True,null=True)
    please_tick_the_type_of_company=models.CharField(max_length=12,choices=typecomp,blank=True,null=True)
    stock_exchange=models.CharField(max_length=50,blank=True,null=True)
    ticker_ID = models.CharField(max_length=20,blank=True,null=True)
    business_strategies_that_are_already_deployed_in_your_company=models.TextField(blank=True,null=True)
    what_are_the_strategies_that_were_deployed_but_failed=models.TextField(blank=True,null=True)
    limitations_of_previous_strategies=models.TextField(blank=True,null=True)
    factors_to_be_considered_before_planning_new_strategies=models.TextField(blank=True,null=True)
    deadline_by_which_strategy_needs_to_be_deployed=models.TextField(blank=True,null=True)
    
    class Meta:
        verbose_name = _("Strategy - Temporary Form")
        verbose_name_plural = _("Strategy - Temporary Forms")
    
    def __unicode__(self):
       return self.form_name


    #Strategy Forms - Permanent
class Strategyp(models.Model):

      
    stagechoices = (
            ( 'start_up','Start up'),
            ( 'growing','Growing'),               
            ('matured','Matured' )
            )

    typecomp = (
              
             ('proprietary','Proprietary'), 
             ('partnership','Partnership'),
             ('llp','LLP'),
             ('private_ltd','Private Ltd'),
             ('limited','Limited'),
             ('privately_held','Private held'),
             ('publically_traded','Publically traded')
             )


    company_name=models.ForeignKey(Client,blank=True,null=True)
    project = models.ForeignKey(Project,blank=True)
    form_name=models.CharField(max_length=200,blank=True,null=True)
    upload_Doc1=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc2=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc3=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc4=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc5=models.FileField(upload_to="media",blank=True,null=True)
    version=models.IntegerField(blank=True,default=1)
    date=models.DateField(blank=True,null=True)
    please_select_the_growth_stage_of_your_company=models.CharField(max_length=30,choices=stagechoices,blank=True,null=True)
    please_tick_the_type_of_company=models.CharField(max_length=12,choices=typecomp,blank=True,null=True)
    stock_exchange=models.CharField(max_length=50,blank=True,null=True)
    ticker_ID = models.CharField(max_length=20,blank=True,null=True)
    business_strategies_that_are_already_deployed_in_your_company=models.TextField(blank=True,null=True)
    what_are_the_strategies_that_were_deployed_but_failed=models.TextField(blank=True,null=True)
    limitations_of_previous_strategies=models.TextField(blank=True,null=True)
    factors_to_be_considered_before_planning_new_strategies=models.TextField(blank=True,null=True)
    deadline_by_which_strategy_needs_to_be_deployed=models.TextField(blank=True,null=True)
    
    class Meta:
        verbose_name = _("Strategy - Permanent Form")
        verbose_name_plural = _("Strategy - Permanent Forms")
    
    def __unicode__(self):
       return self.form_name
#Problem Solving - Temporary
class Problemsolving(models.Model):
    
    company_name=models.ForeignKey(Client,blank=True,null=True)
    project = models.ForeignKey(Project,blank=True)
    form_name=models.CharField(max_length=200,blank=True,null=True)
    upload_Doc1=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc2=models.FileField(upload_to="media",blank=True,null=True)
    version=models.IntegerField(blank=True,default=1)
    date=models.DateField(blank=True,null=True)
    what_is_the_issue_that_needs_to_be_addressed=models.TextField(blank=True,null=True)
    what_is_its_effect_on_the_company=models.TextField(blank=True,null=True)
    researches_that_have_been_done_on_the_possible_solutions=models.TextField(blank=True,null=True)
    what_are_the_solutions_that_have_already_been_tried=models.TextField(blank=True,null=True)
    what_are_the_solutions_that_failed_and_the_reasons_for_failure=models.TextField(blank=True,null=True)
    what_are_the_parameters_to_be_considered=models.TextField(blank=True,null=True)
    
    class Meta:
        verbose_name = _("Problem Solving - Temporary Form")
        verbose_name_plural = _("Problem Solving - Temporary Forms")
    
    def __unicode__(self):
       return self.form_name

    #problem solving - permanent
class Problemsolvingp(models.Model):
    
    company_name=models.ForeignKey(Client,blank=True,null=True)
    project = models.ForeignKey(Project,blank=True)
    form_name=models.CharField(max_length=200,blank=True,null=True)
    upload_Doc1=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc2=models.FileField(upload_to="media",blank=True,null=True)
    version=models.IntegerField(blank=True,default=1)
    date=models.DateField(blank=True,null=True)
    what_is_the_issue_that_needs_to_be_addressed=models.TextField(blank=True,null=True)
    what_is_its_effect_on_the_company=models.TextField(blank=True,null=True)
    researches_that_have_been_done_on_the_possible_solutions=models.TextField(blank=True,null=True)
    what_are_the_solutions_that_have_already_been_tried=models.TextField(blank=True,null=True)
    what_are_the_solutions_that_failed_and_the_reasons_for_failure=models.TextField(blank=True,null=True)
    what_are_the_parameters_to_be_considered=models.TextField(blank=True,null=True)
    
    class Meta:
        verbose_name = _("Problem Solving - Permanent Form")
        verbose_name_plural = _("Problem Solving - Permanent Forms")
    
    def __unicode__(self):
       return self.form_name
#digitalization - temporary
class Digitalization(models.Model):
    
    company_name=models.ForeignKey(Client,blank=True,null=True)
    project = models.ForeignKey(Project,blank=True)
    form_name=models.CharField(max_length=200,blank=True,null=True)
    upload_Doc1=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc2=models.FileField(upload_to="media",blank=True,null=True)
    version=models.IntegerField(blank=True,default=1)
    date=models.DateField(blank=True,null=True)
    what_are_the_departments_that_need_to_be_digitalized_and_why=models.TextField(blank=True,null=True)
    please_mention_if_they_are_new_or_preexisting_departments=models.TextField(blank=True,null=True)
    what_is_the_budget_allocated_for_the_digitlization_process=models.TextField(blank=True,null=True)
    the_priority_in_which_the_deaprtments_need_to_be_digitalized=models.TextField(blank=True,null=True)
    what_are_the_limitations_that_need_to_be_considered=models.TextField(blank=True,null=True)
    the_deadline_by_which_digitalization_needs_to_be_done=models.TextField(blank=True,null=True)
    
    class Meta:
        verbose_name = _("Digitalization - Temporary Form")
        verbose_name_plural = _("Digitalization - Temporary Forms")
    
    def __unicode__(self):
       return self.form_name
#digitalization - permanent
class Digitalizationp(models.Model):
    
    company_name=models.ForeignKey(Client,blank=True,null=True)
    project = models.ForeignKey(Project,blank=True)
    form_name=models.CharField(max_length=200,blank=True,null=True)
    upload_Doc1=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc2=models.FileField(upload_to="media",blank=True,null=True)
    version=models.IntegerField(blank=True,default=1)
    date=models.DateField(blank=True,null=True)
    what_are_the_departments_that_need_to_be_digitalized_and_why=models.TextField(blank=True,null=True)
    please_mention_if_they_are_new_or_preexisting_departments=models.TextField(blank=True,null=True)
    what_is_the_budget_allocated_for_the_digitlization_process=models.TextField(blank=True,null=True)
    the_priority_in_which_the_deaprtments_need_to_be_digitalized=models.TextField(blank=True,null=True)
    what_are_the_limitations_that_need_to_be_considered=models.TextField(blank=True,null=True)
    the_deadline_by_which_digitalization_needs_to_be_done=models.TextField(blank=True,null=True)
    
    class Meta:
        verbose_name = _("Digitalization - Permanent Form")
        verbose_name_plural = _("Digitalization - Permanent Forms")
    
    def __unicode__(self):
       return self.form_name
#minute of meeting - temporary
class Miom(models.Model):
    
    company_name=models.ForeignKey(Client,blank=True,null=True)
    project = models.ForeignKey(Project,blank=True)
    form_name=models.CharField(max_length=200,blank=True,null=True)
    upload_Doc1=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc2=models.FileField(upload_to="media",blank=True,null=True)
    version=models.IntegerField(blank=True,default=1)
    date=models.DateField(blank=True,null=True)
    meeting_description=models.TextField(blank=True,null=True)
    main_concerns=models.TextField(blank=True,null=True)
    restrictions=models.TextField(blank=True,null=True)
    plan_of_action_for_Pathscript=models.TextField(blank=True,null=True)
    plan_of_action_for_Client=models.TextField(blank=True,null=True)
    
    class Meta:
        verbose_name = _("Minute of Meeting - Temporary Form")
        verbose_name_plural = _("Minute of Meeting - Temporary Forms")
    
    def __unicode__(self):
       return self.form_name
#minute of meeting - permanent
class Miomp(models.Model):
    
    company_name=models.ForeignKey(Client,blank=True,null=True)
    project = models.ForeignKey(Project,blank=True)
    form_name=models.CharField(max_length=200,blank=True,null=True)
    upload_Doc1=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc2=models.FileField(upload_to="media",blank=True,null=True)
    version=models.IntegerField(blank=True,default=1)
    date=models.DateField(blank=True,null=True)
    company_name=models.ForeignKey(Client,blank=True,null=True)
    project = models.ForeignKey(Project,blank=True)
    form_name=models.CharField(max_length=200,blank=True,null=True)
    upload_Doc1=models.FileField(upload_to="media",blank=True,null=True)
    upload_Doc2=models.FileField(upload_to="media",blank=True,null=True)
    version=models.IntegerField(blank=True,default=1)
    date=models.DateField(blank=True,null=True)
    meeting_description=models.TextField(blank=True,null=True)
    main_concerns=models.TextField(blank=True,null=True)
    restrictions=models.TextField(blank=True,null=True)
    plan_of_action_for_Pathscript=models.TextField(blank=True,null=True)
    plan_of_action_for_Client=models.TextField(blank=True,null=True)
    
    class Meta:
        verbose_name = _("Minute of Meeting - Permanent Form")
        verbose_name_plural = _("Minute of Meeting - Permanent Forms")
    
    def __unicode__(self):
       return self.form_name
