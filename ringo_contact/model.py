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
    title = sa.Column(sa.String)
    fn = sa.Column(sa.String)
    org = sa.Column(sa.String)
    role = sa.Column(sa.String)
    bday = sa.Column(sa.Date)
    gender = sa.Column(sa.Integer)

    postcode = sa.Column(sa.String)
    city = sa.Column(sa.String)
    street = sa.Column(sa.String)

    phone = sa.Column(sa.String)
    email = sa.Column(sa.String)
    url = sa.Column(sa.String)

    note = sa.Column(sa.Text)

    @classmethod
    def get_item_factory(cls):
        return ContactFactory(cls)
