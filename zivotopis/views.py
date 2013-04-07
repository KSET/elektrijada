# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from zivotopis.models import CurriculumVitae
from zivotopis.forms import CVForm

def cv_add(request):
    form = CVForm(request.POST or None)
    if form.is_valid():
        form.save()
        msg = u'Životopis je uspješno spremljen.'
        messages.add_message(request, messages.SUCCESS, msg)
        return redirect('zivotopis:cv_add')

    return render(request, 'zivotopis/add.html', {
        'form': form,
    })

@login_required
def cv_detail(request, cv_id):
    cv = get_object_or_404(CurriculumVitae, id=cv_id)
    form = CVForm(instance=cv)

    return render(request, 'zivotopis/detail.html', {
        'cv': cv,
        'form': form,
    })

# !view
def search_cvs(query):
    qs = CurriculumVitae.objects.all()
    for q in query.split(' '):
        if not q: continue
        qs = qs.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(college__icontains=q) | Q(course__icontains=q))
    return qs

@login_required
def cv_list(request):
    query = request.GET.get('q', '')
    return render(request, 'zivotopis/list.html', {
        'cvs': search_cvs(query),
        'query': query,
    })
