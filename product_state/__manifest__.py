# Copyright 2017 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Product State",
    "summary": """
        Module introducing a state field on product template""",
    "author": "ACSONE SA/NV, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/product-attribute",
    "category": "Product",
    "version": "14.0.1.0.1",
    "license": "AGPL-3",
    "depends": ["product", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "data/product_state_data.xml",
        "views/product_template.xml",
    ],
    "application": False,
    "maintainers": ["emagdalenaC2i"],
    "post_init_hook": "post_init_hook",
}
