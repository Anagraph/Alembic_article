"""create function

Revision ID: fbc26d0e27eb
Revises: ae713519a1ae
Create Date: 2021-04-30 10:21:42.313883

"""
from alembic import op
import sqlalchemy as sa
from alembic_utils.pg_function import PGFunction

# revision identifiers, used by Alembic.
revision = 'fbc26d0e27eb'
down_revision = 'ae713519a1ae'
branch_labels = None
depends_on = None


def upgrade():
    public_to_upper = PGFunction(
        schema="public",
        signature="createbuffer(integer)",
        definition="""
        RETURNS TABLE(buffercreated geometry)
        LANGUAGE sql
            AS $function$ 
    	    select ST_Transform(ST_Buffer(ST_Transform(geom, 3857), $1), 4326) 
    	    from public.geomtable
        $function$
        ;
        """
    )

    op.create_entity(public_to_upper)


def downgrade():
    public_to_upper = PGFunction(
        schema="public",
        signature="createbuffer(integer)",
        definition="# Not Used"
    )

    op.drop_entity(public_to_upper)
