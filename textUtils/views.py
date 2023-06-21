#Manually Created File
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #  with open("1.txt", "r") as f:    # Opening the file in read mode, we don't use r+ because file already exists, r+ is used when file doesn't exists then assigning it a variable named f
    #       content = f.read()    # Reading the contents of the file and storing it in a variable, we use read instead of readlines because readlines gives each line as a list element
    #  return HttpResponse(content)
    # return HttpResponse('''<h1>Home</h1> <a href="https://abiralale.com.np">Portfolio</a>''')
    # nav = ''' <h1>Home</h1>
    #     <ul>
    #     <li><a href="/about">About</a></li>
    #     <li><a href="/removepunc">Remove Punctuation</a></li>
    #     <li><a href="/capfirst">Capitalize First</a></li>
    #     <li><a href="/newlineremove">New Line Remover</a></li>
    #     <li><a href="/spaceremove">Space Remover</a></li>
    #     <li><a href="/charcount">Character Count</a></li>
    # '''
    # return HttpResponse(nav);

    return render(request,'index.html')

# def about(request):
#     return HttpResponse("<h1>About</h1><a href='/'>Back</a>")

# def removepunc(request):
#     #get the text
#     djtext = request.GET.get('text','default')
#     print(djtext)
#     #analyse the text
#     return HttpResponse("<h1>Remove Punc</h1><a href='/'>Back</a>")

# def capfirst(request):
#     return HttpResponse("<h1>Capitilize first</h1><a href='/'>Back</a>")

# def newlineremove(request):
#     return HttpResponse("<h1>New Line Remove</h1><a href='/'>Back</a>")

# def spaceremove(request):
#     return HttpResponse("<h1>Space remover</h1><a href='/'>Back</a>")

# def charcount(request):
#     return HttpResponse("<h1>Character Count</h1><a href='/'>Back</a>")


def analyze(request):
    # #get the text
    # djtext = request.GET.get('text','default')
    # # removepunc = request.GET.get('removepunc','default')

    # # Check Checkbox values
    # removepunc = request.GET.get('removepunc','off')
    # capfirst = request.GET.get('capfirst','off')
    # newlineremove = request.GET.get('newlineremove','off')
    # spaceremove = request.GET.get('spaceremove','off')
    # charcount = request.GET.get('charcount','off')
    #get the text
    djtext = request.POST.get('text','default')
    # removepunc = request.GET.get('removepunc','default')

    # Check Checkbox values
    removepunc = request.POST.get('removepunc','off')
    capfirst = request.POST.get('capfirst','off')
    newlineremove = request.POST.get('newlineremove','off')
    spaceremove = request.POST.get('spaceremove','off')
    charcount = request.POST.get('charcount','off')


    # Checking If Checkbox is on
    # Removing Punctuations
    if removepunc == "on":
        # analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char

        params = {
            'purpose':'Removed Punctuations',
            'analyzed_text': analyzed
        }
        #analyse the text
        djtext = analyzed
        # return render(request,'analyze.html',params)
    
    # CAPITALIZING
    
    if capfirst == "on":
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {
            'purpose':'Capitalized',
            'analyzed_text': analyzed
        }
        #analyse the text
        djtext = analyzed
        # return render(request,'analyze.html',params)
        
    #New Line Remover
    if newlineremove == "on":
        analyzed = ''
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        params = {
            'purpose': 'Removed New Line',
            'analyzed_text': analyzed
        }
        djtext = analyzed
        # return render(request,'analyze.html',params)



    #ExtraSpace Remover
    if spaceremove == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
                
        params = {
            'purpose': 'Removed extra spaces',
            'analyzed_text': analyzed
        }
        djtext = analyzed
        # return render(request,'analyze.html',params)

    # No of characters

    if charcount == "on":
        analyzed = len(djtext)
        params = {
            'purpose': 'No of characters:',
            'analyzed_text': analyzed
        }
        # return render(request,'analyze.html',params)
    
    if(removepunc!='on' and capfirst!='on' and newlineremove!='on' and spaceremove!='on' and charcount!='on'): 
        return HttpResponse("Please select any operation and <a href='/'>Try Again</a>")
    
    return render(request, 'analyze.html', params)