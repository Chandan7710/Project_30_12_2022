from django.db import models

# Create your models here.

class Musician(models.Model):
    '''The bolow field will be automatically created by the django models by default'''
    # id = models.AutoField(Primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    
class Album(models.Model):
    '''The bolow field will be automatically created by the django models by default'''
    # id = models.AutoField(Primary_key=True)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    release_date = models.DateField()
    
    # It is similar to html code as below
    # <select>
    # <option value = "">Worst</option>
    
    rating =(
    (1, "Worst"),
    (2, "Bad"),
    (3, "Not Bad"),
    (4, "Good"),
    (5, "Excellent"),
    )
    
    num_stars = models.IntegerField(choices=rating)
    
    # class Meta:
        # db_table = "album"
    
    def __str__(self):
        return self.name + " Rating - " + str(self.num_stars)