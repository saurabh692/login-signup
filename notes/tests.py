from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Note


class NoteModelTest(TestCase):
    """Test the Note model"""
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
    
    def test_create_note(self):
        """Test creating a note"""
        note = Note.objects.create(
            user=self.user,
            title='Test Note',
            content='This is a test note'
        )
        self.assertEqual(note.title, 'Test Note')
        self.assertEqual(note.content, 'This is a test note')
        self.assertFalse(note.is_pinned)
    
    def test_pin_note(self):
        """Test pinning a note"""
        note = Note.objects.create(
            user=self.user,
            title='Test Note',
            content='This is a test note'
        )
        note.is_pinned = True
        note.save()
        self.assertTrue(note.is_pinned)


class NoteViewTest(TestCase):
    """Test the Note views"""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
    
    def test_notes_list_view_requires_login(self):
        """Test that notes list view requires login"""
        response = self.client.get('/notes/')
        self.assertEqual(response.status_code, 302)
    
    def test_add_note_view_requires_login(self):
        """Test that add note view requires login"""
        response = self.client.get('/notes/add/')
        self.assertEqual(response.status_code, 302)
