from django.db import models
from django.utils import timezone
#from PyPDF2 import PdfFileReader, PdfFileWriter
import os
    
class Livre(models.Model):
    owner = models.ForeignKey("base.Profil", null=True, related_name="auteur", on_delete=models.SET_NULL)
    maison = models.CharField(max_length=30, verbose_name="maison d'edition")
    titre = models.CharField(max_length=30, verbose_name="titre du livre")
    categorie = models.ForeignKey("Categorie", null=True, on_delete=models.SET_NULL)
    cover = models.ImageField(upload_to="librairie/covers")
    description = models.TextField(verbose_name="le contenue du livre")
    annee = models.DateField(default=timezone.now)
    contributeurs = models.ManyToManyField("base.Profil", through='Contribution')
    prix = models.IntegerField(verbose_name="prix")
    livre = models.FileField(upload_to="librairie/livres", default = 0)
    thumbnail = models.FileField(null=True, upload_to="librairie/livres")  
    version = models.IntegerField(verbose_name="version du livre")
    slug = models.SlugField(unique=True, max_length=30)

    def save(self, *args, **kwargs):
        self.thumbnail.name = "librairie/livres/"+self.thumbName()
        super(Livre, self).save(*args, **kwargs)
        print("===== thumb =====", self.thumbnail.url)
        self.generateThumbPdf()

    def generateThumbPdf(self):
        thumb_dir = os.path.dirname(self.livre.path)
        thumbName = os.path.basename(self.thumbnail.name)
        thumbfile = os.path.join(thumb_dir, thumbName)
        file = open(self.livre.path, 'rb')
        output = PdfFileWriter()
        pdfOne = PdfFileReader(file)
        for i in range(10):
            output.addPage(pdfOne.getPage(i))
        pdf = open(thumbfile, 'ab+')
        output.write(pdf)
        pdf.close()

    def thumbName(self):
        thumb_name, thumb_extension = os.path.splitext(self.livre.name)
        thumb_extension = thumb_extension.lower()
        thumb_filename = thumb_name + '_thumb' + thumb_extension
        return thumb_filename
                
    def __str__(self):
        return f"{self.titre} {self.version} {self.annee}"
