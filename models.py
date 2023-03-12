# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class KipoAdminRegBs(models.Model):
    registernumber = models.TextField(db_column='registerNumber', blank=True, null=True)  # Field name made lowercase.
    registerationdate = models.TextField(db_column='registerationDate', blank=True, null=True)  # Field name made lowercase.
    examinationdate = models.TextField(db_column='examinationDate', blank=True, null=True)  # Field name made lowercase.
    existduringdate = models.TextField(db_column='existDuringDate', blank=True, null=True)  # Field name made lowercase.
    lapscause = models.TextField(db_column='lapsCause', blank=True, null=True)  # Field name made lowercase.
    lapsdate = models.TextField(db_column='lapsDate', blank=True, null=True)  # Field name made lowercase.
    applicationnumber = models.TextField(db_column='applicationNumber', blank=True, null=True)  # Field name made lowercase.
    applicationdate = models.TextField(db_column='applicationDate', blank=True, null=True)  # Field name made lowercase.
    publicationnumber = models.TextField(db_column='publicationNumber', blank=True, null=True)  # Field name made lowercase.
    publicationdate = models.TextField(db_column='publicationDate', blank=True, null=True)  # Field name made lowercase.
    internationregistrationnumber = models.TextField(db_column='internationRegistrationNumber', blank=True, null=True)  # Field name made lowercase.
    internationregistrationdate = models.TextField(db_column='internationRegistrationDate', blank=True, null=True)  # Field name made lowercase.
    originalapplicationnumber = models.TextField(db_column='originalApplicationNumber', blank=True, null=True)  # Field name made lowercase.
    originalapplicationdate = models.TextField(db_column='originalApplicationDate', blank=True, null=True)  # Field name made lowercase.
    classificationcode = models.TextField(db_column='classificationCode', blank=True, null=True)  # Field name made lowercase.
    inventiontitle = models.TextField(db_column='inventionTitle', blank=True, null=True)  # Field name made lowercase.
    inventiontitleeng = models.TextField(db_column='inventionTitleEng', blank=True, null=True)  # Field name made lowercase.
    claimcount = models.TextField(db_column='claimCount', blank=True, null=True)  # Field name made lowercase.
    prioritycountry = models.TextField(db_column='priorityCountry', blank=True, null=True)  # Field name made lowercase.
    prioritydate = models.TextField(db_column='priorityDate', blank=True, null=True)  # Field name made lowercase.
    prioritycount = models.TextField(db_column='priorityCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KIPO_ADMIN_REG_BS'


class LastRightHolder(models.Model):
    last_right_holder_number = models.TextField(db_column='LAST_RIGHT_HOLDER_NUMBER', blank=True, null=True)  # Field name made lowercase.
    last_right_holder_name = models.TextField(db_column='LAST_RIGHT_HOLDER_NAME', blank=True, null=True)  # Field name made lowercase.
    last_right_holder_address = models.TextField(db_column='LAST_RIGHT_HOLDER_ADDRESS', blank=True, null=True)  # Field name made lowercase.
    last_right_holder_country = models.TextField(db_column='LAST_RIGHT_HOLDER_COUNTRY', blank=True, null=True)  # Field name made lowercase.
    registration_number = models.TextField(db_column='REGISTRATION_NUMBER', blank=True, null=True)  # Field name made lowercase.
    transfer_date = models.DateTimeField(db_column='TRANSFER_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LAST_RIGHT_HOLDER'


class RegistrationFee(models.Model):
    registration_date = models.TextField(db_column='REGISTRATION_DATE', blank=True, null=True)  # Field name made lowercase.
    start_annual = models.TextField(db_column='START_ANNUAL', blank=True, null=True)  # Field name made lowercase.
    last_annual = models.TextField(db_column='LAST_ANNUAL', blank=True, null=True)  # Field name made lowercase.
    ent_degree = models.TextField(db_column='ENT_DEGREE', blank=True, null=True)  # Field name made lowercase.
    payment_fee = models.TextField(db_column='PAYMENT_FEE', blank=True, null=True)  # Field name made lowercase.
    payment_date = models.TextField(db_column='PAYMENT_DATE', blank=True, null=True)  # Field name made lowercase.
    registration_number = models.TextField(db_column='REGISTRATION_NUMBER', blank=True, null=True)  # Field name made lowercase.
    transfer_date = models.DateTimeField(db_column='TRANSFER_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REGISTRATION_FEE'


class RegistrationRightHolderA(models.Model):
    rank_number = models.TextField(db_column='RANK_NUMBER', blank=True, null=True)  # Field name made lowercase.
    rank_correlator_serial_number = models.TextField(db_column='RANK_CORRELATOR_SERIAL_NUMBER', blank=True, null=True)  # Field name made lowercase.
    rank_correlator_type = models.TextField(db_column='RANK_CORRELATOR_TYPE', blank=True, null=True)  # Field name made lowercase.
    rank_correlator_name = models.TextField(db_column='RANK_CORRELATOR_NAME', blank=True, null=True)  # Field name made lowercase.
    rank_correlator_address = models.TextField(db_column='RANK_CORRELATOR_ADDRESS', blank=True, null=True)  # Field name made lowercase.
    registration_number = models.TextField(db_column='REGISTRATION_NUMBER', blank=True, null=True)  # Field name made lowercase.
    transfer_date = models.DateTimeField(db_column='TRANSFER_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REGISTRATION_RIGHT_HOLDER_A'


class RegistrationRightHolderB(models.Model):
    rank_number = models.CharField(db_column='RANK_NUMBER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    document_name = models.CharField(db_column='DOCUMENT_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    receipt_date = models.CharField(db_column='RECEIPT_DATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    registration_cause_name = models.CharField(db_column='REGISTRATION_CAUSE_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    indecation_of_event = models.CharField(db_column='INDECATION_OF_EVENT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    registration_number = models.CharField(db_column='REGISTRATION_NUMBER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    transfer_date = models.DateTimeField(db_column='TRANSFER_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REGISTRATION_RIGHT_HOLDER_B'


class RegistrationRightRank(models.Model):
    rank_number = models.TextField(db_column='RANK_NUMBER', blank=True, null=True)  # Field name made lowercase.
    pertinent_partition = models.TextField(db_column='PERTINENT_PARTITION', blank=True, null=True)  # Field name made lowercase.
    document_name = models.TextField(db_column='DOCUMENT_NAME', blank=True, null=True)  # Field name made lowercase.
    original_registration_number = models.TextField(db_column='ORIGINAL_REGISTRATION_NUMBER', blank=True, null=True)  # Field name made lowercase.
    registration_purpose = models.TextField(db_column='REGISTRATION_PURPOSE', blank=True, null=True)  # Field name made lowercase.
    registration_date = models.TextField(db_column='REGISTRATION_DATE', blank=True, null=True)  # Field name made lowercase.
    registration_cause_name = models.TextField(db_column='REGISTRATION_CAUSE_NAME', blank=True, null=True)  # Field name made lowercase.
    registration_cause_date = models.TextField(db_column='REGISTRATION_CAUSE_DATE', blank=True, null=True)  # Field name made lowercase.
    receipt_number = models.TextField(db_column='RECEIPT_NUMBER', blank=True, null=True)  # Field name made lowercase.
    receipt_date = models.TextField(db_column='RECEIPT_DATE', blank=True, null=True)  # Field name made lowercase.
    disappearance_flag = models.TextField(db_column='DISAPPEARANCE_FLAG', blank=True, null=True)  # Field name made lowercase.
    disappearance_cause_name = models.TextField(db_column='DISAPPEARANCE_CAUSE_NAME', blank=True, null=True)  # Field name made lowercase.
    disappearance_date = models.TextField(db_column='DISAPPEARANCE_DATE', blank=True, null=True)  # Field name made lowercase.
    international_reg_record_date_md = models.TextField(db_column='INTERNATIONAL_REG_RECORD_DATE_MD', blank=True, null=True)  # Field name made lowercase.
    expiration_date_md = models.TextField(db_column='EXPIRATION_DATE_MD', blank=True, null=True)  # Field name made lowercase.
    latest_renewal_date_md = models.TextField(db_column='LATEST_RENEWAL_DATE_MD', blank=True, null=True)  # Field name made lowercase.
    sub_designation_date_md = models.TextField(db_column='SUB_DESIGNATION_DATE_MD', blank=True, null=True)  # Field name made lowercase.
    registration_number = models.TextField(db_column='REGISTRATION_NUMBER', blank=True, null=True)  # Field name made lowercase.
    transfer_date = models.DateTimeField(db_column='TRANSFER_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REGISTRATION_RIGHT_RANK'


class RegUpdateHistory(models.Model):
    registration_number = models.TextField(db_column='REGISTRATION_NUMBER', blank=True, null=True)  # Field name made lowercase.
    registration = models.TextField(db_column='REGISTRATION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REG_UPDATE_HISTORY'


class RightHolder(models.Model):
    pertinent_partition = models.CharField(db_column='PERTINENT_PARTITION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rank_number = models.CharField(db_column='RANK_NUMBER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    registration_date = models.CharField(db_column='REGISTRATION_DATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rank_correlator_serial_number = models.CharField(db_column='RANK_CORRELATOR_SERIAL_NUMBER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rank_correlator_number = models.CharField(db_column='RANK_CORRELATOR_NUMBER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rank_correlator_type = models.CharField(db_column='RANK_CORRELATOR_TYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rank_correlator_name = models.CharField(db_column='RANK_CORRELATOR_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rank_correlator_address = models.CharField(db_column='RANK_CORRELATOR_ADDRESS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    transfer_date = models.DateTimeField(db_column='TRANSFER_DATE', blank=True, null=True)  # Field name made lowercase.
    registration_number = models.CharField(db_column='REGISTRATION_NUMBER', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIGHT_HOLDER'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class RightholderbQuery(models.Model):
    rank_number = models.CharField(db_column='RANK_NUMBER', max_length=2, blank=True, null=True)  # Field name made lowercase.
    document_name = models.CharField(db_column='DOCUMENT_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    receipt_date = models.CharField(db_column='RECEIPT_DATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    registration_cause_name = models.CharField(db_column='REGISTRATION_CAUSE_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    indecation_of_event = models.CharField(db_column='INDECATION_OF_EVENT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    registration_number = models.CharField(db_column='REGISTRATION_NUMBER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    transfer_date = models.DateTimeField(db_column='TRANSFER_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rightHolderB_query'
