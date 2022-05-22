from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator

from string import ascii_uppercase
from MainApp.models import Country


def home(request):
    return render(request, 'index.html')


def languages_page(request):
    countries = Country.objects.all()
    unic_language_list = sorted(set([language for country in countries
                                     for language in country.languages.split(',')]))
    paginator = Paginator(unic_language_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "languages": unic_language_list,
        "alfabet": ascii_uppercase,
        'page_obj': page_obj,
    }
    return render(request, "languages_page.html", context)


def languages_that_start_with_spec_char(request, char):
    countries = Country.objects.all()
    match_languages = sorted(set([language for country in countries
                                     for language in country.languages.split(',') if language[0] == char]))
    #match_languages = []

    # for language in country.languages:
    #     if language[0] == char:
    #         match_languages.append(language)
    paginator = Paginator(match_languages, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "languages": match_languages,
        "char": char,
        "alfabet": ascii_uppercase,
        'page_obj': page_obj,
    }
    return render(request, "languages_that_start_with_spec_char.html", context)


def countries_list_page(request):
    countries = [country.country for country in Country.objects.all()]
    paginator = Paginator(countries, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "countries": countries,
        "alfabet": ascii_uppercase,
        'page_obj': page_obj,
    }
    return render(request, "countries_list_page.html", context)


def special_country_page(request, country_name):
    country = Country.objects.get(country=country_name)
    countries = [country.country for country in Country.objects.all()]
    languages_list = country.languages.split(',')
    paginator = Paginator(countries, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "country_name": country.country,
        'languages': languages_list,
        "alfabet": ascii_uppercase,
        'page_obj': page_obj,
    }
    return render(request, "country_page.html", context)


def countries_that_start_with_spec_char(request, char):
    countries = Country.objects.all()
    match_countrires = []
    for country in countries:
        if country.country[0] == char:
            match_countrires.append(country.country)
    paginator = Paginator(match_countrires, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "countries": match_countrires,
        "char": char,
        "alfabet": ascii_uppercase,
        'page_obj': page_obj,
    }
    return render(request, "countries_that_start_with_spec_char.html", context)


def countries_with_spec_lang(request, language):
    match_countrires = []
    countries = Country.objects.all()
    unic_language_list = sorted(set([language for country in countries
                                     for language in country.languages.split(',')]))
    for country in countries:
        if language in country.languages:
            match_countrires.append(country.country)
    paginator = Paginator(unic_language_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "countries": match_countrires,
        'language': language,
        "alfabet": ascii_uppercase,
        'page_obj': page_obj,
    }
    return render(request, "countries_with_spec_lang.html", context)
