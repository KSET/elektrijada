# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from zivotopis import printer
from zivotopis.forms import CVForm
from zivotopis.models import CurriculumVitae

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
    if not cv.visible:
        raise PermissionDenied
    form = CVForm(instance=cv)
    return render(request, 'zivotopis/detail.html', {
        'cv': cv,
        'form': form,
    })

@login_required
def cv_pdf(request, cv_id):
    cv = get_object_or_404(CurriculumVitae, id=cv_id)
    if not cv.visible:
        raise PermissionDenied
    response = HttpResponse(printer.cv_pdf(cv), content_type='application/pdf')
    response['Content-Disposition'] = 'filename=%s_%s.pdf' % (cv.last_name, cv.first_name)
    return response

# !view
def search_cvs(query):
    qs = CurriculumVitae.objects.filter(visible=True)
    for q in query.split(' '):
        if not q: continue
        qs = qs.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(college__icontains=q) | Q(course__icontains=q))
    return qs

@login_required
def cv_list(request):
    query = request.GET.get('q', '')
    cvs = search_cvs(query)
    return render(request, 'zivotopis/list.html', {
        'cvs': cvs,
        'query': query,
    })
