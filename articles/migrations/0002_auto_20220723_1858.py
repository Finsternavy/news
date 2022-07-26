# Generated by Django 4.0.6 on 2022-07-23 18:58

from django.db import migrations

def populate_sections(apps, schemaeditor):
    sections = {
        "front_page": "Front page articles (headliners)",
        "sports": "Sports related content",
        "business": "Business related content",
        "society": "Society related content",
        "politics": "Politics related content",
    }
    Section = apps.get_model("articles", "Section")
    for name, desc in sections.items():
        section_obj = Section(name=name, description=desc)
        section_obj.save()

def populate_article_types(apps, schemaeditor):
    art_types = {
        "article": "Original research manuscripts",
        "brief_report": "Short, observational studies",
        "editorial": "Opinion piece",
        "column": "An opinion piece on specific topic",
    }
    ArticleType = apps.get_model("articles", "ArticleType")
    for name, desc in art_types.items():
        at_obj = ArticleType(name=name, description=desc)
        at_obj.save()

def populate_status(apps, schemaeditor):
    status = {
        "Published": "Article published",
        "Pending Review": "Article under review",
        "Revision Requested": "Sent back to writer for revision",
        "Denied": "Article denied",
        "Draft": "Article being worked on",
    }
    Status = apps.get_model("articles", "Status")
    for name, desc in status.items():
        status_obj = Status(name=name, description=desc)
        status_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_sections),
        migrations.RunPython(populate_article_types),
        migrations.RunPython(populate_status),
    ]
