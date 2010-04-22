# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Locale'
        db.create_table('localedb_locale', (
            ('abday_7', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('d_fmt', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('abday_5', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('abday_4', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('abday_3', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('abday_2', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('p_sep_by_space', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('abday_6', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('thousands_sep', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('abmon_11', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('t_fmt', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('era_d_fmt', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('abmon_3', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('mon_10', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('mon_grouping', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('era_year', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('mon_11', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('int_frac_digits', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('mon_12', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('abday_1', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('alt_digits', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('abmon_6', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('noexpr', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('int_curr_symbol', self.gf('django.db.models.fields.CharField')(max_length=4, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('abmon_9', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('era_d_t_fmt', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('n_cs_precedes', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('day_2', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('day_3', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('n_sign_posn', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('day_1', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('p_cs_precedes', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('day_7', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('day_4', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('day_5', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('mon_2', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('yesexpr', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('d_t_fmt', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('abmon_2', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('abmon_5', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('abmon_8', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('currency_symbol', self.gf('django.db.models.fields.CharField')(max_length=4, blank=True)),
            ('mon_thousands_sep', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('abmon_12', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('negative_sign', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('abmon_10', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('n_sep_by_space', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('abmon_7', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('positive_sign', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('mon_7', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('mon_decimal_point', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('mon_3', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('abmon_1', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('mon_1', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('mon_6', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('mon_4', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('mon_5', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('day_6', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('t_fmt_ampm', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('mon_9', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('abmon_4', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('era', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('codeset', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('decimal_point', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('p_sign_posn', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('mon_8', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('grouping', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
        ))
        db.send_create_signal('localedb', ['Locale'])

        # Adding model 'LocaleSiteDefault'
        db.create_table('localedb_localesitedefault', (
            ('locale', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['localedb.Locale'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sites.Site'], unique=True)),
        ))
        db.send_create_signal('localedb', ['LocaleSiteDefault'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Locale'
        db.delete_table('localedb_locale')

        # Deleting model 'LocaleSiteDefault'
        db.delete_table('localedb_localesitedefault')
    
    
    models = {
        'localedb.locale': {
            'Meta': {'object_name': 'Locale'},
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
            'Meta': {'object_name': 'LocaleSiteDefault'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locale': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localedb.Locale']"}),
            'site': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['sites.Site']", 'unique': 'True'})
        },
        'sites.site': {
            'Meta': {'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['localedb']
