from django.http import HttpResponse
from django.shortcuts import render

#Just Learn Html
# def index(request):
#     return HttpResponse('''<h>YASH GUPTA</h> <br>
#     <a href="https://www.youtube.com/watch?v=pWsHZ0rc0Zc">
#      I Train Like " Saket Gokhale " For A Day</a><br>
#     <a href="https://www.youtube.com/watch?v=pQ4RdI4i0Vs">
#     <h>High Protein Veg Oats Recipe (PRO-OATS)🇮🇳🇮🇳| Package Of Super GAINZZ </h></a>''')

# def about(request):
#     return HttpResponse("about yash bhai")    

def index(request):
    # return HttpResponse("<h><b> Home </b></h>")
    return render(request,'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed }

        djtext=analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)
    # else:
    #     return HttpResponse("Error")  
    if(removepunc!="on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("ERROR")
    return render(request, 'analyze.html', params)    

# def analyse(request):
#     djtext=request.GET.get('Text','default')
#     removepunc= request.GET.get('removepunc','off')
#     fullcaps= request.GET.get('fullcaps','off')
#     newlineremover= request.GET.get('newlineremover','off')
#     spaceremover= request.GET.get('spaceremover','off')
#     charcount =request.GET.get('charcount','off')
#     functions=""
#     if removepunc=="on":
#         analyzed=""
#         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#         for char in djtext:
#             if char not in punctuations:
#                 analyzed=analyzed + char
#         functions= functions+' Removed Punctuations'
#         djtext=analyzed    

#     if(fullcaps=="on"):
#         analyzed=""
#         for char in djtext:
#             analyzed=analyzed+char.upper() 
#         if len(functions)!=0:
#             functions=functions+" &"
#         functions=functions+' Change To Upparcase'
#         djtext=analyzed
    
#     if(newlineremover=="on"):
#         analyzed=""
#         for char in djtext:
#             if char!="\n":
#                 analyzed=analyzed+char
#         if len(functions)!=0:
#             functions=functions+" &"
#         functions=functions+' NEW LINE REMOVER'  
#         djtext=analyzed      

#     if(spaceremover=="on"):
#         analyzed=""
#         for char in djtext:
#             if char!="  ":
#                 analyzed=analyzed+char
#         if len(functions)!=0:
#             functions=functions+" &"
#         functions=functions+' Extra Space Remover'  
#         djtext=analyzed       
     
#     elif(charcount=="on"):
#         k=0
#         for char in djtext:
#             if char.isalpha()== True:
#                 k=k+1
#         params= {'purpose':'The Number Of Character is','analysed_text':int(k)}
#         return render(request,'analyse.html',params) 
#     else:
#         return HttpResponse("ERROR") 

   

# def removepunc(request):
#     #Get The Text
#     djtext= request.GET.get('Text','default')
#     #Analyse the Text
#     return HttpResponse('''<h> Remove Punctuation </h>
#     <br> <a href="index"> Home </a>''')

# def capfirst(request):
#     return HttpResponse('''<h> Capitalize First</h><br>
#     <a href="index"> Home </a>''')   

# def newlineremover(request):
#     return HttpResponse(''' <h> New Line Remover </h> <br>
#     <a href="index"> Home </a>''')

# def spaceremover(request):
#     return HttpResponse(''' <h> Space Remover </h> <br>
#     <a href="index"> Home </a>''')   

# def charcount(request):
#     return HttpResponse(''' <h> Character Counts </h> <br>
#     <a href="index"> Home </a>''')          
