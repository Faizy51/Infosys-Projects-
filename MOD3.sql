set define off
set verify off
set serveroutput on size 1000000
set feedback off
WHENEVER SQLERROR EXIT SQL.SQLCODE ROLLBACK
begin wwv_flow.g_import_in_progress := true; end; 
/
 
--       AAAA       PPPPP   EEEEEE  XX      XX
--      AA  AA      PP  PP  EE       XX    XX
--     AA    AA     PP  PP  EE        XX  XX
--    AAAAAAAAAA    PPPPP   EEEE       XXXX
--   AA        AA   PP      EE        XX  XX
--  AA          AA  PP      EE       XX    XX
--  AA          AA  PP      EEEEEE  XX      XX
begin
select value into wwv_flow_api.g_nls_numeric_chars from nls_session_parameters where parameter='NLS_NUMERIC_CHARACTERS';
execute immediate 'alter session set nls_numeric_characters=''.,''';
end;
/
-- Workspace, user group, user and team development export
-- Generated 2017.05.29 11:10:03 by MOD3
-- This script can be run in sqlplus as the owner of the Oracle Apex owner.
begin
    wwv_flow_api.set_security_group_id(p_security_group_id=>4900514680601033);
end;
/
----------------
-- W O R K S P A C E
-- Creating a workspace will not create database schemas or objects.
-- This API creates only the meta data for this APEX workspace
prompt  Creating workspace MOD3...
begin
wwv_flow_fnd_user_api.create_company (
  p_id                           => 4900629076601138,
  p_provisioning_company_id      => 4900514680601033,
  p_short_name                   => 'MOD3',
  p_first_schema_provisioned     => 'MOD3',
  p_company_schemas              => 'MOD3',
  p_expire_fnd_user_accounts     => '',
  p_account_lifetime_days        => '',
  p_fnd_user_max_login_failures  => '',
  p_allow_plsql_editing          => 'Y',
  p_allow_app_building_yn        => 'Y',
  p_allow_sql_workshop_yn        => 'Y',
  p_allow_websheet_dev_yn        => 'Y',
  p_allow_team_development_yn    => 'Y',
  p_allow_to_be_purged_yn        => 'Y',
  p_source_identifier            => 'MOD3',
  p_builder_notification_message => '');
end;
/
----------------
-- G R O U P S
--
prompt  Creating Groups...
----------------
-- U S E R S
-- User repository for use with apex cookie based authenticaion.
--
prompt  Creating Users...
begin
wwv_flow_fnd_user_api.create_fnd_user (
  p_user_id      => '4900418222601033',
  p_user_name    => 'MOD3',
  p_first_name   => '',
  p_last_name    => '',
  p_description  => '',
  p_email_address=> '',
  p_web_password => 'E9C195E4475C38D3B5D8977A972F8D0A',
  p_web_password_format => 'HEX_ENCODED_DIGEST_V2',
  p_group_ids    => '',
  p_developer_privs=> 'ADMIN:CREATE:DATA_LOADER:EDIT:HELP:MONITOR:SQL',
  p_default_schema=> 'MOD3',
  p_account_locked=> 'N',
  p_account_expiry=> to_date('201705270820','YYYYMMDDHH24MI'),
  p_failed_access_attempts=> 0,
  p_change_password_on_first_use=> 'N',
  p_first_password_use_occurred=> 'N',
  p_allow_app_building_yn=> 'Y',
  p_allow_sql_workshop_yn=> 'Y',
  p_allow_websheet_dev_yn=> 'Y',
  p_allow_team_development_yn=> 'Y',
  p_allow_access_to_schemas => '');
end;
/
commit;
begin 
execute immediate 'begin dbms_session.set_nls( param => ''NLS_NUMERIC_CHARACTERS'', value => '''''''' || replace(wwv_flow_api.g_nls_numeric_chars,'''''''','''''''''''') || ''''''''); end;';
end;
/
set verify on
set feedback on
prompt  ...done
