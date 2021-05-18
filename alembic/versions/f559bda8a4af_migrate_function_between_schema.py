"""migrate function between schema

Revision ID: f559bda8a4af
Revises: fbc26d0e27eb
Create Date: 2021-05-18 15:27:30.312423

"""
from alembic import op
import sqlalchemy as sa
from alembic_utils.pg_function import PGFunction

# revision identifiers, used by Alembic.
revision = 'f559bda8a4af'
down_revision = 'fbc26d0e27eb'
branch_labels = None
depends_on = None


bufferfunction = {
    'signature': """createbuffer(integer)""",
    'definition': """
  RETURNS TABLE(buffercreated geometry)
 LANGUAGE sql
AS $function$ 
    	    select ST_Transform(ST_Buffer(ST_Transform(geom, 3857), $1), 4326) 
    	    from public.geomtable
        $function$
;
    """
}

list_of_function_descriptions_to_migrate = [
bufferfunction
]

list_of_functions_in_public = [
    PGFunction(
        schema='public',
        signature=f['signature'],
        definition=f['definition']) for f in
    list_of_function_descriptions_to_migrate]
list_of_functions_in_tiger = [
    PGFunction(schema='tiger',
               signature=f['signature'],
               definition=f['definition']) for f in
    list_of_function_descriptions_to_migrate]

def upgrade():
    for function_in_public in list_of_functions_in_public:
        op.drop_entity(function_in_public)
    for function_in_tiger in list_of_functions_in_tiger:
        op.create_entity(function_in_tiger)


def downgrade():
    for function_in_tiger in list_of_functions_in_tiger:
        op.drop_entity(function_in_tiger)
    for function_in_public in list_of_functions_in_public:
        op.create_entity(function_in_public)
