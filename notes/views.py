from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Note


def notes_list(request):
    """Display all notes"""
    notes = Note.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': notes})


def add_note(request):
    """Add a new note"""
    if request.method == 'POST':
        title = request.POST.get('title', 'Untitled Note')
        content = request.POST.get('content', '')
        
        # Create a default user or use the first one
        from django.contrib.auth.models import User
        user = User.objects.first() or User.objects.create_user(username='default', password='temp')
        
        Note.objects.create(
            user=user,
            title=title,
            content=content
        )
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            notes = Note.objects.filter(user=request.user)
            return JsonResponse({
                'status': 'success',
                'message': 'Note added successfully'
            })
        
        return redirect('notes_list')
    
    return render(request, 'notes/add_note.html')


def delete_note(request, note_id):
    """Delete a note"""
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success', 'message': 'Note deleted'})
    
    return redirect('notes_list')


def pin_note(request, note_id):
    """Toggle pin status of a note"""
    note = get_object_or_404(Note, id=note_id)
    note.is_pinned = not note.is_pinned
    note.save()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'success',
            'is_pinned': note.is_pinned
        })
    
    return redirect('notes_list')


def edit_note(request, note_id):
    """Edit a note"""
    note = get_object_or_404(Note, id=note_id)
    
    if request.method == 'POST':
        note.title = request.POST.get('title', note.title)
        note.content = request.POST.get('content', note.content)
        note.save()
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success', 'message': 'Note updated'})
        
        return redirect('notes_list')
    
    return render(request, 'notes/edit_note.html', {'note': note})
