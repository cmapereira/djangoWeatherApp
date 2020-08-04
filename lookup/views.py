from django.shortcuts import render

def home(request):
  import json
  import requests

  if request.method == "POST":
    zipcode = request.POST['zipcode']
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=2759E87A-DCD7-469E-A206-D83A9DDBE27B")
    try:
      api = json.loads(api_request.content)
    except Exception as e:
      api = "Error"
    category_description = ''
    category_color = ''
    if api[0]['Category']['Name'] == "Good":
      category_description = "Description: (0 - 50) Air quality is considered satisfactory"
      category_color = 'good'
    elif api[0]['Category']['Name'] == "Moderate":
      category_description = "Description: (51 - 100) Air quality is considered acceptable"
      category_color = 'moderate'
    elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
      category_description = "Description: (101 - 150) Risk for people with lung disease"
      category_color = 'usg'
    elif api[0]['Category']['Name'] == "Unhealthy":
      category_description = "Description: (151 - 200) Risk for every people"
      category_color = 'unhealthy'
    elif api[0]['Category']['Name'] == "Very Unhealthy":
      category_description = "Description: (201 - 300) Serious healthy effect"
      category_color = 'veryunhealthy'
    elif api[0]['Category']['Name'] == "Hazardous":
      category_description = "Description: (301 - 500) Healthy warning - emergency conditions"
      category_color = 'hazardous'
    return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color})

  else:
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=2759E87A-DCD7-469E-A206-D83A9DDBE27B")
    try:
      api = json.loads(api_request.content)
    except Exception as e:
      api = "Error"
    category_description = ''
    category_color = ''
    if api[0]['Category']['Name'] == "Good":
      category_description = "Description: (0 - 50) Air quality is considered satisfactory"
      category_color = 'good'
    elif api[0]['Category']['Name'] == "Moderate":
      category_description = "Description: (51 - 100) Air quality is considered acceptable"
      category_color = 'moderate'
    elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
      category_description = "Description: (101 - 150) Risk for people with lung disease"
      category_color = 'usg'
    elif api[0]['Category']['Name'] == "Unhealthy":
      category_description = "Description: (151 - 200) Risk for every people"
      category_color = 'unhealthy'
    elif api[0]['Category']['Name'] == "Very Unhealthy":
      category_description = "Description: (201 - 300) Serious healthy effect"
      category_color = 'veryunhealthy'
    elif api[0]['Category']['Name'] == "Hazardous":
      category_description = "Description: (301 - 500) Healthy warning - emergency conditions"
      category_color = 'hazardous'
    return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color})

def about(request):
  return render(request, 'about.html', {})