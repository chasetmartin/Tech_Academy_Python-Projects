from django.db import models


# Create UniversityCampus Model
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    campus_state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(default="", blank=True, null=False)

    # create model manager
    object = models.Manager()

    # displays the object output values in the form of a string
    def __str__(self):
        # Return the input value of the campus_name and campus_state
        # fields as a tuple to display in the browser instead of the default titles
        display_campus = '{0.campus_name}: {0.campus_state}'
        return display_campus.format(self)

    # Remove added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus"