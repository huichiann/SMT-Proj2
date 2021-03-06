"""empty message

Revision ID: 8bfec97e4882
Revises: 
Create Date: 2019-03-22 16:40:56.898091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bfec97e4882'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('challenge',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('start', sa.DateTime(), nullable=True),
    sa.Column('end', sa.DateTime(), nullable=True),
    sa.Column('daily_steps_quota', sa.Integer(), nullable=False),
    sa.Column('reward', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('contactnumber', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('contactnumber'),
    sa.UniqueConstraint('email')
    )
    op.create_table('steps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('steps', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_challenge',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('challenge_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['challenge_id'], ['challenge.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'challenge_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_challenge')
    op.drop_table('steps')
    op.drop_table('user')
    op.drop_table('challenge')
    # ### end Alembic commands ###
