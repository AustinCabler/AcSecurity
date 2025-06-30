# Logger using pandas for structured logging

import pandas as pd
from datetime import datetime
import os

LOG_FILE = "acsecurity_log.csv"

def _write_log(event_type, message, details=None):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "event_type": event_type,
        "message": message,
        "details": details if details is not None else ""
    }
    # If file exists, append; else, create new DataFrame
    if os.path.exists(LOG_FILE):
        df = pd.read_csv(LOG_FILE)
        df = pd.concat([df, pd.DataFrame([log_entry])], ignore_index=True)
    else:
        df = pd.DataFrame([log_entry])
    df.to_csv(LOG_FILE, index=False)

def log_info(message, details=None):
    _write_log("INFO", message, details)

def log_warning(message, details=None):
    _write_log("WARNING", message, details)

def log_error(message, details=None):
    _write_log("ERROR", message, details)

def log_debug(message, details=None):
    _write_log("DEBUG", message, details)

def log_critical(message, details=None):
    _write_log("CRITICAL", message, details)

def log_exception(exception, details=None):
    _write_log("EXCEPTION", str(exception), details)

def log_access(username, action, details=None):
    _write_log("ACCESS", f"Access attempt by {username}: {action}", details)

def log_security_event(event, details=None):
    _write_log("SECURITY_EVENT", event, details)

def log_system_event(event, details=None):
    _write_log("SYSTEM_EVENT", event, details)

def log_configuration_change(change, details=None):
    _write_log("CONFIG_CHANGE", change, details)

def log_performance_metric(metric, value, details=None):
    _write_log("PERFORMANCE", f"{metric} = {value}", details)

def log_user_activity(username, activity, details=None):
    _write_log("USER_ACTIVITY", f"{username}: {activity}", details)

def log_network_activity(activity, details=None):
    _write_log("NETWORK_ACTIVITY", activity, details)

def log_suspicious_activity(activity, details=None):
    _write_log("SUSPICIOUS_ACTIVITY", activity, details)

def log_audit_trail(event, details=None):
    _write_log("AUDIT_TRAIL", event, details)

def log_system_health(health_status, details=None):
    _write_log("SYSTEM_HEALTH", health_status, details)

def log_data_access(username, data_access, details=None):
    _write_log("DATA_ACCESS", f"{username}: {data_access}", details)

def log_backup_event(event, details=None):
    _write_log("BACKUP_EVENT", event, details)

def log_restore_event(event, details=None):
    _write_log("RESTORE_EVENT", event, details)

def log_update_event(event, details=None):
    _write_log("UPDATE_EVENT", event, details)

def log_shutdown_event(event, details=None):
    _write_log("SHUTDOWN_EVENT", event, details)

def log_startup_event(event, details=None):
    _write_log("STARTUP_EVENT", event, details)

def log_user_login(username, details=None):
    _write_log("USER_LOGIN", f"{username} logged in.", details)

def log_user_logout(username, details=None):
    _write_log("USER_LOGOUT", f"{username} logged out.", details)

def log_configuration_backup(backup_details, details=None):
    _write_log("CONFIG_BACKUP", backup_details, details)

def log_configuration_restore(restore_details, details=None):
    _write_log("CONFIG_RESTORE", restore_details, details)

def log_security_policy_change(change_details, details=None):
    _write_log("SECURITY_POLICY_CHANGE", change_details, details)

def log_system_error(error_message, details=None):
    _write_log("SYSTEM_ERROR", error_message, details)

def log_system_warning(warning_message, details=None):
    _write_log("SYSTEM_WARNING", warning_message, details)

def log_system_info(info_message, details=None):
    _write_log("SYSTEM_INFO", info_message, details)

def log_system_debug(debug_message, details=None):
    _write_log("SYSTEM_DEBUG", debug_message, details)

def log_system_critical(critical_message, details=None):
    _write_log("SYSTEM_CRITICAL", critical_message, details)

def log_user_registration(username, details=None):
    _write_log("USER_REGISTRATION", f"{username} registered.", details)

def log_user_deletion(username, details=None):
    _write_log("USER_DELETION", f"{username} deleted.", details)

def log_user_update(username, update_details, details=None):
    _write_log("USER_UPDATE", f"{username} updated: {update_details}", details)

def log_user_password_change(username, details=None):
    _write_log("USER_PASSWORD_CHANGE", f"{username} changed password.", details)

def log_user_role_change(username, new_role, details=None):
    _write_log("USER_ROLE_CHANGE", f"{username} role changed to {new_role}.", details)

def log_user_permission_change(username, permissions, details=None):
    _write_log("USER_PERMISSION_CHANGE", f"{username} permissions changed: {permissions}", details)

def log_user_session_start(username, details=None):
    _write_log("USER_SESSION_START", f"{username} session started.", details)

def log_user_session_end(username, details=None):
    _write_log("USER_SESSION_END", f"{username} session ended.", details)

def log_user_activity_summary(username, activity_summary, details=None):
    _write_log("USER_ACTIVITY_SUMMARY", f"{username} activity summary: {activity_summary}", details)

def log_system_shutdown(details=None):
    _write_log("SYSTEM_SHUTDOWN", "System is shutting down.", details)

def log_system_startup(details=None):
    _write_log("SYSTEM_STARTUP", "System has started up.", details)

def log_system_maintenance(maintenance_details, details=None):
    _write_log("SYSTEM_MAINTENANCE", maintenance_details, details)

def log_system_upgrade(upgrade_details, details=None):
    _write_log("SYSTEM_UPGRADE", upgrade_details, details)

def log_system_downtime(downtime_details, details=None):
    _write_log("SYSTEM_DOWNTIME", downtime_details, details)

def log_system_performance(performance_metrics, details=None):
    _write_log("SYSTEM_PERFORMANCE", performance_metrics, details)

def log_system_security(security_metrics, details=None):
    _write_log("SYSTEM_SECURITY", security_metrics, details)

def log_system_configuration(configuration_details, details=None):
    _write_log("SYSTEM_CONFIGURATION", configuration_details, details)

def log_system_compliance(compliance_status, details=None):
    _write_log("SYSTEM_COMPLIANCE", compliance_status, details)

def log_system_audit(audit_details, details=None):
    _write_log("SYSTEM_AUDIT", audit_details, details)

def log_system_backup(backup_details, details=None):
    _write_log("SYSTEM_BACKUP", backup_details, details)

def log_system_restore(restore_details, details=None):
    _write_log("SYSTEM_RESTORE", restore_details, details)