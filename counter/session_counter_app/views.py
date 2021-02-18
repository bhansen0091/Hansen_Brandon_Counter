from django.shortcuts import redirect, render

def root(request):
    if 'submission_count' not in request.session:
        request.session['submission_count'] = 0
    request.session['submission_count'] += 1
    return render(request, "index.html")

def destroy_session(request):
    request.session.clear()
    return redirect("/")