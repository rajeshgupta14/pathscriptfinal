from django import forms
from consultantform.models import Relatedcompany,Article,Backgroundcheck,Backgroundcheckb, Problemsolving, Problemsolvingp, Digitalization, Digitalizationp, Miom, Miomp, Duediligence, Script, Strategy,Duediligencep, Scriptp, Strategyp, Branch,Subsidiary
from myapp.models import Project,Client,User,Product
from django.utils.translation import ugettext_lazy as _
class ArticleForm(forms.ModelForm):#kyc form
    founding_date=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    
    class Meta:
        model = Article
        fields = ('founding_date','headquarter_location',
                  'areas_served','no_of_employees','type_of_company','type_of_industry','type_of_activity','warehouse_addresses',
                  'factory_addresses','number_of_owners_and_officers','officers_and_roles',
                  'registered_address','telephone','email','website',
                  'services_opted','upload_Doc1','upload_Doc2','upload_Doc3','upload_Doc4','upload_Doc5','upload_Doc6','upload_Doc7','upload_Doc8','upload_Doc9','upload_Doc10','upload_Doc11','upload_Doc12','notes')
        labels = {
                'services_opted' : _('Services Opted (Hold Ctrl + select for alternate choices, Hold Shift + select for continuous choices)'),
                }
    def __init__(self,request,*args, **kwargs):
         super(ArticleForm, self).__init__(*args, **kwargs)
        
         
        # self.fields['company_name'].queryset = Client.objects.filter(
         #                               userid=request.user.id)
    
class BranchForm(forms.ModelForm):#branch form
    branch_founding_date=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    
    class Meta:
        model = Branch
        fields = (
                  'branch_name','branch_founding_date','branch_location',
                  'areas_served_by_branch','no_of_employees_in_branch','type_of_business_by_branch',
                  'number_of_owners_and_officers_in_branch','officers_and_roles_in_branch',
                  'branch_registered_address','branch_telephone','branch_email','branch_website','upload_Doc1','upload_Doc2','upload_Doc3','upload_Doc4','upload_Doc5')
    def __init__(self,request,*args, **kwargs):
         super(BranchForm, self).__init__(*args, **kwargs)
        
         
         #self.fields['company_name'].queryset = Client.objects.filter(
          #                              userid=request.user.id)
            
class SubsidiaryForm(forms.ModelForm):
    subsidiary_founding_date=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    
    class Meta:
        model = Subsidiary
        fields = (
                  'subsidiary_name','subsidiary_founding_date','subsidiary_location',
                  'areas_served_by_subsidiary','no_of_employees_in_subsidiary','type_of_business_by_subsidiary',
                  'subsidiary_warehouse_addresses','subsidiary_factory_addresses','number_of_owners_and_officers_in_subsidiary','officers_and_roles_in_subsidiary',
                  'subsidiary_registered_address','subsidiary_telephone','subsidiary_email','subsidiary_website','upload_Doc1','upload_Doc2','upload_Doc3','upload_Doc4','upload_Doc5')
    def __init__(self,request,*args, **kwargs):
         super(SubsidiaryForm, self).__init__(*args, **kwargs)
        
         
         #self.fields['company_name'].queryset = Client.objects.filter(
          #                              userid=request.user.id)


class RelatedcompanyForm(forms.ModelForm):
    
    class Meta:
        model = Relatedcompany
        fields = (
                  'related_company_name','relation','related_company_registered_address','related_company_telephone','related_company_email','related_company_website','upload_Doc1','upload_Doc2','upload_Doc3','upload_Doc4','upload_Doc5','upload_Doc6','upload_Doc7')
    def __init__(self,request,*args, **kwargs):
         super(RelatedcompanyForm, self).__init__(*args, **kwargs)
        
         
         #self.fields['company_name'].queryset = Client.objects.filter(
          #                              userid=request.user.id)
    
class BackgroundcheckForm(forms.ModelForm):
    
    class Meta:
        model = Backgroundcheck
        fields = ('c1','rOC_Certificates','c2','mOA','c3',
                  'current_List_of_Directors_including_Photo_ID','c4',
                  'term_Sheets','c5','current_Bankers_and_Auditors_and_Company_Secretary','c6',
                  'sales_Tax_Registration_Certificate','c7','last_Filed_Sales_Tax_Certificate','c8',
                  'municipal_Certificate','c9','last_2_years_Audited_Books_of_Accounts','c10',
                  'last_Paid_Tax_Receipt','c11','employee_List_Statement','c12',
                  'last_Provident_Fund_Receipt','c13','list_of_Competitors')
    
        labels = {
            'company_name': _('Company Name'),
            'c1': _('Currently with'),
            'rOC_Certificates': _('ROC Certificates'),
            'c2': _('Currently with'),
            'mOA': _('MOA'),
            'c3': _('Currently with'),
            'current_List_of_Directors_including_Photo_ID': _('Current List of Directors including Photo ID'),
            'c4': _('Currently with'),
            'term_Sheets': _('Term Sheets'),
            'c5': _('Currently with'),
            'current_Bankers_and_Auditors_and_Company_Secretary': _('Current Bankers, Auditors and Company Secretary'),
            'c6': _('Currently with'),
            'sales_Tax_Registration_Certificate': _('Sales Tax Registration Certificate'),
            'c7': _('Currently with'),
            'last_Filed_Sales_Tax_Certificate': _('Last Filed Sales Tax Certificate'),
            'c8': _('Currently with'),
            'municipal_Certificate': _('Municipal Certificate'),
            'c9': _('Currently with'),
            'last_2_years_Audited_Books_of_Accounts': _('Last 2 years Audited Books of Accounts'),
            'c10': _('Currently with'),
            'last_Paid_Tax_Receipt': _('Last Paid Tax Receipt'),
            'c11': _('Currently with'),
            'employee_List_Statement': _('Employee List Statement'),
            'c12': _('Currently with'),
            'last_Provident_Fund_Receipt': _('last Provident Fund Receipt'),
            'c13': _('Currently with'),
            'list_of_Competitors': _('List of Competitors'),
            
                    
            
            
            
                 }
                   
    
    
    
    def __init__(self,request,*args, **kwargs):
         super(BackgroundcheckForm, self).__init__(*args, **kwargs)
        
         
         #self.fields['company_name'].queryset = Client.objects.filter(userid=request.user.id)
         self.fields['c1'].queryset = User.objects.filter(is_staff=True)
         self.fields['c2'].queryset = User.objects.filter(is_staff=True)
         self.fields['c3'].queryset = User.objects.filter(is_staff=True)
         self.fields['c4'].queryset = User.objects.filter(is_staff=True)
         self.fields['c5'].queryset = User.objects.filter(is_staff=True)
         self.fields['c6'].queryset = User.objects.filter(is_staff=True)
         self.fields['c7'].queryset = User.objects.filter(is_staff=True)
         self.fields['c8'].queryset = User.objects.filter(is_staff=True)
         self.fields['c9'].queryset = User.objects.filter(is_staff=True)
         self.fields['c10'].queryset = User.objects.filter(is_staff=True)
         self.fields['c11'].queryset = User.objects.filter(is_staff=True)
         self.fields['c12'].queryset = User.objects.filter(is_staff=True)
         self.fields['c13'].queryset = User.objects.filter(is_staff=True)
        
class BackgroundcheckbForm(forms.ModelForm):
    
    class Meta:
        model = Backgroundcheckb
        fields = ('c1','rOC_Certificates','c2','mOA','c3',
                  'current_List_of_Directors_including_Photo_ID','c4',
                  'term_Sheets','c5','current_Bankers_and_Auditors_and_Company_Secretary','c6',
                  'sales_Tax_Registration_Certificate','c7','last_Filed_Sales_Tax_Certificate','c8',
                  'municipal_Certificate','c9','last_2_years_Audited_Books_of_Accounts','c10',
                  'last_Paid_Tax_Receipt','c11','employee_List_Statement','c12',
                  'last_Provident_Fund_Receipt','c13','list_of_Competitors')
    
        # self.fields['company_name'].queryset = Client.objects.filter(id=User.objects.get(clientid=request.user.clientid).clientid)
    
class ProjectForm(forms.ModelForm):#create, view project form
    
    class Meta:
        model = Project
        fields=('name','client','product','user')
        
    def __init__(self,request,*args, **kwargs):
         super(ProjectForm, self).__init__(*args, **kwargs)
        
         self.fields['client'].queryset = Client.objects.filter(
                                        userid=request.user.id)
        
class ProductForm(forms.ModelForm):#create , view product form
    
    class Meta:
        model = Product
        fields=('name','description','upload_Doc1','upload_Doc2')
        
    def __init__(self,request,*args, **kwargs):
         super(ProductForm, self).__init__(*args, **kwargs)
        
         
        
        


class CustomerForm(forms.ModelForm):#kyc form in client view
    
    class Meta:
        model = Article
        fields = ('founding_date','headquarter_location',
                  'areas_served','no_of_employees','type_of_company','type_of_industry','type_of_activity','warehouse_addresses',
                  'factory_addresses','number_of_owners_and_officers','officers_and_roles',
                  'registered_address','telephone','email','website','upload_Doc1','upload_Doc2','upload_Doc3','upload_Doc4','upload_Doc5','upload_Doc6','upload_Doc7','upload_Doc8','upload_Doc9','upload_Doc10','upload_Doc11','upload_Doc12')
        
    def __init__(self,request,*args, **kwargs):
         super(CustomerForm, self).__init__(*args, **kwargs)
        
         
         #self.fields['company_name'].queryset = Client.objects.filter(
                  #                      userid=request.user.id)
    
class DuediligencetForm(forms.ModelForm):#duediligence create form
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    
    class Meta:
        model = Duediligence
        fields = ('date','version',
                  'please_select_the_growth_stage_of_your_company','please_tick_the_type_of_company',
                  'stock_exchange','ticker_ID','what_is_the_key_need_you_are_providing_for_your_customer',
                  'evidences_that_show_need_stated_above_for_customer_is_fulfilled',
                  'what_are_some_of_the_aspects_you_are_facing_a_challenge_with','upload_Doc1','upload_Doc2')
        
    def __init__(self,request,*args, **kwargs):
         super(DuediligencetForm, self).__init__(*args, **kwargs)
        
        
class DuediligenceForm(forms.ModelForm):#duediligence temporary form
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    
    class Meta:
        model = Duediligence
        fields = ('date',
                  'please_select_the_growth_stage_of_your_company','please_tick_the_type_of_company',
                  'stock_exchange','ticker_ID','what_is_the_key_need_you_are_providing_for_your_customer',
                  'evidences_that_show_need_stated_above_for_customer_is_fulfilled',
                  'what_are_some_of_the_aspects_you_are_facing_a_challenge_with','upload_Doc1','upload_Doc2')
        
    def __init__(self,request,*args, **kwargs):
         super(DuediligenceForm, self).__init__(*args, **kwargs)
        
         
         #self.fields['project'].queryset = Project.objects.filter(
                                        #user=request.user.id)



class DuediligencepForm(forms.ModelForm):#duediligence permanent 
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    
    class Meta:
        model = Duediligencep
        fields = ('date',
                  'please_select_the_growth_stage_of_your_company','please_tick_the_type_of_company',
                  'stock_exchange','ticker_ID','what_is_the_key_need_you_are_providing_for_your_customer',
                  'evidences_that_show_need_stated_above_for_customer_is_fulfilled',
                  'what_are_some_of_the_aspects_you_are_facing_a_challenge_with','upload_Doc1','upload_Doc2')
        
    def __init__(self,request,*args, **kwargs):
         super(DuediligencepForm, self).__init__(*args, **kwargs)
        
         
         #self.fields['project'].queryset = Project.objects.filter(
                                        #user=request.user.id)


class ScripttForm(forms.ModelForm):#script create form
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    
    class Meta:
        model = Script
        fields = ('date','version',
                  'please_select_the_growth_stage_of_your_company','please_tick_the_type_of_company',
                  'stock_exchange','ticker_ID','what_is_the_idea_you_are_looking_to_implement',
                  'why_do_you_think_that_the_idea_should_be_implemented','was_this_idea_previously_executed_and_if_yes_state_the_method',
                  'reasons_for_failure_of_previous_implementation_methods','other_methods_of_implementation_that_you_would_suggest',
                  'is_the_level_of_implementation_generic_or_specific','deadline_by_which_you_need_the_idea_to_be_implemented','upload_Doc1','upload_Doc2')

    def __init__(self,request,*args, **kwargs):
         super(ScripttForm, self).__init__(*args, **kwargs)
        
         
         #self.fields['project'].queryset = Project.objects.filter(
          #                              user=request.user.id)
        
class ScriptForm(forms.ModelForm):#script temporary
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    
    class Meta:
        model = Script
        fields = ('date',
                  'please_select_the_growth_stage_of_your_company','please_tick_the_type_of_company',
                  'stock_exchange','ticker_ID','what_is_the_idea_you_are_looking_to_implement',
                  'why_do_you_think_that_the_idea_should_be_implemented','was_this_idea_previously_executed_and_if_yes_state_the_method',
                  'reasons_for_failure_of_previous_implementation_methods','other_methods_of_implementation_that_you_would_suggest',
                  'is_the_level_of_implementation_generic_or_specific','deadline_by_which_you_need_the_idea_to_be_implemented','upload_Doc1','upload_Doc2')

    def __init__(self,request,*args, **kwargs):
         super(ScriptForm, self).__init__(*args, **kwargs)
        
         
         #self.fields['project'].queryset = Project.objects.filter(
          #                              user=request.user.id)
    
class ScriptpForm(forms.ModelForm):#script permanent
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    
    class Meta:
        model = Scriptp
        fields = ('date',
                  'please_select_the_growth_stage_of_your_company','please_tick_the_type_of_company',
                  'stock_exchange','ticker_ID','what_is_the_idea_you_are_looking_to_implement',
                  'why_do_you_think_that_the_idea_should_be_implemented','was_this_idea_previously_executed_and_if_yes_state_the_method',
                  'reasons_for_failure_of_previous_implementation_methods','other_methods_of_implementation_that_you_would_suggest',
                  'is_the_level_of_implementation_generic_or_specific','deadline_by_which_you_need_the_idea_to_be_implemented','upload_Doc1','upload_Doc2')

    def __init__(self,request,*args, **kwargs):
         super(ScriptpForm, self).__init__(*args, **kwargs)
        
         
         #self.fields['project'].queryset = Project.objects.filter(
          #                              user=request.user.id)
    

class StrategytForm(forms.ModelForm):#strategy create
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    
    class Meta:
        model = Strategy
        fields = ('date','version',
                  'please_select_the_growth_stage_of_your_company','please_tick_the_type_of_company',
                  'stock_exchange','ticker_ID','business_strategies_that_are_already_deployed_in_your_company',
                  'what_are_the_strategies_that_were_deployed_but_failed','limitations_of_previous_strategies',
                  'factors_to_be_considered_before_planning_new_strategies','deadline_by_which_strategy_needs_to_be_deployed','upload_Doc1','upload_Doc2','upload_Doc3','upload_Doc4','upload_Doc5')
        
    def __init__(self,request,*args, **kwargs):
         super(StrategytForm, self).__init__(*args, **kwargs)
        
         
         #self.fields['project'].queryset = Project.objects.filter(
          #                              user=request.user.id)
    
class StrategyForm(forms.ModelForm):#strategy temporary
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    
    class Meta:
        model = Strategy
        fields = ('date',
                  'please_select_the_growth_stage_of_your_company','please_tick_the_type_of_company',
                  'stock_exchange','ticker_ID','business_strategies_that_are_already_deployed_in_your_company',
                  'what_are_the_strategies_that_were_deployed_but_failed','limitations_of_previous_strategies',
                  'factors_to_be_considered_before_planning_new_strategies','deadline_by_which_strategy_needs_to_be_deployed','upload_Doc1','upload_Doc2','upload_Doc3','upload_Doc4','upload_Doc5')
        
    def __init__(self,request,*args, **kwargs):
         super(StrategyForm, self).__init__(*args, **kwargs)
        
         
        # self.fields['project'].queryset = Project.objects.filter(
         #                               user=request.user.id)
    
        
        

class StrategypForm(forms.ModelForm):#strategy permanent
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    
    class Meta:
        model = Strategyp
        fields = ('date',
                  'please_select_the_growth_stage_of_your_company','please_tick_the_type_of_company',
                  'stock_exchange','ticker_ID','business_strategies_that_are_already_deployed_in_your_company',
                  'what_are_the_strategies_that_were_deployed_but_failed','limitations_of_previous_strategies',
                  'factors_to_be_considered_before_planning_new_strategies','deadline_by_which_strategy_needs_to_be_deployed','upload_Doc1','upload_Doc2','upload_Doc3','upload_Doc4','upload_Doc5')
        
        
    
    def __init__(self,request,*args, **kwargs):
         super(StrategypForm, self).__init__(*args, **kwargs)
        
         
         #self.fields['project'].queryset = Project.objects.filter(
          #                              user=request.user.id)
    
class ProblemSolvingtForm(forms.ModelForm):#problem solving create
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    
    class Meta:
        model = Problemsolving
        fields = ('date','version',
                  'what_is_the_issue_that_needs_to_be_addressed','what_is_its_effect_on_the_company',
                  'researches_that_have_been_done_on_the_possible_solutions','what_are_the_solutions_that_have_already_been_tried',
                  'what_are_the_solutions_that_failed_and_the_reasons_for_failure','what_are_the_parameters_to_be_considered','upload_Doc1','upload_Doc2')
    def __init__(self,request,*args, **kwargs):
         super(ProblemSolvingtForm, self).__init__(*args, **kwargs)

class ProblemSolvingForm(forms.ModelForm):#problem solving temporary
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
     
    class Meta:
        model = Problemsolving
        fields = ('date',
                  'what_is_the_issue_that_needs_to_be_addressed','what_is_its_effect_on_the_company',
                  'researches_that_have_been_done_on_the_possible_solutions','what_are_the_solutions_that_have_already_been_tried',
                  'what_are_the_solutions_that_failed_and_the_reasons_for_failure','what_are_the_parameters_to_be_considered','upload_Doc1','upload_Doc2')
    def __init__(self,request,*args, **kwargs):
         super(ProblemSolvingForm, self).__init__(*args, **kwargs)
                
class ProblemSolvingpForm(forms.ModelForm):#problem solving permanent
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    
    class Meta:
        model = Problemsolvingp
        fields = ('date',
                  'what_is_the_issue_that_needs_to_be_addressed','what_is_its_effect_on_the_company',
                  'researches_that_have_been_done_on_the_possible_solutions','what_are_the_solutions_that_have_already_been_tried',
                  'what_are_the_solutions_that_failed_and_the_reasons_for_failure','what_are_the_parameters_to_be_considered','upload_Doc1','upload_Doc2')
    def __init__(self,request,*args, **kwargs):
         super(ProblemSolvingpForm, self).__init__(*args, **kwargs)
         
         
         
class DigitalizationtForm(forms.ModelForm):#digitalization create
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    
    class Meta:
        model = Digitalization
        fields = ('date','version',
                  'what_are_the_departments_that_need_to_be_digitalized_and_why',
                  'please_mention_if_they_are_new_or_preexisting_departments',
                  'what_is_the_budget_allocated_for_the_digitlization_process',
                  'the_priority_in_which_the_deaprtments_need_to_be_digitalized',
                  'what_are_the_limitations_that_need_to_be_considered','the_deadline_by_which_digitalization_needs_to_be_done','upload_Doc1','upload_Doc2')
    def __init__(self,request,*args, **kwargs):
         super(DigitalizationtForm, self).__init__(*args, **kwargs)


class DigitalizationForm(forms.ModelForm):#digitalization temporary
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    
    class Meta:
        model = Digitalization
        fields = ('date',
                  'what_are_the_departments_that_need_to_be_digitalized_and_why',
                  'please_mention_if_they_are_new_or_preexisting_departments',
                  'what_is_the_budget_allocated_for_the_digitlization_process',
                  'the_priority_in_which_the_deaprtments_need_to_be_digitalized',
                  'what_are_the_limitations_that_need_to_be_considered','the_deadline_by_which_digitalization_needs_to_be_done','upload_Doc1','upload_Doc2')
    def __init__(self,request,*args, **kwargs):
         super(DigitalizationForm, self).__init__(*args, **kwargs)

class DigitalizationpForm(forms.ModelForm):#digitalization permanent
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    
    class Meta:
        model = Digitalizationp
        fields = ('date',
                  'what_are_the_departments_that_need_to_be_digitalized_and_why',
                  'please_mention_if_they_are_new_or_preexisting_departments',
                  'what_is_the_budget_allocated_for_the_digitlization_process',
                  'the_priority_in_which_the_deaprtments_need_to_be_digitalized',
                  'what_are_the_limitations_that_need_to_be_considered','the_deadline_by_which_digitalization_needs_to_be_done','upload_Doc1','upload_Doc2')
    def __init__(self,request,*args, **kwargs):
         super(DigitalizationpForm, self).__init__(*args, **kwargs)


class MiomtForm(forms.ModelForm):#min of meeting create
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    
    class Meta:
        model = Miom
        fields = ('date','version',
                  'meeting_description','main_concerns','restrictions',
                  'plan_of_action_for_Pathscript','plan_of_action_for_Client',
                  'upload_Doc1','upload_Doc2')
    def __init__(self,request,*args, **kwargs):
         super(MiomtForm, self).__init__(*args, **kwargs)


class MiomForm(forms.ModelForm):#min of meeting temporary
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    
    class Meta:
        model = Miom
        fields = ('date',
                  'meeting_description','main_concerns','restrictions',
                  'plan_of_action_for_Pathscript','plan_of_action_for_Client',
                  'upload_Doc1','upload_Doc2')
    def __init__(self,request,*args, **kwargs):
         super(MiomForm, self).__init__(*args, **kwargs)

class MiompForm(forms.ModelForm):#min of meeting permanent
    date=forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    
    class Meta:
        model = Miomp
        fields = ('date',
                  'meeting_description','main_concerns','restrictions',
                  'plan_of_action_for_Pathscript','plan_of_action_for_Client',
                  'upload_Doc1','upload_Doc2')
    def __init__(self,request,*args, **kwargs):
         super(MiompForm, self).__init__(*args, **kwargs)
