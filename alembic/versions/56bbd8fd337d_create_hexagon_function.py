"""create hexagon function

Revision ID: 56bbd8fd337d
Revises: aa951f9a1503
Create Date: 2021-06-17 13:24:12.755082

"""
from alembic import op
import sqlalchemy as sa
from alembic_utils.pg_function import PGFunction


# revision identifiers, used by Alembic.
revision = '56bbd8fd337d'
down_revision = 'aa951f9a1503'
branch_labels = None
depends_on = None


def upgrade():
    create_hexes = PGFunction(
        schema="public",
        signature="create_hexes(resolution integer)",
        definition="""
        RETURNS TABLE(hexa_id text, hexa_geom geometry)
        LANGUAGE plpgsql
        AS $function$
        begin
            return query
                with envelope as (
                    select st_envelope(geom) geom from "quartiers_sociologiques"
                ), h3_id as (
                    select h3_polyfill(geom, resolution) id from envelope
                ), h3 as (
                    select id, st_setsrid(h3_h3index_to_geoboundary(id), 4326) geom from h3_id
                )
                select h3.id, h3.geom from h3;
        end;$function$
        ;
        """
    )

    op.create_entity(create_hexes)


def downgrade():
    create_hexes = PGFunction(
        schema="public",
        signature="create_hexes(resolution integer)",
        definition="# Not Used"
    )

    op.drop_entity(create_hexes)
