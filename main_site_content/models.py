from django.db import models
from django.core.validators import MaxValueValidator
from fontawesome.fields import IconField
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
import uuid


SOCIAL_URL_HELP_TEXT = '{} URL of your business (leave blank to omit icon from site)'
BACKGROUND_IMAGE_HELP_TEXT = '{section} background image{extra}'


class MainSiteContent(models.Model):
    """
    Defines fields for managing static site content, e.g. header wording, 'about me' skills, etc. Intended to be used
    as a single-row table, but can be used as a multi-row table for site versioning.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    # Global content
    name = models.CharField(
        max_length=100,
        help_text='Name this version of your static site content. Only one version is expected to be used, but you may '
                  'create additional versions in the future if desired',
        null=True
    )
    business_name = models.CharField(
        max_length=100,
        help_text='Add a business name. Will appear in copyright, purchase forms, etc'
    )
    logo = models.ImageField(
        help_text='Add a logo. This image is displayed at the top of the navigation',
        null=True
    )

    # Social links
    facebook_url = models.URLField(
        help_text=SOCIAL_URL_HELP_TEXT.format('Facebook'),
        null=True,
        blank=True
    )
    twitter_url = models.URLField(
        help_text=SOCIAL_URL_HELP_TEXT.format('Twitter'),
        null=True,
        blank=True
    )
    dribbble_url = models.URLField(
        help_text=SOCIAL_URL_HELP_TEXT.format('Dribbble'),
        null=True,
        blank=True
    )
    google_plus_url = models.URLField(
        help_text=SOCIAL_URL_HELP_TEXT.format('Google+'),
        null=True,
        blank=True
    )
    instagram_url = models.URLField(
        help_text=SOCIAL_URL_HELP_TEXT.format('Instagram'),
        null=True,
        blank=True
    )

    # "Home" section
    home_background_image = models.ImageField(
        help_text=BACKGROUND_IMAGE_HELP_TEXT.format(
            section='"Home"',
            extra=': the first image seen by visitors'
        ),
        verbose_name='Background image',
        null=True
    )
    home_header_1 = models.CharField(
        max_length=50,
        help_text='First header on the "Home" section (leave blank to ignore)',
        verbose_name='Header 1',
        blank=True
    )
    home_header_2 = models.CharField(
        max_length=50,
        help_text='Second header on the "Home" section (leave blank to ignore)',
        verbose_name='Header 2',
        blank=True
    )
    home_header_3 = models.CharField(
        max_length=50,
        help_text='Third header on the "Home" section (leave blank to ignore)',
        verbose_name='Header 3',
        blank=True
    )
    home_paragraph = models.CharField(
        max_length=50,
        help_text='Paragraph on the "Home" section, below headers (leave blank to ignore)',
        verbose_name='Additional paragraph',
        blank=True
    )
    home_button_text = models.CharField(
        max_length=50,
        help_text='Button on the "Home" section, below headers and paragraph (leave blank to ignore)',
        verbose_name='Button text',
        blank=True
    )
    home_button_link = models.CharField(
        max_length=50,
        help_text='Link used by the button on the "Home" section, below headers and paragraph (leave blank to ignore)',
        verbose_name='Button link',
        choices=(
            ('about', 'About'),
            ('services', 'Services'),
            ('portfolio', 'Portfolio'),
            ('blog', 'Blog'),
            ('contact', 'Contact'),
        ),
        blank=True
    )

    # "About" section
    about_background_image = models.ImageField(
        help_text=BACKGROUND_IMAGE_HELP_TEXT.format(
            section='"About"',
            extra=''
        ),
        verbose_name='Background image',
        null=True
    )
    about_paragraph = models.TextField(
        help_text='Paragraph on the "About" section (leave blank to ignore)',
        verbose_name='Paragraph',
        null=True,
        blank=True
    )
    about_quote = models.TextField(
        help_text='Quote on the "About" section (leave blank to ignore)',
        verbose_name='Quote',
        null=True,
        blank=True
    )
    about_button_text = models.CharField(
        max_length=50,
        help_text='Button on the "About" section, below paragraph and quote (leave blank to ignore)',
        verbose_name='Button text',
        blank=True
    )
    about_button_link = models.CharField(
        max_length=50,
        help_text='Link used by the button on the "About" section, below paragraph and quote (leave blank to ignore)',
        verbose_name='Button link',
        choices=(
            ('home', 'Home'),
            ('services', 'Services'),
            ('portfolio', 'Portfolio'),
            ('blog', 'Blog'),
            ('contact', 'Contact'),
        ),
        blank=True
    )
    about_skills_header = models.CharField(
        max_length=50,
        help_text='Header of the "Skills" component of the "About" section (leave blank to ignore)',
        verbose_name='"Skills" header',
        blank=True
    )
    about_skills_footnote = models.CharField(
        max_length=200,
        help_text='Footnote of the "Skills" component of the "About" section (leave blank to ignore)',
        verbose_name='"Skills" footnote',
        blank=True
    )

    # "Services" section
    services_background_image = models.ImageField(
        help_text=BACKGROUND_IMAGE_HELP_TEXT.format(
            section='"Services"',
            extra=''
        ),
        verbose_name='Background image',
        null=True
    )
    services_left_subsection_header = models.CharField(
        max_length=25,
        help_text='Header of the "Our Services" (left) sub-section of "Services" (add Services to populate)',
        verbose_name='Left sub-section header',
        blank=True
    )
    services_middle_subsection_header = models.CharField(
        max_length=25,
        help_text='Header of the "What We Do" (middle) sub-section of "Services" (add Skills to populate)',
        verbose_name='Middle sub-section header',
        blank=True
    )
    services_right_subsection_header = models.CharField(
        max_length=25,
        help_text='Header of the "Our Partners" (right) sub-section of "Services" (add Partners to populate)',
        verbose_name='Right sub-section header',
        blank=True
    )

    # "Portfolio" section
    portfolio_background_image = models.ImageField(
        help_text=BACKGROUND_IMAGE_HELP_TEXT.format(
            section='"Portfolio"',
            extra=''
        ),
        verbose_name='Background image',
        null=True
    )

    # "Blog" section
    blog_background_image = models.ImageField(
        help_text=BACKGROUND_IMAGE_HELP_TEXT.format(
            section='"Blog"',
            extra=''
        ),
        verbose_name='Background image',
        null=True
    )

    # "Contact" section
    contact_background_image = models.ImageField(
        help_text=BACKGROUND_IMAGE_HELP_TEXT.format(
            section='"Contact"',
            extra=''
        ),
        verbose_name='Background image',
        null=True
    )
    contact_address_street_1 = models.CharField(
        max_length=100,
        verbose_name='Street address (line 1)',
        blank=True
    )
    contact_address_street_2 = models.CharField(
        max_length=100,
        verbose_name='Street address (line 2)',
        blank=True
    )
    contact_address_city = models.CharField(
        max_length=50,
        verbose_name='City',
        blank=True
    )
    contact_address_state_or_province = models.CharField(
        max_length=50,
        verbose_name='State/Province',
        blank=True
    )
    contact_address_postal_code = models.CharField(
        max_length=50,
        verbose_name='ZIP/Postal Code',
        blank=True
    )
    contact_address_country = CountryField(
        verbose_name='Country',
        null=True,
        blank=True
    )
    contact_phone = PhoneNumberField(
        verbose_name='Phone',
        blank=True
    )
    contact_email = models.EmailField(
        verbose_name='Email',
        blank=True
    )
    contact_footnote = models.CharField(
        help_text='Displays with an asterisk (*) below the contact form',
        verbose_name='Footnote',
        blank=True
    )


class Service(models.Model):
    """
    A service rendered in the "Services" section carousel
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    icon = IconField()


class Skill(models.Model):
    """
    A skill rendered in the "About" and "Services" sections
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=50,
        null=True
    )
    progress = models.PositiveIntegerField(
        validators=(
            MaxValueValidator(limit_value=100),
        ),
        help_text='Percent progress of skill (1-100)',
        null=True
    )


class Partner(models.Model):
    """
    A partner rendered in the "Services" section
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=100,
        null=True
    )
    image = models.ImageField(
        help_text='Template image dimensions are 208x39'
    )
    link = models.URLField()
