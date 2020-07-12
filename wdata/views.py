from django.shortcuts import redirect, render
from .models import SelectDateTime
from .forms import SelectDateTimeForm
from django.views import View
template_renewal_add_path = 'wdata/renewal_add.html'

class SelectDateTimeViews(View):
    model = SelectDateTime
    form = SelectDateTimeForm

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(AromaInLureMixViews, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form()
        return render(request,
                      template_renewal_add_path,
                      {'form': form})

    def post(self, request, *args, **kwargs):
        entry = self.model()
        form = self.form(request.POST)
        if form.is_valid():
            entry.date = form.cleaned_data['date']
            entry.time = form.cleaned_data['time']
            entry.save()
        return redirect('selectdatetime:select')