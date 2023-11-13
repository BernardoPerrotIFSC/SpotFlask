"""empty message

Revision ID: 6c542ab8a1b4
Revises: 600c5325f9af
Create Date: 2023-11-12 21:34:31.558171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c542ab8a1b4'
down_revision = '600c5325f9af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('historico',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('vento', sa.Float(), nullable=True),
    sa.Column('swell', sa.Float(), nullable=True),
    sa.Column('direcao', sa.Float(), nullable=True),
    sa.Column('data', sa.Date(), nullable=True),
    sa.Column('classicos', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('melhores')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('melhores',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('usuario_id', sa.INTEGER(), nullable=True),
    sa.Column('vento', sa.FLOAT(), nullable=True),
    sa.Column('swell', sa.FLOAT(), nullable=True),
    sa.Column('direcao', sa.FLOAT(), nullable=True),
    sa.Column('data', sa.DATE(), nullable=True),
    sa.Column('classicos', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('historico')
    # ### end Alembic commands ###
