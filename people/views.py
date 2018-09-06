from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Team
from .models import Employee

def index(req):
  return render(req, 'people/index.html')

def employees(request, id):
  employee = Employee.objects.get(id=id)
  
  skill_list = employee.skills.split(",")
  
  template = loader.get_template('people/employee.html')
  context = {
    'employee': employee,
    'skills': skill_list,
    'team': employee.teamID
  }
  return render(request, 'people/employee.html', context)

def search(request, search):
  listEmployee = Employee.objects.all()
  listTeams = Team.objects.all()
  
  mydict = dict()
  tdict = dict()
  sdict = dict()
  cdict = dict()
  for emp in listEmployee:
    convertedName = emp.last_name.upper() + " " + emp.first_name
    mydict[convertedName] = emp.id

    listSkills = emp.skills.lower().split(",")
    if search.lower() in listSkills:
      sdict[convertedName] = emp.id
    if search.lower() == emp.COE.lower():
      cdict[convertedName] = emp.id

  for team in listTeams:
    tdict[team.teamName] = team.id
  

  results = ""
  resultsFound = False;

  cont = False
  for key, value in mydict.items():
    if search.lower() in key.lower():
      if cont == False:
        results += '<h5 style="font-weight: 700">Employees matching "' + search + '": </h5><ul class="list-unstyled">'
        cont = True
      url = '/people/employees/' + str(value) + '/'
      results += '<li class="media my-4"><img class="mr-3" src="http://via.placeholder.com/68x68" alt="Profile Picture">'
      results += '<div class="media-body"><h5 class="mt-0 mb-1"><a href="' + url + '">' + key + '</a></h5>'
      results += Employee.objects.get(id=value).position + '</div></li>'
  if cont == True:
    resultsFound = True;
    results += '</ul><br />'

  cont = False
  for key, value in tdict.items():
    if search.lower() in key.lower():
      if cont == False:
        results += '<h5 style="font-weight: 700">Teams matching "' + search + '": </h5><ul class="list-unstyled">'    
        cont = True    
      url = '/people/teams/' + str(value) + '/'
      results += '<li class="media my-4"><div class="media-body">'
      results += '<h5 class="mt-0 mb-1"><a href="' + url + '">' + key + '</a></h5>'
      results += Team.objects.get(id=value).department + '</div></li>'

  if cont == True:
    resultsFound = True;      
    results += '</ul><br />'

  cont = False
  for key, value in sdict.items():
    if cont == False and len(sdict) > 0:
      results += '<h5 style="font-weight: 700">Employees Skilled in "' + search + '": </h5><ul class="list-unstyled">'
      cont = True
    url = '/people/employees/' + str(value) + '/'
    results += '<li class="media my-4"><img class="mr-3" src="http://via.placeholder.com/68x68" alt="Profile Picture">'
    results += '<div class="media-body"><h5 class="mt-0 mb-1"><a href="' + url + '">' + key + '</a></h5>'
    results += Employee.objects.get(id=value).position + '</div></li>'

  if cont == True:
    resultsFound = True;      
    results += '</ul><br />'

  cont = False
  for key, value in cdict.items():
    if cont == False and len(cdict) > 0:
      results += '<h5 style="font-weight: 700">Centers of Expertise: </h5><ul class="list-unstyled">'
      cont = True
    url = '/people/employees/' + str(value) + '/'
    results += '<li class="media my-4"><img class="mr-3" src="http://via.placeholder.com/68x68" alt="Profile Picture">'
    results += '<div class="media-body"><h5 class="mt-0 mb-1"><a href="' + url + '">' + key + '</a></h5>'
    results += Employee.objects.get(id=value).position + '</div></li>'
    
  if cont == True:
    resultsFound = True;      
    results += '</ul><br />'  

  if resultsFound == False:
    results = "<h4>No results found</h4>"

  context = {
    'searchresults': results
  }

  return render(request, 'people/search.html', context)


def teamlist(request):
  #GIVE THIS PART INTO THE HTML
  all_teams = Team.objects.all()
  html = '<h5 style="font-weight: bold">All Teams</h5><ul class="list-unstyled">'
  
  for team in all_teams:
    url = '/people/teams/' + str(team.id) + '/'
    html += '<li class="media my-4"><div class="media-body">'
    html += '<h5 class="mt-0 mb-1"><a href="' + url + '">' + team.teamName + '</a></h5>'
    html += team.department + '</div></li>'
    
  html += '</ul>'
  context = {
    'teams': html
  }
  return render(request, 'people/teams.html', context)
  

def employeelist(req):
   #GIVE THIS PART INTO THE HTML
   all_employee = Employee.objects.all()
   html = '<h5 style="font-weight: bold">All Employees</h5><ul class="list-unstyled">'
   
   for emp in all_employee:
     url = '/people/employees/' + str(emp.id) + '/'
     
     html += '<li class="media my-4"><img class="mr-3" src="http://via.placeholder.com/68x68" alt="Profile Picture">'
     html += '<div class="media-body"><h5 class="mt-0 mb-1"><a href="' + url + '">' + emp.last_name + ' ' +  emp.first_name + '</a></h5>'
     html += emp.position + '</div></li>'
   
   html += '</ul>'
   context = {
     'employees': html
   }
   return render(req, 'people/employees.html', context)

def teamview(req, id):
  team = Team.objects.get(id=id)

  context = {
    'team': team
  }
  return render(req, 'people/team.html', context)
