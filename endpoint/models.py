from django.db import models
import datetime
# from datetime import datetime
import pytz
from datetime import datetime
import calendar


class Endpoint(models.Model):
    slack_name = models.CharField(max_length=50)
    current_day = models.CharField(max_length=50)
    utc_time = models.DateTimeField(datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
    track = models.CharField(max_length=100)
    github_file_url = models.CharField(max_length=100)
    github_repo_url = models.CharField(max_length=50)
    status_code = models.IntegerField(default=200)