"""empty message

Revision ID: d6a6b943b492
Revises: e5f8690b4f83
Create Date: 2023-12-08 15:53:13.057266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6a6b943b492'
down_revision = 'e5f8690b4f83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('historico2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('vento', sa.Float(), nullable=True),
    sa.Column('swell', sa.Float(), nullable=True),
    sa.Column('direcao', sa.Float(), nullable=True),
    sa.Column('data', sa.Date(), nullable=True),
    sa.Column('picos', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('historico2')
    # ### end Alembic commands ###