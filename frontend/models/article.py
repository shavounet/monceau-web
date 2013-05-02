from django.db import models

class Article(models.Model):
    title = "test"
    description = """Ceci est un Article.
    
    Et je peux même sauter des lignes !
    """