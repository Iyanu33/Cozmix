from .models import SiteLogo, Banner, SiteInfo, Footer

def site_settings(request):
    logo = SiteLogo.objects.first()
    banners = Banner.objects.all()
    site_info = SiteInfo.objects.first()
    footer = Footer.objects.first()
    return {
        'site_logo': logo,
        'banners': banners,
        'site_info': site_info,
        'footer': footer,
    }
