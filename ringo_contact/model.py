import sqlalchemy as sa
from ringo.model import Base
from ringo.model.base import BaseItem, BaseFactory


class ContactFactory(BaseFactory):

    def create(self, user=None):
        new_item = BaseFactory.create(self, user)
        return new_item


class Contact(BaseItem, Base):
    """Docstring for contact extension"""

    __tablename__ = 'contacts'
    """Name of the table in the database for this modul. Do not
    change!"""
    _modul_id = None
    """Will be set dynamically. See include me of this modul"""

    # Define columns of the table in the database
    id = sa.Column(sa.Integer, primary_key=True)

    # Define relations to other tables

    @classmethod
    def get_item_factory(cls):
        return ContactFactory(cls)
