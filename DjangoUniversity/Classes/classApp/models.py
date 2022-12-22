from django.db import models


# Create model of University Classes
class UniversityClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField(default="", blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(null=True, blank=True, default=None)

    # create model manager
    object = models.Manager()

    # displays the object output values in the form of a string
    def __str__(self):
        # Return the input value of the title and instructor name
        # fields as a tuple to display in the browser instead of the default titles
        display_course = '{0.title}: {0.instructor_name}'
        return display_course.format(self)

    # Remove added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Classes"
