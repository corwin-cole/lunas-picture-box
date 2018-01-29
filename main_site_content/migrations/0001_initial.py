# Generated by Django 2.0.1 on 2018-01-29 00:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import fontawesome.fields
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainSiteContent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name this version of your static site content. Only one version is expected to be used, but you may create additional versions in the future if desired', max_length=100, null=True)),
                ('business_name', models.CharField(help_text='Add a business name. Will appear in copyright, purchase forms, etc', max_length=100)),
                ('logo', models.ImageField(help_text='Add a logo. This image is displayed at the top of the navigation', null=True, upload_to='')),
                ('facebook_url', models.URLField(blank=True, help_text='Facebook URL of your business (leave blank to omit icon from site)', null=True)),
                ('twitter_url', models.URLField(blank=True, help_text='Twitter URL of your business (leave blank to omit icon from site)', null=True)),
                ('dribbble_url', models.URLField(blank=True, help_text='Dribbble URL of your business (leave blank to omit icon from site)', null=True)),
                ('google_plus_url', models.URLField(blank=True, help_text='Google+ URL of your business (leave blank to omit icon from site)', null=True)),
                ('instagram_url', models.URLField(blank=True, help_text='Instagram URL of your business (leave blank to omit icon from site)', null=True)),
                ('home_background_image', models.ImageField(help_text='"Home" background image: the first image seen by visitors', null=True, upload_to='', verbose_name='Background image')),
                ('home_header_1', models.CharField(blank=True, help_text='First header on the "Home" section (leave blank to ignore)', max_length=50, verbose_name='Header 1')),
                ('home_header_2', models.CharField(blank=True, help_text='Second header on the "Home" section (leave blank to ignore)', max_length=50, verbose_name='Header 2')),
                ('home_header_3', models.CharField(blank=True, help_text='Third header on the "Home" section (leave blank to ignore)', max_length=50, verbose_name='Header 3')),
                ('home_paragraph', models.CharField(blank=True, help_text='Paragraph on the "Home" section, below headers (leave blank to ignore)', max_length=50, verbose_name='Additional paragraph')),
                ('home_button_text', models.CharField(blank=True, help_text='Button on the "Home" section, below headers and paragraph (leave blank to ignore)', max_length=50, verbose_name='Button text')),
                ('home_button_link', models.CharField(blank=True, choices=[('about', 'About'), ('services', 'Services'), ('portfolio', 'Portfolio'), ('blog', 'Blog'), ('contact', 'Contact')], help_text='Link used by the button on the "Home" section, below headers and paragraph (leave blank to ignore)', max_length=50, verbose_name='Button link')),
                ('about_background_image', models.ImageField(help_text='"About" background image', null=True, upload_to='', verbose_name='Background image')),
                ('about_paragraph', models.TextField(blank=True, help_text='Paragraph on the "About" section (leave blank to ignore)', null=True, verbose_name='Paragraph')),
                ('about_quote', models.TextField(blank=True, help_text='Quote on the "About" section (leave blank to ignore)', null=True, verbose_name='Quote')),
                ('about_button_text', models.CharField(blank=True, help_text='Button on the "About" section, below paragraph and quote (leave blank to ignore)', max_length=50, verbose_name='Button text')),
                ('about_button_link', models.CharField(blank=True, choices=[('home', 'Home'), ('services', 'Services'), ('portfolio', 'Portfolio'), ('blog', 'Blog'), ('contact', 'Contact')], help_text='Link used by the button on the "About" section, below paragraph and quote (leave blank to ignore)', max_length=50, verbose_name='Button link')),
                ('about_skills_header', models.CharField(blank=True, help_text='Header of the "Skills" component of the "About" section (leave blank to ignore)', max_length=50, verbose_name='"Skills" header')),
                ('about_skills_footnote', models.CharField(blank=True, help_text='Footnote of the "Skills" component of the "About" section (leave blank to ignore)', max_length=200, verbose_name='"Skills" footnote')),
                ('services_background_image', models.ImageField(help_text='"Services" background image', null=True, upload_to='', verbose_name='Background image')),
                ('services_left_subsection_header', models.CharField(blank=True, help_text='Header of the "Our Services" (left) sub-section of "Services" (add Services to populate)', max_length=25, verbose_name='Left sub-section header')),
                ('services_middle_subsection_header', models.CharField(blank=True, help_text='Header of the "What We Do" (middle) sub-section of "Services" (add Skills to populate)', max_length=25, verbose_name='Middle sub-section header')),
                ('services_right_subsection_header', models.CharField(blank=True, help_text='Header of the "Our Partners" (right) sub-section of "Services" (add Partners to populate)', max_length=25, verbose_name='Right sub-section header')),
                ('portfolio_background_image', models.ImageField(help_text='"Portfolio" background image', null=True, upload_to='', verbose_name='Background image')),
                ('blog_background_image', models.ImageField(help_text='"Blog" background image', null=True, upload_to='', verbose_name='Background image')),
                ('contact_background_image', models.ImageField(help_text='"Contact" background image', null=True, upload_to='', verbose_name='Background image')),
                ('contact_address_street_1', models.CharField(blank=True, max_length=100, verbose_name='Street address (line 1)')),
                ('contact_address_street_2', models.CharField(blank=True, max_length=100, verbose_name='Street address (line 2)')),
                ('contact_address_city', models.CharField(blank=True, max_length=50, verbose_name='City')),
                ('contact_address_state_or_province', models.CharField(blank=True, max_length=50, verbose_name='State/Province')),
                ('contact_address_postal_code', models.CharField(blank=True, max_length=50, verbose_name='ZIP/Postal Code')),
                ('contact_address_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True, verbose_name='Country')),
                ('contact_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, verbose_name='Phone')),
                ('contact_email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('contact_footnote', models.CharField(blank=True, help_text='Displays with an asterisk (*) below the contact form', max_length=200, verbose_name='Footnote')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(help_text='Template image dimensions are 208x39', upload_to='')),
                ('link', models.URLField()),
                ('main_site_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site_content.MainSiteContent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('icon', fontawesome.fields.IconField(blank=True, max_length=60)),
                ('main_site_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site_content.MainSiteContent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('progress', models.PositiveIntegerField(help_text='Percent progress of skill (1-100)', null=True, validators=[django.core.validators.MaxValueValidator(limit_value=100)])),
                ('main_site_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site_content.MainSiteContent')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
