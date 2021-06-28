"""bulk insert geometry data

Revision ID: ae713519a1ae
Revises: 6ebdf8367772
Create Date: 2021-04-29 16:41:04.664394

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from geoalchemy2.types import Geometry
from sqlalchemy import String, Integer

# revision identifiers, used by Alembic.
revision = 'ae713519a1ae'
down_revision = '6ebdf8367772'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('CREATE SCHEMA IF NOT EXISTS tiger')
    # Create an ad-hoc table to use for the insert statement.
    geomtable = table('geomtable',
        column('id', Integer),
        column('name', String),
        column('description', String),
        column('club', String),
        column('geom', Geometry(geometry_type='POINT', srid=4326))
    )
    op.bulk_insert(geomtable,
        [
            {'id':1, 'name':'Cristiano Ronaldo',
                    'description':'Le meilleur au monde', 
                    'club':'Juventus Turin',
                    "geom": "SRID=4326;POINT(7.742615 45.116177)"},
            {'id':2, 'name':'Zinedine Zidane',
                    'description':'Le meilleur de l"hstoire', 
                    'club':'Real Madrid',
                    "geom": "SRID=4326;POINT(-3.703790 40.416775)"},
            {'id':3, 'name':'Neymar Junior',
                    'description':'Le talent', 
                    'club':'Paris St Germain',
                    "geom": "SRID=4326;POINT(2.3488 48.8534)"},
        ]
    )  

def downgrade():
     op.execute(
        """DELETE FROM geomtable WHERE name IN (
   'Cristiano Ronaldo' ,
   'Zinedine Zidane',
   'Neymar Junior'
               );"""
    )
