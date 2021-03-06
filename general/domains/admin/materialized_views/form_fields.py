from general.database.session_scope import session_scope


def create_form_fields_materialized_view():
    with session_scope() as session:
        session.execute("""
            DROP MATERIALIZED VIEW IF EXISTS admin.form_fields CASCADE;
        """)
        session.execute("""
            CREATE MATERIALIZED VIEW admin.form_fields AS
                SELECT 
                    replace(params.specific_schema, '_api', '') AS schema_name,
                    routines.routine_name as form_name,
                    params.ordinal_position,
                    params.parameter_mode,
                    params.parameter_name as field_name,
                    params.data_type as field_type
                FROM information_schema.parameters params
                LEFT JOIN information_schema.routines routines 
                    ON routines.specific_name = params.specific_name
                WHERE params.specific_schema LIKE '%_api'
                  AND params.parameter_mode = 'IN';
        """)

if __name__ == '__main__':
    create_form_fields_materialized_view()

# SELECT (row_number() OVER())::INT id, sub1.* FROM
# (SELECT pg_proc.proname as form_name,
#                            unnest(pg_proc.proargnames) as name
# FROM pg_catalog.pg_proc) sub1
# ;