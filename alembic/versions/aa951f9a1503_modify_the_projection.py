"""modify the projection

Revision ID: aa951f9a1503
Revises: f559bda8a4af
Create Date: 2021-06-04 17:55:55.962483

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from geoalchemy2.types import Geometry
from sqlalchemy import String, Integer

# revision identifiers, used by Alembic.
revision = 'aa951f9a1503'
down_revision = 'f559bda8a4af'
branch_labels = None
depends_on = None


def upgrade():
     # Create an ad-hoc table to use for the insert statement.
    mtlwifi = table('mtlwifi_bornes',
        column('id_0', Integer),
        column('geom', Geometry(geometry_type='POINT', srid=32188)),
        column('id', String),
        column('lieu', String),
        column('latitude', String),
        column('longitude', String),
        column('x', String),
        column('y', String),
        column('type', String),
        column('arrondisse', String),
        column('zone activ', String),
    )

    op.execute(
        'alter table "mtlwifi_bornes" rename column wkb_geometry to geom'
    )

    op.execute(
        'alter table "mtlwifi_bornes" alter column geom type geometry(POINT, 4326) using st_transform(geom, 4326)'
    )

def downgrade():
    op.execute(
        'alter table "mtlwifi_bornes" alter column geom type geometry(POINT, 32188) using st_transform(geom, 32188)'
    )

    op.execute(
        'alter table "mtlwifi_bornes" rename column geom to wkb_geometry'
    )