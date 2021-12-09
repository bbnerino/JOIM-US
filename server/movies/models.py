from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    adult = models.BooleanField()
    backdrop_path = models.TextField()
    iden = models.IntegerField()
    original_language = models.TextField()
    original_title = models.TextField()
    video = models.BooleanField()
    genres = models.ManyToManyField(Genre, related_name='movies')

    def __str__(self):
        return self.title

class Actor(models.Model):
    actor_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    profile_path = models.TextField()
    
    adventure = models.IntegerField(default=0, null=True)
    fantasy = models.IntegerField(default=0, null=True)
    animation = models.IntegerField(default=0, null=True)
    drama = models.IntegerField(default=0, null=True)
    horror = models.IntegerField(default=0, null=True)
    action = models.IntegerField(default=0, null=True)
    comedy = models.IntegerField(default=0, null=True)
    historic = models.IntegerField(default=0, null=True)
    western = models.IntegerField(default=0, null=True)
    thriller = models.IntegerField(default=0, null=True)
    criminal = models.IntegerField(default=0, null=True)
    documentary = models.IntegerField(default=0, null=True)
    sf = models.IntegerField(default=0, null=True)
    mystery = models.IntegerField(default=0, null=True)
    music = models.IntegerField(default=0, null=True)
    romance = models.IntegerField(default=0, null=True)
    family = models.IntegerField(default=0, null=True)
    millitary = models.IntegerField(default=0, null=True)
    tv = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.name