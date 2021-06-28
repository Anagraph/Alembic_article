"""create geometric table

Revision ID: 6ebdf8367772
Revises: 
Create Date: 2021-04-29 15:56:32.692696

"""
from alembic import op
import sqlalchemy as sa
from geoalchemy2.types import Geometry

# revision identifiers, used by Alembic.
revision = '6ebdf8367772'
down_revision = '19a48e8d11d3'
branch_labels = None
depends_on = None

def upgrade():

    op.create_table(
        'geomtable',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
        sa.Column('club', sa.String(50), nullable=False),
        sa.Column('geom', Geometry(geometry_type='POINT', srid=4326), nullable=True),
    )

def downgrade():
    op.drop_table('geomtable')
