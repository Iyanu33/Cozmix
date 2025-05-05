from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import SiteLogo, Banner, SiteInfo, Footer,SocialMedia

admin.site.register(SiteLogo)
admin.site.register(Banner)
admin.site.register(SiteInfo)
admin.site.register(Footer)
admin.site.register(SocialMedia)
