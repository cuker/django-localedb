# -*- coding: utf-8 -*-

from south.db import db
from django.db import models
from localedb.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'LocaleSiteDefault'
        db.create_table('localedb_localesitedefault', (
            ('id', orm['localedb.LocaleSiteDefault:id']),
            ('site', orm['localedb.LocaleSiteDefault:site']),
            ('locale', orm['localedb.LocaleSiteDefault:locale']),
        ))
        db.send_create_signal('localedb', ['LocaleSiteDefault'])
        
        # Adding model 'Locale'
        db.create_table('localedb_locale', (
            ('id', orm['localedb.Locale:id']),
            ('name', orm['localedb.Locale:name']),
            ('mon_decimal_point', orm['localedb.Locale:mon_decimal_point']),
            ('mon_thousands_sep', orm['localedb.Locale:mon_thousands_sep']),
            ('mon_grouping', orm['localedb.Locale:mon_grouping']),
            ('currency_symbol', orm['localedb.Locale:currency_symbol']),
            ('int_curr_symbol', orm['localedb.Locale:int_curr_symbol']),
            ('int_frac_digits', orm['localedb.Locale:int_frac_digits']),
            ('p_sep_by_space', orm['localedb.Locale:p_sep_by_space']),
            ('n_sep_by_space', orm['localedb.Locale:n_sep_by_space']),
            ('thousands_sep', orm['localedb.Locale:thousands_sep']),
            ('p_sign_posn', orm['localedb.Locale:p_sign_posn']),
            ('n_sign_posn', orm['localedb.Locale:n_sign_posn']),
            ('decimal_point', orm['localedb.Locale:decimal_point']),
            ('p_cs_precedes', orm['localedb.Locale:p_cs_precedes']),
            ('n_cs_precedes', orm['localedb.Locale:n_cs_precedes']),
            ('positive_sign', orm['localedb.Locale:positive_sign']),
            ('negative_sign', orm['localedb.Locale:negative_sign']),
            ('grouping', orm['localedb.Locale:grouping']),
            ('codeset', orm['localedb.Locale:codeset']),
            ('d_t_fmt', orm['localedb.Locale:d_t_fmt']),
            ('d_fmt', orm['localedb.Locale:d_fmt']),
            ('t_fmt', orm['localedb.Locale:t_fmt']),
            ('t_fmt_ampm', orm['localedb.Locale:t_fmt_ampm']),
            ('day_1', orm['localedb.Locale:day_1']),
            ('day_2', orm['localedb.Locale:day_2']),
            ('day_3', orm['localedb.Locale:day_3']),
            ('day_4', orm['localedb.Locale:day_4']),
            ('day_5', orm['localedb.Locale:day_5']),
            ('day_6', orm['localedb.Locale:day_6']),
            ('day_7', orm['localedb.Locale:day_7']),
            ('abday_1', orm['localedb.Locale:abday_1']),
            ('abday_2', orm['localedb.Locale:abday_2']),
            ('abday_3', orm['localedb.Locale:abday_3']),
            ('abday_4', orm['localedb.Locale:abday_4']),
            ('abday_5', orm['localedb.Locale:abday_5']),
            ('abday_6', orm['localedb.Locale:abday_6']),
            ('abday_7', orm['localedb.Locale:abday_7']),
            ('mon_1', orm['localedb.Locale:mon_1']),
            ('mon_2', orm['localedb.Locale:mon_2']),
            ('mon_3', orm['localedb.Locale:mon_3']),
            ('mon_4', orm['localedb.Locale:mon_4']),
            ('mon_5', orm['localedb.Locale:mon_5']),
            ('mon_6', orm['localedb.Locale:mon_6']),
            ('mon_7', orm['localedb.Locale:mon_7']),
            ('mon_8', orm['localedb.Locale:mon_8']),
            ('mon_9', orm['localedb.Locale:mon_9']),
            ('mon_10', orm['localedb.Locale:mon_10']),
            ('mon_11', orm['localedb.Locale:mon_11']),
            ('mon_12', orm['localedb.Locale:mon_12']),
            ('abmon_1', orm['localedb.Locale:abmon_1']),
            ('abmon_2', orm['localedb.Locale:abmon_2']),
            ('abmon_3', orm['localedb.Locale:abmon_3']),
            ('abmon_4', orm['localedb.Locale:abmon_4']),
            ('abmon_5', orm['localedb.Locale:abmon_5']),
            ('abmon_6', orm['localedb.Locale:abmon_6']),
            ('abmon_7', orm['localedb.Locale:abmon_7']),
            ('abmon_8', orm['localedb.Locale:abmon_8']),
            ('abmon_9', orm['localedb.Locale:abmon_9']),
            ('abmon_10', orm['localedb.Locale:abmon_10']),
            ('abmon_11', orm['localedb.Locale:abmon_11']),
            ('abmon_12', orm['localedb.Locale:abmon_12']),
            ('yesexpr', orm['localedb.Locale:yesexpr']),
            ('noexpr', orm['localedb.Locale:noexpr']),
            ('era', orm['localedb.Locale:era']),
            ('era_year', orm['localedb.Locale:era_year']),
            ('era_d_t_fmt', orm['localedb.Locale:era_d_t_fmt']),
            ('era_d_fmt', orm['localedb.Locale:era_d_fmt']),
            ('alt_digits', orm['localedb.Locale:alt_digits']),
        ))
        db.send_create_signal('localedb', ['Locale'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'LocaleSiteDefault'
        db.delete_table('localedb_localesitedefault')
        
        # Deleting model 'Locale'
        db.delete_table('localedb_locale')
        
    
    
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
            'grouping': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
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
