from .commons import *


@login_required(login_url=login_view)
def prescription_edit(request):
    if request.resolver_match.view_name == 'prescription_new':
        pass
    context = get_default_context('index', user=request.user)
    custom_context = {}
    return render(request, 'mainapp/index.html', context | custom_context)


@login_required(login_url=login_view)
def order_edit(request):
    if request.resolver_match.view_name == 'prescription_new':
        pass
    context = get_default_context('index', user=request.user)
    custom_context = {}
    return render(request, 'mainapp/index.html', context | custom_context)


@login_required(login_url=login_view)
def receipt_edit(request):
    if request.resolver_match.view_name == 'prescription_new':
        pass
    context = get_default_context('index', user=request.user)
    custom_context = {}
    return render(request, 'mainapp/index.html', context | custom_context)


@login_required(login_url=login_view)
def certificate_edit(request):
    if request.resolver_match.view_name == 'prescription_new':
        pass
    context = get_default_context('index', user=request.user)
    custom_context = {}
    return render(request, 'mainapp/index.html', context | custom_context)


@login_required(login_url=login_view)
def contract_edit(request):
    if request.resolver_match.view_name == 'prescription_new':
        pass
    context = get_default_context('index', user=request.user)
    custom_context = {}
    return render(request, 'mainapp/index.html', context | custom_context)


