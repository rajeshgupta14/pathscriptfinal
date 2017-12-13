from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from consultantform.forms import ProductForm,ArticleForm,BranchForm,SubsidiaryForm,RelatedcompanyForm,ProblemSolvingForm,ProblemSolvingtForm,ProblemSolvingpForm, DigitalizationForm, DigitalizationtForm, DigitalizationpForm, MiomtForm, MiomForm,MiompForm,CustomerForm,ProjectForm,BackgroundcheckForm,BackgroundcheckbForm,DuediligenceForm,DuediligencetForm,ScriptForm,ScripttForm,StrategyForm,StrategytForm,DuediligencepForm,ScriptpForm,StrategypForm
from consultantform.models import Article,Product,Branch,Subsidiary,Relatedcompany,Problemsolving,Problemsolvingp,Backgroundcheck,Duediligence,Script,Strategy,Duediligencep,Scriptp,Strategyp,Digitalization,Digitalizationp,Miom,Miomp
from myapp.models import Client,Project
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def consultantformss(request,a_id=1):#consultant side - common forms such as kyc, bg check and project forms view
    curr=request.user
    return render(request,'consultantforms.html',
                              {'user':request.user,'prforms':Product.objects.all(),'relforms':Relatedcompany.objects.filter(company_name=a_id),'subforms':Subsidiary.objects.filter(company_name=a_id),'branchforms':Branch.objects.filter(company_name=a_id),'checkforms':Backgroundcheck.objects.filter(company_name=a_id),'consultantforms':Article.objects.filter(company_name=a_id),'a':Client.objects.get(id=a_id),'projects':Project.objects.filter(client=a_id,user=curr.id)})
    
@login_required
def finalformss(request,a_id=1):#client side - common forms such as kyc, bg check and project forms view
    curr=request.user
    return render(request,'finalforms.html',
                              {'user':request.user,'checkforms':Backgroundcheck.objects.filter(company_name=a_id),'forms':Article.objects.filter(company_name=a_id),'a':Client.objects.get(id=a_id),'projects':Project.objects.filter(client=a_id,user=curr.id),'prforms':Product.objects.all(),'relforms':Relatedcompany.objects.filter(company_name=a_id),'subforms':Subsidiary.objects.filter(company_name=a_id),'branchforms':Branch.objects.filter(company_name=a_id)})    
    
    
@login_required   
def consultantform(request,a_id=1,consultantform_id=1):#view created kyc form 
 
    
    consultantform = Article.objects.get(id=consultantform_id)
    form=ArticleForm(request,instance=consultantform)
    
    return render(request,'consultantform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'consultantform' : Article.objects.get(id=consultantform_id)})

@login_required   
def branchform(request,a_id=1,consultantform_id=1):#view created branch form
 
    
    consultantform = Branch.objects.get(id=consultantform_id)
    form=BranchForm(request,instance=consultantform)
    if request.user.is_staff:
     return render(request,'branchform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'consultantform' : Branch.objects.get(id=consultantform_id)})
    else:
     return render(request,'branchcform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'consultantform' : Branch.objects.get(id=consultantform_id)})

@login_required   
def subsidiaryform(request,a_id=1,consultantform_id=1):#view created subsidiary form
 
    
    consultantform = Subsidiary.objects.get(id=consultantform_id)
    form=SubsidiaryForm(request,instance=consultantform)
    if request.user.is_staff:
     return render(request,'subsidiaryform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'consultantform' : Subsidiary.objects.get(id=consultantform_id)})
    else:
     return render(request,'subsidiarycform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'consultantform' : Subsidiary.objects.get(id=consultantform_id)})
        
@login_required   
def relatedform(request,a_id=1,consultantform_id=1):#view created related company form
 
    
    consultantform = Relatedcompany.objects.get(id=consultantform_id)
    form=RelatedcompanyForm(request,instance=consultantform)
    if request.user.is_staff:
     return render(request,'relatedform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'consultantform' : Relatedcompany.objects.get(id=consultantform_id)})
    else:
     return render(request,'relatedcform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'consultantform' : Relatedcompany.objects.get(id=consultantform_id)})



@login_required   
def productform(request,a_id=1,consultantform_id=1):#view products created by admin
 
    
    consultantform = Product.objects.get(id=consultantform_id)
    form=ProductForm(request,instance=consultantform)
    if request.user.is_staff:
     return render(request,'productform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'consultantform' : Product.objects.get(id=consultantform_id)})
    else:
     return render(request,'productcform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'consultantform' : Product.objects.get(id=consultantform_id)})
      
@login_required   
def checklistform(request,a_id=1,checklistform_id=1):#view created checklist
 
    curr=request.user
    checkform = Backgroundcheck.objects.get(id=checklistform_id)
    form=BackgroundcheckForm(request,instance=checkform)
    #form1=BackgroundcheckcForm(request,instance=checkform)
    if curr.is_staff:
     return render(request,'checklistform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'checklistform':Backgroundcheck.objects.get(id=checklistform_id)})
    else:
     return render(request,'customerchecklistform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'checklistform':Backgroundcheck.objects.get(id=checklistform_id)})


@login_required   
def projectform(request,a_id=1,projectform_id=1):#view project form - consultant and client side
 
    curr=request.user
    projectform = Project.objects.get(id=projectform_id)
    form=ProjectForm(request,instance=projectform)
    if curr.is_staff:
     return render(request,'projectform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'projectform':Project.objects.get(id=projectform_id)})
    else:
     return render(request,'customerprojectform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'projectform':Project.objects.get(id=projectform_id)})








@login_required   
def finalform(request,a_id=1,form_id=1):#view kyc form -client side
        
    
    consultantform = Article.objects.get(id=form_id)
    form=CustomerForm(request,instance=consultantform)
    
    return render(request,'finalform.html',{'user':request.user,'consultantform' : Article.objects.get(id=form_id),'form':form,'a':Client.objects.get(id=a_id)})

#@login_required   
#def customerchecklistform(request,a_id=1,checklistform_id=1):
 
    
    #checkform = Backgroundcheck.objects.get(id=checklistform_id)
    #form=BackgroundcheckForm(instance=checkform)
    
    #return render(request,'customerchecklistform.html',{'form':form,'a':Client.objects.get(id=a_id)})

@login_required
def serviceforms(request,a_id=1,serviceform_id=1):#view service forms - consultant and client side
    curr = request.user
    if curr.is_staff:
        return render(request,'serviceforms.html',
                              {'user':request.user,'dueforms':Duediligence.objects.filter(project=serviceform_id),'duepforms':Duediligencep.objects.filter(project=serviceform_id),'scriptforms':Script.objects.filter(project=serviceform_id),'scriptpforms':Scriptp.objects.filter(project=serviceform_id),'project':Project.objects.get(id=serviceform_id),'a':Client.objects.get(id=a_id),'pstrategies':Strategyp.objects.filter(project=serviceform_id),'strategies':Strategy.objects.filter(project=serviceform_id),'pspforms':Problemsolvingp.objects.filter(project=serviceform_id),'digipforms':Digitalizationp.objects.filter(project=serviceform_id),'miompforms':Miomp.objects.filter(project=serviceform_id),'psforms':Problemsolving.objects.filter(project=serviceform_id),'digiforms':Digitalization.objects.filter(project=serviceform_id),'miomforms':Miom.objects.filter(project=serviceform_id)})
    else:
        return render(request,'cserviceforms.html',
                              {'user':request.user,'dueforms':Duediligencep.objects.filter(project=serviceform_id),'scriptforms':Scriptp.objects.filter(project=serviceform_id),'project':Project.objects.get(id=serviceform_id),'a':Client.objects.get(id=a_id),'strategies':Strategyp.objects.filter(project=serviceform_id),'psforms':Problemsolvingp.objects.filter(project=serviceform_id),'digiforms':Digitalizationp.objects.filter(project=serviceform_id),'miomforms':Miomp.objects.filter(project=serviceform_id)})











@login_required   
def create(request,a_id=1):#create kyc form
    if request.POST:
        
        
        form= ArticleForm(request,request.POST,request.FILES)
        if form.is_valid():
            torr1=form.save()
            torr1.company_name=Client.objects.get(id=a_id)#changed
            a=Article.objects.filter(company_name=Client.objects.get(id=a_id))
            if a.count() >= 1:
             torr1.version=a.count()
            torr1.save()
            
            url=reverse('consultantformss',kwargs={'a_id':a_id})
            return HttpResponseRedirect(url)
    else:
        form = ArticleForm(request)
        
    return render(request,'create_form.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id)})

@login_required   
def create1(request,a_id=1):#create branch form
    if request.POST:
        
        
        form= BranchForm(request,request.POST,request.FILES)
        if form.is_valid():
            torr1=form.save(commit=False)
            torr1.company_name=Client.objects.get(id=a_id)
            torr1.save()
            url=reverse('consultantformss',kwargs={'a_id':a_id})
            return HttpResponseRedirect(url)
    else:
        form = BranchForm(request)
        
    return render(request,'createbranch.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id)})

@login_required   
def create2(request,a_id=1):#create subsidiary form
    if request.POST:
        
        
        form= SubsidiaryForm(request,request.POST,request.FILES)
        if form.is_valid():
            torr1=form.save(commit=False)
            torr1.company_name=Client.objects.get(id=a_id)
            torr1.save()
            
            url=reverse('consultantformss',kwargs={'a_id':a_id})
            return HttpResponseRedirect(url)
    else:
        form = SubsidiaryForm(request)
        
    return render(request,'createsub.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id)})

@login_required   
def create3(request,a_id=1):#create related company form
    if request.POST:
        
        
        form= RelatedcompanyForm(request,request.POST,request.FILES)
        if form.is_valid():
            torr1=form.save(commit=False)
            torr1.company_name=Client.objects.get(id=a_id)
            torr1.save()
            
            url=reverse('consultantformss',kwargs={'a_id':a_id})
            return HttpResponseRedirect(url)
    else:
        form = RelatedcompanyForm(request)
        
    return render(request,'createrel.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id)})

@login_required   
def checklist(request,a_id=1):#create bgchecklist and also creates a bgcheck log
    if request.POST:
        form= BackgroundcheckForm(request,request.POST)
        form1=BackgroundcheckbForm(request.POST)
        if form.is_valid():
            torr1=form.save()
            #torr1=form.save(commit=False)
            torr1.company_name=Client.objects.get(id=a_id)
            #torr1.save()
            
            torr1.version=Backgroundcheck.objects.filter(company_name=Client.objects.get(id=a_id)).count()+1
            torr1.form_name="BG"+str(torr1.version)
            torm1=form1.save(commit=False)
            torm1.user=request.user.username
            torm1.version=torr1.version
            torm1.company_name=Client.objects.get(id=a_id)
            torm1.form_name=torr1.form_name
            torm1.save()
            torr1.save()
            
            url=reverse('consultantformss',kwargs={'a_id':a_id})
            return HttpResponseRedirect(url)
    else:
        form = BackgroundcheckForm(request)
        
    
    return render(request,'createchecklist.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id)})

@login_required
def projects(request,a_id=1):#create project
    if request.POST:
        form= ProjectForm(request,request.POST)
        if form.is_valid():
            form.save()
            #torr1.client=Client.objects.get(id=a_id)
            #torr1.save()
            
            url=reverse('consultantformss',kwargs={'a_id':a_id})
            return HttpResponseRedirect(url)
    else:
        form = ProjectForm(request)
    
    return render(request,'projects.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id)})


@login_required   
def created(request,a_id=1,project_id=1):#create duediligence form
    
    
    
    if request.POST:
        
        
        form= DuediligencetForm(request,request.POST,request.FILES)
        
        project=Project.objects.get(id=project_id)
        
        if form.is_valid():
            torr1=form.save(commit=False)
            torr1.project=project
            torr1.company_name=Client.objects.get(id=a_id)
            torr1.form_name="DDF"+str(project.id)+"."+str(torr1.version)
            torr1.save()
                     
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url)
    else:
        form = DuediligenceForm(request)
        
    return render(request,'create_due.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'project':Project.objects.get(id=project_id)})

@login_required   
def createps(request,a_id=1,project_id=1):#create problem solving form
    
    
    
    if request.POST:
        
        
        form= ProblemSolvingtForm(request,request.POST,request.FILES)
        
        project=Project.objects.get(id=project_id)
        
        if form.is_valid():
            torr1=form.save(commit=False)
            torr1.project=project
            torr1.company_name=Client.objects.get(id=a_id)
            torr1.form_name="PS"+str(project.id)+"."+str(torr1.version)
            torr1.save()
                     
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url)
    else:
        form = ProblemSolvingForm(request)
        
    return render(request,'create_ps.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'project':Project.objects.get(id=project_id)})

@login_required   
def createdigi(request,a_id=1,project_id=1):#create digitalization form
    
    
    
    if request.POST:
        
        
        form= DigitalizationtForm(request,request.POST,request.FILES)
        
        project=Project.objects.get(id=project_id)
        
        if form.is_valid():
            torr1=form.save(commit=False)
            torr1.project=project
            torr1.company_name=Client.objects.get(id=a_id)
            torr1.form_name="DIGI"+str(project.id)+"."+str(torr1.version)
            torr1.save()
                     
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url)
    else:
        form = DigitalizationForm(request)
        
    return render(request,'create_digi.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'project':Project.objects.get(id=project_id)})

@login_required   
def createmiom(request,a_id=1,project_id=1):#create min of meeting form
    
    
    
    if request.POST:
        
        
        form= MiomtForm(request,request.POST,request.FILES)
        
        project=Project.objects.get(id=project_id)
        
        if form.is_valid():
            torr1=form.save(commit=False)
            torr1.project=project
            torr1.company_name=Client.objects.get(id=a_id)
            torr1.form_name="MIOM"+str(project.id)+"."+str(torr1.version)
            torr1.save()
                     
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url)
    else:
        form = MiomForm(request)
        
    return render(request,'create_miom.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'project':Project.objects.get(id=project_id)})



@login_required   
def createsc(request,a_id=1,project_id=1):#create script form
    if request.POST:
        form= ScripttForm(request,request.POST,request.FILES)
        project=Project.objects.get(id=project_id)
        
        if form.is_valid():
            torr1=form.save(commit=False)
            torr1.project=project
            torr1.company_name=Client.objects.get(id=a_id)
            torr1.form_name="SC"+str(project.id)+"."+str(torr1.version)
            torr1.save()    
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url)
    else:
        form = ScriptForm(request)
        
    return render(request,'create_script.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'project':Project.objects.get(id=project_id)})


@login_required   
def createst(request,a_id=1,project_id=1):#create strategy form
    if request.POST:
        form= StrategytForm(request,request.POST,request.FILES)
        project=Project.objects.get(id=project_id)
        
        if form.is_valid():
            torr1=form.save(commit=False)
            torr1.project=project
            torr1.company_name=Client.objects.get(id=a_id)
            n=torr1.version
            torr1.form_name="ST"+str(project.id)+"."+str(n)
            torr1.save()    
            
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url)
    else:
        form = StrategyForm(request)
        
    return render(request,'create_strat.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'project':Project.objects.get(id=project_id)})




@login_required   
def ram(request,consultantform_id=1):#edit and save kyc form
    if request.method == 'POST':
        consultantform = Article.objects.get(id=consultantform_id)
        client= Client.objects.get(clientname=consultantform.company_name)
        form= ArticleForm(request,request.POST,request.FILES,instance=consultantform)
        if form.is_valid():
            form.save()
                        
            url=reverse('consultantformss',kwargs={'a_id':client.id})
            return HttpResponseRedirect(url)
        
@login_required   
def ram1(request,consultantform_id=1):#edit and save branch form
    if request.method == 'POST':
        consultantform = Branch.objects.get(id=consultantform_id)
        client= Client.objects.get(clientname=consultantform.company_name)
        form= BranchForm(request,request.POST,request.FILES,instance=consultantform)
        if form.is_valid():
            form.save()
                        
            url=reverse('consultantformss',kwargs={'a_id':client.id})
            return HttpResponseRedirect(url)

@login_required   
def ram2(request,consultantform_id=1):#edit and save subsidiary form
    if request.method == 'POST':
        consultantform = Subsidiary.objects.get(id=consultantform_id)
        client= Client.objects.get(clientname=consultantform.company_name)
        form= SubsidiaryForm(request,request.POST,request.FILES,instance=consultantform)
        if form.is_valid():
            form.save()
                        
            url=reverse('consultantformss',kwargs={'a_id':client.id})
            return HttpResponseRedirect(url)
    
@login_required   
def ram3(request,consultantform_id=1):#edit and save related company form
    if request.method == 'POST':
        consultantform = Relatedcompany.objects.get(id=consultantform_id)
        client= Client.objects.get(clientname=consultantform.company_name)
        form= RelatedcompanyForm(request,request.POST,request.FILES,instance=consultantform)
        if form.is_valid():
            form.save()
                        
            url=reverse('consultantformss',kwargs={'a_id':client.id})
            return HttpResponseRedirect(url)

@login_required   
def ramm(request,checklistform_id=1):#edit and save background checklist
    if request.method == 'POST':
        checklistform = Backgroundcheck.objects.get(id=checklistform_id)
        client= Client.objects.get(clientname=checklistform.company_name)
        form= BackgroundcheckForm(request,request.POST,instance=checklistform)
        form1=BackgroundcheckbForm(request.POST)
        if form.is_valid():
            form.save()
            torm1=form1.save(commit=False)
            torm1.company_name=Backgroundcheck.objects.get(id=checklistform_id).company_name
            torm1.user=request.user.username
            torm1.version=Backgroundcheck.objects.get(id=checklistform_id).version
            torm1.form_name=Backgroundcheck.objects.get(id=checklistform_id).form_name
            torm1.save()
            
            
            
            url=reverse('consultantformss',kwargs={'a_id':client.id})
            return HttpResponseRedirect(url)

@login_required   
def rammm(request,projectform_id=1):#edit and save project form
    if request.method == 'POST':
        projectform = Project.objects.get(id=projectform_id)
        client= Client.objects.get(clientname=projectform.client)
        form= ProjectForm(request,request.POST,instance=projectform)
        if form.is_valid():
            form.save()
                        
            url=reverse('consultantformss',kwargs={'a_id':client.id})
            return HttpResponseRedirect(url)
    
@login_required   
def sam(request,a_id=1,project_id=1,dueform_id=1):#view temporary duediligence form
    
    
    if 'modify' in request.POST:#finalizes form
        
        form=DuediligencepForm(request,request.POST,request.FILES)
        
        
        
        
        if form.is_valid():
            torr1=form.save(commit=False)
            torr1.project=Duediligence.objects.get(id=dueform_id).project
            torr1.company_name=Client.objects.get(id=a_id)
            torr1.upload_Doc1=Duediligence.objects.get(id=dueform_id).upload_Doc1
            torr1.upload_Doc2=Duediligence.objects.get(id=dueform_id).upload_Doc2
            torr1.form_name=Duediligence.objects.get(id=dueform_id).form_name
            torr1.version=Duediligence.objects.get(id=dueform_id).version
            torr1.save()
            
            Duediligence.objects.get(id=dueform_id).delete()
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url)
        
    elif 'modify1' in request.POST:#saves changes in temporary
        dform = Duediligence.objects.get(id=dueform_id)
        form= DuediligenceForm(request,request.POST,request.FILES,instance=dform)
        
        
        if form.is_valid():
            form.save()
            #torr1.upload=Duediligence.objects.get(id=dueform_id).upload
            #return render(request,'dueform.html',{'form':form,'project':Project.objects.get(id=project_id),'a':Client.objects.get(id=a_id),'dueform' : Duediligence.objects.get(id=dueform_id)})
            url=reverse('sam',kwargs={'a_id':a_id,'project_id':project_id,'dueform_id':dueform_id})
            return HttpResponseRedirect(url)
    elif 'modify2' in request.POST:#deletes in temporary
        dform = Duediligence.objects.get(id=dueform_id)
        form= DuediligenceForm(request,request.POST,request.FILES,instance=dform)
        if form.is_valid():
            form.save(commit=False)
            Duediligence.objects.get(id=dueform_id).delete()
            
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url)
    else:
     dform = Duediligence.objects.get(id=dueform_id)
    
     form= DuediligenceForm(request,instance=dform)
    #form= DuediligenceForm(request,request.FILES)
    
    
    
    return render(request,'dueform.html',{'user':request.user,'form':form,'project':Project.objects.get(id=project_id),'a':Client.objects.get(id=a_id),'dueform' : Duediligence.objects.get(id=dueform_id)})
    
@login_required   
def samp(request,a_id=1,project_id=1,dueform_id=1):#permanent duediligence form
    
    
   
    
    if 'modify1' in request.POST:#upgrades to a new version and exports it to temporary
        form= DuediligencetForm(request,request.POST,request.FILES)
        project=Project.objects.get(id=project_id)
        
        if form.is_valid():
            torr1=form.save(commit=False)
            torr1.project=Duediligencep.objects.get(id=dueform_id).project
            torr1.company_name=Client.objects.get(id=a_id)
            torr1.upload_Doc1=Duediligencep.objects.get(id=dueform_id).upload_Doc1
            torr1.upload_Doc2=Duediligencep.objects.get(id=dueform_id).upload_Doc2
            torr1.version=Duediligencep.objects.get(id=dueform_id).version+1
            n=torr1.version
            torr1.form_name="DDF"+str(project.id)+"."+str(n)
            torr1.save()
            
            
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url)
    
    dform = Duediligencep.objects.get(id=dueform_id)
    form= DuediligencepForm(request,instance=dform)
    
    if request.user.is_staff:
     return render(request,'pdueform.html',{'user':request.user,'form':form,'project':Project.objects.get(id=project_id),'a':Client.objects.get(id=a_id),'dueform' : Duediligencep.objects.get(id=dueform_id)})
    else:
     return render(request,'cdueform.html',{'user':request.user,'form':form,'project':Project.objects.get(id=project_id),'a':Client.objects.get(id=a_id),'dueform' : Duediligencep.objects.get(id=dueform_id)})

@login_required   
def samm(request,a_id=1,project_id=1,scriptform_id=1):#temporary script form
    
     if 'modify' in request.POST:#finalizes form
        form=ScriptpForm(request,request.POST,request.FILES)
        
        if form.is_valid():
            tor1=form.save(commit=False)
            tor1.project=Script.objects.get(id=scriptform_id).project
            tor1.company_name=Client.objects.get(id=a_id)
            tor1.upload_Doc1=Script.objects.get(id=scriptform_id).upload_Doc1
            tor1.upload_Doc2=Script.objects.get(id=scriptform_id).upload_Doc2
            tor1.form_name=Script.objects.get(id=scriptform_id).form_name
            tor1.version=Script.objects.get(id=scriptform_id).version
            tor1.save()
            Script.objects.get(id=scriptform_id).delete()            
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url)
     elif 'modify2' in request.POST:#deletes in temporary
        dform = Script.objects.get(id=scriptform_id)
        form= ScriptForm(request,request.POST,request.FILES,instance=dform)
        if form.is_valid():
            form.save(commit=False)
            Script.objects.get(id=scriptform_id).delete()
            
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url) 
     elif 'modify1' in request.POST:#saves changes in temporary
        dform = Script.objects.get(id=scriptform_id)
        form= ScriptForm(request,request.POST,request.FILES,instance=dform)
        
        
        if form.is_valid():
            form.save()
            
            url=reverse('samm',kwargs={'a_id':a_id,'project_id':project_id,'scriptform_id':scriptform_id})
            return HttpResponseRedirect(url)
            
     else:
        dform = Script.objects.get(id=scriptform_id)
        form= ScriptForm(request,instance=dform)
    
    
     return render(request,'scriptform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'project':Project.objects.get(id=project_id),'scriptform' : Script.objects.get(id=scriptform_id)})
    
@login_required   
def sammp(request,a_id=1,project_id=1,scriptform_id=1):#permanent script form
    
    if 'modify1' in request.POST:#upgrades to new version and exports it to temporary
        form=ScriptForm(request,request.POST,request.FILES)
        project=Project.objects.get(id=project_id)
        
        
        if form.is_valid():
            torr1=form.save(commit=False)
            torr1.project=Scriptp.objects.get(id=scriptform_id).project
            torr1.company_name=Client.objects.get(id=a_id)
            torr1.upload_Doc1=Scriptp.objects.get(id=scriptform_id).upload_Doc1
            torr1.upload_Doc2=Scriptp.objects.get(id=scriptform_id).upload_Doc2
            torr1.version=Scriptp.objects.get(id=scriptform_id).version+1
            n=torr1.version
            torr1.form_name="SC"+str(project.id)+"."+str(n)
            torr1.save()
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url)
    
    #if 'modify1' in request.POST:
        #form= ScriptForm(request,request.POST)
        #if form.is_valid():
            #form.save()
            
            #return HttpResponseRedirect('/clients')
        
    dform = Scriptp.objects.get(id=scriptform_id)
    form= ScriptpForm(request,instance=dform)
    
    if request.user.is_staff:
     return render(request,'pscriptform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'project':Project.objects.get(id=project_id),'scriptform' : Scriptp.objects.get(id=scriptform_id)})
    else:
     return render(request,'cscriptform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'project':Project.objects.get(id=project_id),'scriptform' : Scriptp.objects.get(id=scriptform_id)})
        
@login_required   
def sammm(request,a_id=1,project_id=1,strategyform_id=1):#temporary strategy
    if 'modify' in request.POST:#finalizes
        form=StrategypForm(request,request.POST,request.FILES)
        if form.is_valid():
            tor1=form.save(commit=False)
            tor1.project=Strategy.objects.get(id=strategyform_id).project
            tor1.company_name=Client.objects.get(id=a_id)
            tor1.upload_Doc1=Strategy.objects.get(id=strategyform_id).upload_Doc1
            tor1.upload_Doc2=Strategy.objects.get(id=strategyform_id).upload_Doc2
            tor1.upload_Doc3=Strategy.objects.get(id=strategyform_id).upload_Doc3
            tor1.upload_Doc4=Strategy.objects.get(id=strategyform_id).upload_Doc4
            tor1.upload_Doc5=Strategy.objects.get(id=strategyform_id).upload_Doc5
            tor1.form_name=Strategy.objects.get(id=strategyform_id).form_name
            tor1.version=Strategy.objects.get(id=strategyform_id).version
            tor1.save()
            Strategy.objects.get(id=strategyform_id).delete()            
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url)
    elif 'modify2' in request.POST:#saves changes in temporary
        dform = Strategy.objects.get(id=strategyform_id)
        form= StrategyForm(request,request.POST,request.FILES,instance=dform)
        if form.is_valid():
            form.save(commit=False)
            Strategy.objects.get(id=strategyform_id).delete()
            
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url) 
    elif 'modify1' in request.POST:#deletes in temporary
        dform = Strategy.objects.get(id=strategyform_id)
        form= StrategyForm(request,request.POST,request.FILES,instance=dform)
        if form.is_valid():
            form.save()
                        
            url=reverse('sammm',kwargs={'a_id':a_id,'project_id':project_id,'strategyform_id':strategyform_id})
            return HttpResponseRedirect(url)
        
    else:
     dform = Strategy.objects.get(id=strategyform_id)
     form= StrategyForm(request,instance=dform)
    
    
    return render(request,'stratform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'project':Project.objects.get(id=project_id),'stratform' : Strategy.objects.get(id=strategyform_id)})
        
@login_required   
def sammmp(request,a_id=1,project_id=1,strategyform_id=1):#permanent strategy
    #if 'modify' in request.POST:
        #form=StrategypForm(request,request.POST)
        #if form.is_valid():
            #form.save()
                        
            #return HttpResponseRedirect('/clients')
    
    if 'modify1' in request.POST:#upgrades it to a new version and exports it to temporary
        form= StrategyForm(request,request.POST,request.FILES)
        project=Project.objects.get(id=project_id)
        
        
        if form.is_valid():
            torr1=form.save(commit=False)
            torr1.project=Strategyp.objects.get(id=strategyform_id).project
            torr1.company_name=Client.objects.get(id=a_id)
            torr1.upload_Doc1=Strategyp.objects.get(id=strategyform_id).upload_Doc1
            torr1.upload_Doc2=Strategyp.objects.get(id=strategyform_id).upload_Doc2
            torr1.upload_Doc3=Strategyp.objects.get(id=strategyform_id).upload_Doc3
            torr1.upload_Doc4=Strategyp.objects.get(id=strategyform_id).upload_Doc4
            torr1.upload_Doc5=Strategyp.objects.get(id=strategyform_id).upload_Doc5
            torr1.version=Strategyp.objects.get(id=strategyform_id).version+1
            n=torr1.version
            torr1.form_name="ST"+str(project.id)+"."+str(n)
            torr1.save()
            
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url)
        
    dform = Strategyp.objects.get(id=strategyform_id)
    form= StrategypForm(request,instance=dform)
    
    if request.user.is_staff:
     return render(request,'pstratform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'project':Project.objects.get(id=project_id),'stratform' : Strategyp.objects.get(id=strategyform_id)})
    else:
     return render(request,'cstratform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'project':Project.objects.get(id=project_id),'stratform' : Strategyp.objects.get(id=strategyform_id)})

@login_required   
def dam(request,a_id=1,project_id=1,psform_id=1):#temporary problem solving
    if 'modify' in request.POST:#finalizes form
        form=ProblemSolvingpForm(request,request.POST,request.FILES)
        if form.is_valid():
            tor1=form.save(commit=False)
            tor1.project=Problemsolving.objects.get(id=psform_id).project
            tor1.company_name=Client.objects.get(id=a_id)
            tor1.upload_Doc1=Problemsolving.objects.get(id=psform_id).upload_Doc1
            tor1.upload_Doc2=Problemsolving.objects.get(id=psform_id).upload_Doc2
            tor1.form_name=Problemsolving.objects.get(id=psform_id).form_name
            tor1.version=Problemsolving.objects.get(id=psform_id).version
            tor1.save()
            Problemsolving.objects.get(id=psform_id).delete()            
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url)
    elif 'modify2' in request.POST:#deletes form
        dform = Problemsolving.objects.get(id=psform_id)
        form= ProblemSolvingForm(request,request.POST,request.FILES,instance=dform)
        if form.is_valid():
            form.save(commit=False)
            Problemsolving.objects.get(id=psform_id).delete()
            
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url) 
    elif 'modify1' in request.POST:#saves changes in temporary
        dform = Problemsolving.objects.get(id=psform_id)
        form= ProblemSolvingForm(request,request.POST,request.FILES,instance=dform)
        if form.is_valid():
            form.save()
                        
            url=reverse('dam',kwargs={'a_id':a_id,'project_id':project_id,'psform_id':psform_id})
            return HttpResponseRedirect(url)
        
    else:
     dform = Problemsolving.objects.get(id=psform_id)
     form= ProblemSolvingForm(request,instance=dform)
    
    
    return render(request,'psform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'project':Project.objects.get(id=project_id),'psform' : Problemsolving.objects.get(id=psform_id)})
        
@login_required   
def damp(request,a_id=1,project_id=1,psform_id=1):#permanent problem solving
    #if 'modify' in request.POST:
        #form=StrategypForm(request,request.POST)
        #if form.is_valid():
            #form.save()
                        
            #return HttpResponseRedirect('/clients')
    
    if 'modify1' in request.POST:#upgrades it to a new version and exports it to temporary
        form= ProblemSolvingForm(request,request.POST,request.FILES)
        project=Project.objects.get(id=project_id)
        
        
        if form.is_valid():
            torr1=form.save(commit=False)
            torr1.project=Problemsolvingp.objects.get(id=psform_id).project
            torr1.company_name=Client.objects.get(id=a_id)
            torr1.upload_Doc1=Problemsolvingp.objects.get(id=psform_id).upload_Doc1
            torr1.upload_Doc2=Problemsolvingp.objects.get(id=psform_id).upload_Doc2
            torr1.version=Problemsolvingp.objects.get(id=psform_id).version+1
            n=torr1.version
            torr1.form_name="PS"+str(project.id)+"."+str(n)
            torr1.save()
            
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url)
        
    dform = Problemsolvingp.objects.get(id=psform_id)
    form= ProblemSolvingpForm(request,instance=dform)
    
    if request.user.is_staff:
     return render(request,'ppsform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'project':Project.objects.get(id=project_id),'psform' : Problemsolvingp.objects.get(id=psform_id)})
    else:
     return render(request,'cpsform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'project':Project.objects.get(id=project_id),'psform' : Problemsolvingp.objects.get(id=psform_id)})

@login_required   
def damm(request,a_id=1,project_id=1,digiform_id=1):#temporary digitalization form
    if 'modify' in request.POST:#finalizes form
        form=DigitalizationpForm(request,request.POST,request.FILES)
        if form.is_valid():
            tor1=form.save(commit=False)
            tor1.project=Digitalization.objects.get(id=digiform_id).project
            tor1.company_name=Client.objects.get(id=a_id)
            tor1.upload_Doc1=Digitalization.objects.get(id=digiform_id).upload_Doc1
            tor1.upload_Doc2=Digitalization.objects.get(id=digiform_id).upload_Doc2
            tor1.form_name=Digitalization.objects.get(id=digiform_id).form_name
            tor1.version=Digitalization.objects.get(id=digiform_id).version
            tor1.save()
            Digitalization.objects.get(id=digiform_id).delete()            
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url)
    elif 'modify2' in request.POST:#deletes form
        dform = Digitalization.objects.get(id=digiform_id)
        form= DigitalizationForm(request,request.POST,request.FILES,instance=dform)
        if form.is_valid():
            form.save(commit=False)
            Digitalization.objects.get(id=digiform_id).delete()
            
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url) 
    elif 'modify1' in request.POST:#saves changes 
        dform = Digitalization.objects.get(id=digiform_id)
        form= DigitalizationForm(request,request.POST,request.FILES,instance=dform)
        if form.is_valid():
            form.save()
                        
            url=reverse('damm',kwargs={'a_id':a_id,'project_id':project_id,'digiform_id':digiform_id})
            return HttpResponseRedirect(url)
        
    else:
     dform = Digitalization.objects.get(id=digiform_id)
     form= DigitalizationForm(request,instance=dform)
    
    
    return render(request,'digiform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'project':Project.objects.get(id=project_id),'digiform' : Digitalization.objects.get(id=digiform_id)})
        
@login_required   
def dammp(request,a_id=1,project_id=1,digiform_id=1):#permanent digitalization form
    #if 'modify' in request.POST:
        #form=StrategypForm(request,request.POST)
        #if form.is_valid():
            #form.save()
                        
            #return HttpResponseRedirect('/clients')
    
    if 'modify1' in request.POST:#upgrades it to new version and exports it to temporary
        form= DigitalizationForm(request,request.POST,request.FILES)
        project=Project.objects.get(id=project_id)
        
        
        if form.is_valid():
            torr1=form.save(commit=False)
            torr1.project=Digitalizationp.objects.get(id=digiform_id).project
            torr1.company_name=Client.objects.get(id=a_id)
            torr1.upload_Doc1=Digitalizationp.objects.get(id=digiform_id).upload_Doc1
            torr1.upload_Doc2=Digitalizationp.objects.get(id=digiform_id).upload_Doc2
            torr1.version=Digitalizationp.objects.get(id=digiform_id).version+1
            n=torr1.version
            torr1.form_name="DIGI"+str(project.id)+"."+str(n)
            torr1.save()
            
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url)
        
    dform = Digitalizationp.objects.get(id=digiform_id)
    form= DigitalizationpForm(request,instance=dform)
    
    if request.user.is_staff:
     return render(request,'pdigiform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'project':Project.objects.get(id=project_id),'digiform' : Digitalizationp.objects.get(id=digiform_id)})
    else:
     return render(request,'cdigiform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'project':Project.objects.get(id=project_id),'digiform' : Digitalizationp.objects.get(id=digiform_id)})

@login_required   
def dammm(request,a_id=1,project_id=1,miomform_id=1):#temporary min of meeting
    if 'modify' in request.POST:#finalizes form
        form=MiompForm(request,request.POST,request.FILES)
        if form.is_valid():
            tor1=form.save(commit=False)
            tor1.project=Miom.objects.get(id=miomform_id).project
            tor1.company_name=Client.objects.get(id=a_id)
            tor1.upload_Doc1=Miom.objects.get(id=miomform_id).upload_Doc1
            tor1.upload_Doc2=Miom.objects.get(id=miomform_id).upload_Doc2
            tor1.form_name=Miom.objects.get(id=miomform_id).form_name
            tor1.version=Miom.objects.get(id=miomform_id).version
            tor1.save()
            Miom.objects.get(id=miomform_id).delete()            
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url)
    elif 'modify2' in request.POST:#saves changes 
        dform = Miom.objects.get(id=miomform_id)
        form= MiomForm(request,request.POST,request.FILES,instance=dform)
        if form.is_valid():
            form.save(commit=False)
            Miom.objects.get(id=miomform_id).delete()
            
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url) 
    elif 'modify1' in request.POST:#deletes form
        dform = Miom.objects.get(id=miomform_id)
        form= MiomForm(request,request.POST,request.FILES,instance=dform)
        if form.is_valid():
            form.save()
                        
            url=reverse('dammm',kwargs={'a_id':a_id,'project_id':project_id,'miomform_id':miomform_id})
            return HttpResponseRedirect(url)
        
    else:
     dform = Miom.objects.get(id=miomform_id)
     form= MiomForm(request,instance=dform)
    
    
    return render(request,'miomform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'project':Project.objects.get(id=project_id),'miomform' : Miom.objects.get(id=miomform_id)})
        
@login_required   
def dammmp(request,a_id=1,project_id=1,miomform_id=1):#permanent min of meeting
    #if 'modify' in request.POST:
        #form=StrategypForm(request,request.POST)
        #if form.is_valid():
            #form.save()
                        
            #return HttpResponseRedirect('/clients')
    
    if 'modify1' in request.POST:#upgrades it to a new version and exports it to temporary
        form= MiomForm(request,request.POST,request.FILES)
        project=Project.objects.get(id=project_id)
        
        
        if form.is_valid():
            torr1=form.save(commit=False)
            torr1.project=Miomp.objects.get(id=miomform_id).project
            torr1.company_name=Client.objects.get(id=a_id)
            torr1.upload_Doc1=Miomp.objects.get(id=miomform_id).upload_Doc1
            torr1.upload_Doc2=Miomp.objects.get(id=miomform_id).upload_Doc2
            torr1.version=Miomp.objects.get(id=miomform_id).version+1
            n=torr1.version
            torr1.form_name="MIOM"+str(project.id)+"."+str(n)
            torr1.save()
            
            url=reverse('serviceforms',kwargs={'a_id':a_id,'serviceform_id':project_id})
            return HttpResponseRedirect(url)
        
    dform = Miomp.objects.get(id=miomform_id)
    form= MiompForm(request,instance=dform)
    
    if request.user.is_staff:
     return render(request,'pmiomform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'project':Project.objects.get(id=project_id),'miomform' : Miomp.objects.get(id=miomform_id)})
    else:
     return render(request,'cmiomform.html',{'user':request.user,'form':form,'a':Client.objects.get(id=a_id),'project':Project.objects.get(id=project_id),'miomform' : Miomp.objects.get(id=miomform_id)})

                                