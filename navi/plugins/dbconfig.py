from .database import new_db_connection, create_table


def create_keys_table():
    database = r"navi.db"
    key_conn = new_db_connection(database)
    key_table = """CREATE TABLE IF NOT EXISTS keys (
                            access_key text,
                            secret_key text
                            );"""
    create_table(key_conn, key_table)


def create_passwords_table():
    database = r"navi.db"
    ssh_conn = new_db_connection(database)
    ssh_table = """CREATE TABLE IF NOT EXISTS ssh (
                            username text,
                            password text
                            );"""
    create_table(ssh_conn, ssh_table)


def create_diff_table():
    database = r"navi.db"
    diff_conn = new_db_connection(database)
    diff_table = """CREATE TABLE IF NOT EXISTS diff (
                        update_id integer PRIMARY KEY,
                        timestamp text,
                        days text,
                        update_type text,
                        exid text);"""
    create_table(diff_conn, diff_table)


def create_vulns_table():
    database = r"navi.db"
    vuln_conn = new_db_connection(database)
    vuln_table = """CREATE TABLE IF NOT EXISTS vulns (
                            asset_ip text, 
                            asset_uuid text, 
                            asset_hostname text, 
                            first_found text, 
                            last_found text, 
                            output text, 
                            plugin_id text, 
                            plugin_name text, 
                            plugin_family text, 
                            port text, 
                            protocol text, 
                            severity text, 
                            scan_completed text, 
                            scan_started text, 
                            scan_uuid text, 
                            schedule_id text, 
                            state text,
                            cves text,
                            score text,
                            exploit text
                            );"""
    vuln_conn.execute('pragma journal_mode=wal;')
    create_table(vuln_conn, vuln_table)


def create_assets_table():
    database = r"navi.db"
    asset_conn = new_db_connection(database)
    create_asset_table = """CREATE TABLE IF NOT EXISTS assets (
                            ip_address text,
                            hostname text,
                            fqdn text,
                            uuid text PRIMARY KEY,
                            first_found text,
                            last_found text, 
                            operating_system text,
                            mac_address text, 
                            agent_uuid text,
                            last_licensed_scan_date text,
                            network text,
                            acr text,
                            aes text,
                            aws_id text
                            );"""
    asset_conn.execute('pragma journal_mode=wal;')
    create_table(asset_conn, create_asset_table)


def create_tag_table():
    database = r"navi.db"
    tag_conn = new_db_connection(database)
    create_tags_table = """CREATE TABLE IF NOT EXISTS tags (
                        tag_id integer PRIMARY KEY,
                        asset_uuid text,
                        asset_ip,
                        tag_key text,
                        tag_uuid text,
                        tag_value text,
                        tag_added_date text
                        );"""
    tag_conn.execute('pragma journal_mode=wal;')
    create_table(tag_conn, create_tags_table)


def create_apps_table():
    database = r"navi.db"
    app_conn = new_db_connection(database)
    create_apps = """CREATE TABLE IF NOT EXISTS apps (
                            name text,
                            uuid text PRIMARY KEY, 
                            target text, 
                            scan_completed_time text,
                            pages_audited text,
                            pages_crawled text,
                            requests_made text, 
                            critical_count text,
                            high_count text,
                            medium_count text,
                            low_count text, 
                            info_count text,
                            owasp text,
                            tech_list text,
                            config_id text
                            );"""
    app_conn.execute('pragma journal_mode=wal;')

    create_table(app_conn, create_apps)


def create_compliance_table():
    database = r"navi.db"
    compliance_conn = new_db_connection(database)
    create_compliance = """CREATE TABLE IF NOT EXISTS compliance (
                            asset_uuid text,
                            actual_value text,
                            audit_file text,
                            check_id text,
                            check_info text,
                            check_name text,
                            expected_value text,
                            first_seen text,
                            last_seen text,
                            plugin_id text,
                            reference text,
                            see_also text,
                            solution text,
                            status text 
                            );"""

    create_table(compliance_conn, create_compliance)
