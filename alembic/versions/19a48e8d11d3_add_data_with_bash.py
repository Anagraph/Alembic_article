"""add data with bash

Revision ID: 19a48e8d11d3
Revises: 56bbd8fd337d
Create Date: 2021-06-28 09:34:13.410514

"""
import os

from alembic import op


# revision identifiers, used by Alembic.
revision = '19a48e8d11d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    op.execute(
        'create extension IF NOT EXISTS postgis'
    )

    op.execute(
        'create extension IF NOT EXISTS pgh3'
    )

    os.system('/etl/data_load.sh')


def downgrade():
    pass
    # op.drop_table('testdata')
