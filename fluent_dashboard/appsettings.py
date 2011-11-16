"""
Overview of all settings which can be customized.
"""
from django.conf import settings
from django.utils.translation import ugettext as _

FLUENT_DASHBOARD_ICON_THEME = getattr(settings, "FLUENT_DASHBOARD_ICON_THEME", "oxygen")

# The icon names are somewhat Oxygen specific,
# yet based on the Freedesktop Naming Naming Specification.

FLUENT_DASHBOARD_APP_ICONS = {
    'cms/page': 'internet-web-browser.png',
    'snippet/snippet': 'folder-txt.png',
    'filer/folder': 'folder.png',
    'fiber/page': 'internet-web-browser.png',
    'fiber/contentitem': 'folder-txt.png',
    'fiber/image': 'folder-image.png',
    'fiber/file': 'folder.png',
    'ecms/cmsobject': 'internet-web-browser.png',
    'ecms/cmslayout': 'view-choose.png',
    'ecms/cmssite': 'preferences-system-network.png',
    'ecms_media/file': 'folder.png',
    'form_designer/formdefinition': 'mail-mark-task.png',
    'form_designer/formlog': 'view-calendar-journal.png',
    'zinnia/entry': 'view-calendar-journal.png',
    'zinnia/category': 'folder-bookmark.png',
    'comments/comment': 'kde-telepathy.png', #'irc-voice.png',
    'threadedcomments/threadedcomment': 'kde-telepathy.png', #'irc-voice.png',
    'tagging/tag': 'feed-subscribe.png',
    'tagging/taggeditem': 'feed-subscribe.png',
    'auth/user':  'system-users.png',
    'auth/group': 'resource-group.png',
    'google_analytics/analytics': 'view-statistics.png',
    'sites/site': 'applications-internet.png',
    'registration/registrationprofile': 'list-add-user.png'
}

FLUENT_DASHBOARD_DEFAULT_ICON = getattr(settings, "FLUENT_DASHBOARD_DEFAULT_ICON", 'unknown.png')

FLUENT_DASHBOARD_APP_ICONS.update(getattr(settings, 'FLUENT_DASHBOARD_APP_ICONS', {}))

FLUENT_DASHBOARD_APP_GROUPS = getattr(settings, 'FLUENT_DASHBOARD_APP_GROUPS', (
    (_('CMS'), {
        'models': [
            "{0}.*".format(app) for app in FLUENT_DASHBOARD_CMS_APP_NAMES
        ],
        'module': 'fluent_dashboard.modules.CmsAppIconList',
        'collapsible': False,
    }),
    (_('Interactivity'), {
        'models': (
            'django.contrib.comments.*',
            'form_designer.*',
            'threadedcomments.*',
            'zinnia.*',
        ),
        'module': 'fluent_dashboard.modules.AppIconList',
        'collapsible': False,
    }),
    (_('Administration'), {
        'models': (
            'django.contrib.auth.*',
            'django.contrib.sites.*',
            'registration.*',
            'google_analytics.*',
        ),
        'module': 'fluent_dashboard.modules.AppIconList',
        'collapsible': False,
    }),
    (_('Applications'), {
        'models': ('*',),
        'module': 'admin_tools.dashboard.modules.AppList',
        'collapsible': False,
    }),
    #(_('Developer tools'), ()),
))