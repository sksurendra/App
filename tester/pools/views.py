# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import *
from tester import *

def index(request):
  #  o=Template(" <style type=""text/css""> #tb{        text-align:center;	}  <div>    <div>	<p>	<div id=""tb""> TextLock </div></p> </div> <div><p id=""tb""> Enter text to be matched : </p> <form action=""two.html"" method=""POST""> {% csrf_token %}		<div id=""tb""> <textarea cols=""80"" rows=""20"" name=""data""></textarea></div><p><input type=""submit""></p>	</div>
   # disp=o.render()
    #return render_to_response(disp)
    return render_to_response("one.html",RequestContext(request))
def two(request):
     data = request.POST.get('data', '')
     if(data):
        sites,measure = detect(data)
     else:
         return HttpResponse("No data was entered. Please enter data to continue.")
     #src = open('C:\Python\Scripts\tester\pools\two.html','r')
     list= zip(sites,measure)   
     t= Template("<div> TextLock<div><div> Results: </div> <ol>{% for item in list %}    <li>{{ item.0 }} - {{ item.1 }}</li>{% endfor %}</ol>")
     c= Context({'list': list},{'text': data})
     res= t.render(c)
     return HttpResponse(res)
     
    
    
