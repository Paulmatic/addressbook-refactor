from django.db import models
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField

class Contact(models.Model):
    first_name = models.CharField(max_length=50, db_index=True)
    last_name = models.CharField(max_length=50, db_index=True)
    phone_number = models.CharField(max_length=15, db_index=True)
    email = models.EmailField(db_index=True)
    address = models.TextField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    search_vector = SearchVectorField(null=True, blank=True)
    
    class Meta:
        indexes = [
            GinIndex(fields=['search_vector']),
            GinIndex(fields=['first_name', 'last_name']),
        ]
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from django.db import transaction
        transaction.on_commit(lambda: self.update_search_vector())
    
    def update_search_vector(self):
        from django.contrib.postgres.search import SearchVector
        Contact.objects.filter(pk=self.pk).update(
            search_vector=SearchVector('first_name', 'last_name', 'email', 'address', 'phone_number')
        )
