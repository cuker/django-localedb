# -*- coding: utf-8 -*-

from south.db import db
from django.db import models
from localedb.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'Locale.grouping'
        # (to signature: django.db.models.fields.CommaSeparatedIntegerField(max_length=256, blank=True))
        db.alter_column('localedb_locale', 'grouping', orm['localedb.locale:grouping'])
        
    
    
    def backwards(self, orm):
        
        # Changing field 'Locale.grouping'
        # (to signature: django.db.models.fields.CharField(max_length=256, blank=True))
        db.alter_column('localedb_locale', 'grouping', orm['localedb.locale:grouping'])
        
    
    
    models = {
        'localedb.locale': {
            'abday_1': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'abday_2': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'abday_3': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'abday_4': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'abday_5': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'abday_6': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'abday_7': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'abmon_1': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'abmon_10': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'abmon_11': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'abmon_12': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'abmon_2': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'abmon_3': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'abmon_4': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'abmon_5': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'abmon_6': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'abmon_7': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'abmon_8': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'abmon_9': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'alt_digits': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'codeset': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'currency_symbol': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'd_fmt': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'd_t_fmt': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'day_1': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'day_2': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'day_3': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'day_4': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'day_5': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'day_6': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'day_7': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'decimal_point': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'era': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'era_d_fmt': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'era_d_t_fmt': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'era_year': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'frac_digits': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'grouping': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '256', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'int_curr_symbol': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'int_frac_digits': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'mon_1': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mon_10': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mon_11': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mon_12': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mon_2': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mon_3': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mon_4': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mon_5': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mon_6': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mon_7': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mon_8': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mon_9': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mon_decimal_point': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'mon_grouping': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'mon_thousands_sep': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'n_cs_precedes': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'n_sep_by_space': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'n_sign_posn': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'negative_sign': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'noexpr': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'p_cs_precedes': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'p_sep_by_space': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'p_sign_posn': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'positive_sign': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            't_fmt': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            't_fmt_ampm': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'thousands_sep': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'yesexpr': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'localedb.localesitedefault': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locale': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localedb.Locale']"}),
            'site': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['sites.Site']", 'unique': 'True'})
        },
        'sites.site': {
            'Meta': {'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['localedb']
