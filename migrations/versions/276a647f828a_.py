"""empty message

Revision ID: 276a647f828a
Revises: None
Create Date: 2015-06-26 15:13:05.579248

"""

# revision identifiers, used by Alembic.
revision = '276a647f828a'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cre',
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('version', sa.Integer(), nullable=False),
    sa.Column('template', sa.String(), nullable=True),
    sa.Column('infills', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('code', 'version')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cre')
    ### end Alembic commands ###