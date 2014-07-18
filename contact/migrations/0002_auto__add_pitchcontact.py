# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PitchContact'
        db.create_table(u'contact_pitchcontact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('overview', self.gf('django.db.models.fields.TextField')()),
            ('business_model', self.gf('django.db.models.fields.TextField')()),
            ('mvp', self.gf('django.db.models.fields.TextField')()),
            ('company_details', self.gf('django.db.models.fields.TextField')()),
            ('project_plan', self.gf('django.db.models.fields.TextField')()),
            ('dev_calendar', self.gf('django.db.models.fields.TextField')()),
            ('middle_person', self.gf('django.db.models.fields.TextField')()),
            ('timezone', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'contact', ['PitchContact'])


    def backwards(self, orm):
        # Deleting model 'PitchContact'
        db.delete_table(u'contact_pitchcontact')


    models = {
        u'contact.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'contact.pitchcontact': {
            'Meta': {'object_name': 'PitchContact'},
            'business_model': ('django.db.models.fields.TextField', [], {}),
            'company_details': ('django.db.models.fields.TextField', [], {}),
            'dev_calendar': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'middle_person': ('django.db.models.fields.TextField', [], {}),
            'mvp': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'overview': ('django.db.models.fields.TextField', [], {}),
            'project_plan': ('django.db.models.fields.TextField', [], {}),
            'timezone': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['contact']