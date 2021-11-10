"""empty message

Revision ID: a14e6ea5e3ac
Revises: 3b292edae342
Create Date: 2021-09-17 04:02:28.971975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a14e6ea5e3ac'
down_revision = '3b292edae342'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
