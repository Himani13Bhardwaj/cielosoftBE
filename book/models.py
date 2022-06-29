from django.db import models
from enumchoicefield import ChoiceEnum, EnumChoiceField
from author.models import Author
from genre.models import Genre
from languages.fields import LanguageField
from account.models import Account
# Create your models here.

class State(ChoiceEnum):
    locked       = "Locked"
    unlocked     = "Un-Locked"
    free         = "Free"
    bonus        = "Bonus"
    
class BookStatus(ChoiceEnum):
    draft       = "Draft"
    review     = "Reviewing"
    published         = "Published"
    pending        = "Pending"

class BookDetails(models.Model):
    
    view                    = models.IntegerField(default=0)
    upvote                  = models.IntegerField(default=0)
    downvote                = models.IntegerField(default=0)
    

    def __str__(self):
        return str(self.view)

    
class Books(models.Model):
    book_name               = models.CharField(max_length=254)
    book_cover_url          = models.ImageField(upload_to = 'static/books', default = '')
    chapters                = models.IntegerField(default=0)
    view                    = models.IntegerField(default=0)
    published_time          = models.DateField(blank=True, null=True)
    user_count              = models.IntegerField(default=0)
    ranking                 = models.IntegerField(default=0)
    book_brief_info         = models.CharField(max_length=1024)
    genre                   = models.ForeignKey(Genre, on_delete=models.CASCADE, default=None)
    # author                  = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    author                  = models.ForeignKey(Author, related_name='books' ,on_delete=models.CASCADE, default=None)
    book_details            = models.OneToOneField(BookDetails, on_delete=models.CASCADE, default=1)
    language                = LanguageField(default='en', max_length=100)
    status                  = EnumChoiceField(enum_class=BookStatus , default=BookStatus.draft)
    bookmark                = models.ManyToManyField(Account, blank=True)
    book_preface            = models.FileField(upload_to = 'static/book_preface', default = '')
    book_copyright          = models.FileField(upload_to = 'static/book_copyright', default = '')
    book_acknowledgement    = models.FileField(upload_to = 'static/book_acknowledgement', default = '')
    policy_agreement        = models.BooleanField(default=False)
    def __str__(self):
        return self.book_name

class Chapter(models.Model):

    chapter_no              = models.PositiveIntegerField(null=True, blank=True)
    chapter_name            = models.CharField(max_length=100)
    chapter_url             = models.FileField(upload_to = 'static/chapters', default = '')
    state                   = EnumChoiceField(enum_class=State , default=State.free)
    book_id                 = models.ForeignKey(Books, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.chapter_name
