from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

Day = {
    'saturday': 'this is saturated in dictionary',
    'sunday': 'this is sunday in dictionary',
    'monday': 'this is monday in dictionary',
    'tuesday': 'this is tuesday in dictionary',
    'wednesday': 'this is wednesday in dictionary',
    'thursday': 'this is thursday in dictionary',
    'friday': 'this is friday in dictionary',
}


def home(request):
    Template = render_to_string("UZ/m.html")
    return HttpResponse(Template)


def Templates(request, day):
    day_data = Day.get(day)
    context = {
        "day2": day,
        "day_data": day_data
    }
    return render(request, "UZ/t.html", context)


def text(request):
    return render(request, "UZ/text.html")


def after_text(request):
    return render(request, "UZ/after_text.html")


def to_day(request, day):
    day_data = Day.get(day)
    context = {
        "day": day,
        "day_data": day_data
    }
    if day_data is not None:
        return render(request, "UZ/m.html", context)
    else:
        return HttpResponseNotFound("Could not find")


def to_day_number(request, day):
    list_day = list(Day.keys())
    r = list_day[day - 1]
    number = reverse("Number", args=[r])
    if day > len(list_day):
        return HttpResponseNotFound("Could not find")
    else:
        return HttpResponseRedirect(number)


def list_day(request):
    day_list = list(Day.keys())
    list_item = ""
    for day in day_list:
        url_path = reverse('Number', args=[day])
        list_item += f"<li> <a href='{url_path}'> {day} </a> </li>\n"
    meno = f" <div> <ul> {list_item} </ul></div>  "
    return HttpResponse(meno)



