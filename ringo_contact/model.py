import sqlalchemy as sa
from ringo.model import Base
from ringo.model.mixins import Meta, Owned
from ringo.model.base import BaseItem, BaseFactory


class ContactFactory(BaseFactory):

    def create(self, user=None):
        new_item = BaseFactory.create(self, user)
        return new_item


class Contact(BaseItem, Meta, Owned, Base):
    """Docstring for contact extension"""

    __tablename__ = 'contacts'
    """Name of the table in the database for this modul. Do not
    change!"""
    _modul_id = None
    """Will be set dynamically. See include me of this modul"""

    # Define columns of the table in the database
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String, nullable=False, default="")
    fn = sa.Column(sa.String, nullable=False, default="")
    org = sa.Column(sa.String, nullable=False, default="")
    role = sa.Column(sa.String, nullable=False, default="")
    bday = sa.Column(sa.Date)
    gender = sa.Column(sa.Integer, nullable=False, default="")

    postalcode = sa.Column(sa.String, nullable=False, default="")
    city = sa.Column(sa.String, nullable=False, default="")
    street = sa.Column(sa.String, nullable=False, default="")

    phone = sa.Column(sa.String, nullable=False, default="")
    email = sa.Column(sa.String, nullable=False, default="")
    url = sa.Column(sa.String, nullable=False, default="")

    note = sa.Column(sa.Text, nullable=False, default="")

    @classmethod
    def get_item_factory(cls):
        return ContactFactory(cls)
