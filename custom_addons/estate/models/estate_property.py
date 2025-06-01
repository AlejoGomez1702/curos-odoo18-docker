from odoo import fields, models
from datetime import date, timedelta

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=lambda self: date.today() + timedelta(days=90) )
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ])
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], default='new', required=True, copy=False)

    # Una propiedad puede tener un solo tipo
    property_type_id = fields.Many2one('estate.property.type')

    # Vendedor y el comprador de la propiedad
    buyer_id = fields.Many2one('res.partner', copy=False)
    saleman_id = fields.Many2one('res.users', default=lambda self: self.env.user)

    # Relación cin el modelo de tags
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')