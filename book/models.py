from django.db import models
class Book(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField(upload_to='bookImages')
    author = models.CharField(max_length = 30, default="Chetan Bhagat..")
    email = models.EmailField(blank = True)
    describe = models.TextField(default = "Library for various books")
    book_soft_copy = models.FileField(upload_to='bookSoftcopy')
    
    def __str__(self):
        return self.name
