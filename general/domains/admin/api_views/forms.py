from general.database.session_scope import session_scope


def create_forms_view():
    with session_scope() as session:
        session.execute("""
        DROP VIEW IF EXISTS admin_api.forms CASCADE;
        """)
        session.execute("""
          CREATE OR REPLACE VIEW admin_api.forms AS
            SELECT (row_number() OVER())::INT id, *
            FROM (
                SELECT 
                       dfs.custom_button_copy,
                       dfs.custom_name,
                       dfs.dialog_settings,
                       dfs.form_name,
                       dfs.schema_name,
                       dfs.user_id
                FROM admin.default_form_settings dfs
                WHERE dfs."user" = current_user
            ) sub;
        """)
