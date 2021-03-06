# Generated by Django 2.1.5 on 2019-01-24 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destroyer', '0004_auto_20190124_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='destroyer',
            name='initial_language',
            field=models.CharField(choices=[('af', 'Afrikaans'), ('sq', 'Albanian'), ('am', 'Amharic'), ('ar', 'Arabic'), ('hy', 'Armenian'), ('az', 'Azerbaijani'), ('eu', 'Basque'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('bs', 'Bosnian'), ('bg', 'Bulgarian'), ('ca', 'Catalan / Valencian'), ('ceb', 'Cebuano'), ('ny', 'Chichewa / Chewa / Nyanja'), ('zh', 'Chinese'), ('co', 'Corsican'), ('hr', 'Croatian'), ('cs', 'Czech'), ('da', 'Danish'), ('nl', 'Dutch / Flemish'), ('en', 'English'), ('eo', 'Esperanto'), ('et', 'Estonian'), ('fil', 'Filipino / Pilipino'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('gl', 'Galician'), ('ka', 'Georgian'), ('de', 'German'), ('el', 'Modern Greek'), ('gu', 'Gujarati'), ('ht', 'Haitian'), ('ha', 'Hausa'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hu', 'Hungarian'), ('is', 'Icelandic'), ('ig', 'Igbo'), ('id', 'Indonesian'), ('ga', 'Irish'), ('it', 'Italian'), ('ja', 'Japanese'), ('jv', 'Javanese'), ('kn', 'Kannada'), ('kk', 'Kazakh'), ('km', 'Central Khmer'), ('ko', 'Korean'), ('ku', 'Kurdish'), ('ky', 'Kirghiz / Kyrgyz'), ('lo', 'Lao'), ('la', 'Latin'), ('lv', 'Latvian'), ('lt', 'Lithuanian'), ('lb', 'Luxembourgish / Letzeburgesch'), ('mk', 'Macedonian'), ('mg', 'Malagasy'), ('ms', 'Malay'), ('ml', 'Malayalam'), ('mt', 'Maltese'), ('mi', 'Maori'), ('mr', 'Marathi'), ('mn', 'Mongolian'), ('my', 'Burmese'), ('ne', 'Nepali'), ('no', 'Norwegian'), ('ps', 'Pushto / Pashto'), ('fa', 'Persian'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pa', 'Panjabi / Punjabi'), ('ro', 'Romanian / Moldavian / Moldovan'), ('ru', 'Russian'), ('sm', 'Samoan'), ('gd', 'Gaelic / Scottish Gaelic'), ('sr', 'Serbian'), ('st', 'Southern Sotho'), ('sn', 'Shona'), ('sd', 'Sindhi'), ('si', 'Sinhala / Sinhalese'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('so', 'Somali'), ('es', 'Spanish / Castilian'), ('su', 'Sundanese'), ('sw', 'Swahili'), ('sv', 'Swedish'), ('tg', 'Tajik'), ('ta', 'Tamil'), ('te', 'Telugu'), ('th', 'Thai'), ('tr', 'Turkish'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('vi', 'Vietnamese'), ('cy', 'Welsh'), ('xh', 'Xhosa'), ('yi', 'Yiddish'), ('yo', 'Yoruba'), ('zu', 'Zulu')], default=('en', 'English'), max_length=3),
        ),
        migrations.AddField(
            model_name='destroyer',
            name='input',
            field=models.TextField(default='Hello, world!', verbose_name='Text to destroy'),
        ),
        migrations.AddField(
            model_name='destroyer',
            name='output',
            field=models.TextField(default='Station station', verbose_name='Result'),
        ),
    ]
