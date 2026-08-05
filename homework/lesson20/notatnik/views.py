from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Note


def note_list(request):
    notes = Note.objects.all()
    paginator = Paginator(notes, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "notatnik/note_list.html",
        {"page_obj": page_obj},
    )


def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    return render(
        request,
        "notatnik/note_detail.html",
        {"note": note},
    )