"""added_configurations_table

Revision ID: 3356a2f89a33
Revises: 35e47f20475b
Create Date: 2023-06-06 10:51:15.111738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3356a2f89a33'
down_revision = '35e47f20475b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('configurations',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('organisation_id', sa.Integer(), nullable=True),
    sa.Column('key', sa.String(), nullable=True),
    sa.Column('value', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_aea_step_id', table_name='agent_executions')
    op.drop_index('ix_ats_unique_id', table_name='agent_template_steps')
    op.drop_index('ix_at_name', table_name='agent_templates')
    op.drop_index('ix_agents_agnt_template_id', table_name='agents')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_agents_agnt_template_id', 'agents', ['agent_template_id'], unique=False)
    op.create_index('ix_at_name', 'agent_templates', ['name'], unique=False)
    op.create_index('ix_ats_unique_id', 'agent_template_steps', ['unique_id'], unique=False)
    op.create_index('ix_aea_step_id', 'agent_executions', ['current_step_id'], unique=False)
    op.drop_table('configurations')
    # ### end Alembic commands ###
